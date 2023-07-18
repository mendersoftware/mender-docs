---
title: Mender Server
taxonomy:
    category: docs
    label: tutorial
---


!!!!! Mutual TLS authentication is only available in the Mender Enterprise plan.
!!!!! To gain access to the mtls proxy container before you are an Enterprise customer please [contact us](https://mender.io/contact-us). 
!!!!! In the message please mention the 'Evaluation of the mtls proxy'.

## mTLS Ambassador
The mTLS Ambassador is an optional component to add Mutual TLS authentication between the Mender Client and the Mender Backend.

## Prerequisites
* A valid TLS Server certificate named `cert.crt`
* A valid TLS Key named `private.key`
* A CA shared with your device fleet named `ca.crt`
* Valid access to the Mender Enterprise Container Registry. Please email contact@mender.io to receive an evaluation account.
* A Mender user: this is used for device authentication purposes

## Create required secrets
* Create a new Mender user in the Mender UI and take note of the username and password.
* Create the Kubernetes secret:
  ```bash
  export MENDER_USERNAME=username@example.org
  export MENDER_PASSWORD=usernamepassword
  kubectl create secret generic mtls-user --from-literal=MTLS_MENDER_USER=${MENDER_USERNAME} --from-literal=MTLS_MENDER_PASS=${MENDER_PASSWORD}
  ```
* Create the keycert secret:
  ```bash
  kubectl create secret generic keycert --from-file=cert.crt=./cert.crt --from-file=private.key=./private.key
  ```
* Create the CA secret:
  ```bash
  kubectl create secret generic mtls-ca --from-file=ca.crt=./ca.crt
  ```
* Create the registry secret:
  ```bash
  kubectl create secret docker-registry registry-mtls-secret --docker-server=registry.mender.io --docker-username=<your username> --docker-password=<your password>
  ```

## mTLS Deployment
* Create the following Kubernetes resource:
<!--AUTOVERSION: "MTLS_IMAGE=\"registry.mender.io/mendersoftware/mtls-ambassador:saas-v%\""/ignore -->
```bash
export MTLS_IMAGE="registry.mender.io/mendersoftware/mtls-ambassador:saas-v2023.06.20"
export MTLS_MENDER_BACKEND="http://mender-api-gateway"
export SCALABILITY_MAX_REPLICAS=10
export SCALABILITY_AVERAGE_CPU_UTILIZATION=70

cat >mender-mtls-deployment.yml <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: mender-mtls
  name: mender-mtls
spec:
  replicas: 1
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 0
  selector:
    matchLabels:
      run: mender-mtls
  template:
    metadata:
      labels:
        run: mender-mtls
    spec:
      containers:
      - name: mender-mtls
        image: ${MTLS_IMAGE}
        env:
        - name: MTLS_MENDER_BACKEND
          value: ${MTLS_MENDER_BACKEND}
        - name: MTLS_DEBUG_LOG
          value: "true"
        - name: MTLS_TENANT_CA_PEM
          value: "/etc/ssl/certs/ca.crt"
        envFrom:
        - secretRef:
            name: mtls-user
        volumeMounts:
        - name: server-cert
          mountPath: /etc/mtls/certs/server/server.crt
          subPath: "cert.crt"
          readOnly: true
        - name: server-cert
          mountPath: /etc/mtls/certs/server/server.key
          subPath: "private.key"
          readOnly: true
        - name: mtls-ca
          mountPath: /etc/ssl/certs/ca.crt
          subPath: "ca.crt"
          readOnly: true

        resources:
          limits:
            cpu: 200m
            memory: 80M
          requests:
            cpu: 10m
            memory: 30M

        ports:
        - containerPort: 8080

        readinessProbe:
          tcpSocket:
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 10
        livenessProbe:
          tcpSocket:
            port: 8080
          initialDelaySeconds: 15
          periodSeconds: 30
         
      imagePullSecrets:
      - name: registry-mtls-secret
      volumes:
      - name: server-cert
        secret:
          secretName: keycert
      - name: mtls-ca
        secret:
          secretName: mtls-ca
---
# HPA option
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: mender-mtls
spec:
  maxReplicas: ${SCALABILITY_MAX_REPLICAS}
  minReplicas: 1

  metrics:
   - type: Resource
     resource:
       name: cpu
       target:
         type: Utilization
         averageUtilization: ${SCALABILITY_AVERAGE_CPU_UTILIZATION}
 
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: mender-mtls
EOF

kubectl apply -f mender-mtls-deployment.yml
```

## Expose the mTLS service
You can expose the Mender mTLS Ambassador service with a L4 Load balancer. Please
refer to your cloud provider documentation for a complete overview.
Here you can have sample setups, that could be different for your specific use case:

* AWS sample setup:
```bash
cat >mender-mtls-service.yml <<EOF
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout: "600"
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
  labels:
    run: mender-mtls
  name: mender-mtls
spec:
  ports:
  - port: 443
    protocol: TCP
    targetPort: 8080
    name: https
  selector:
    run: mender-mtls
  type: LoadBalancer

EOF

kubectl apply -f mender-mtls-service.yml
```

* Azure sample setup:
```bash
cat >mender-mtls-service.yml <<EOF
apiVersion: v1
kind: Service
metadata:
  labels:
    run: mender-mtls
  name: mender-mtls
spec:
  ports:
  - port: 443
    protocol: TCP
    targetPort: 8080
    name: https
  selector:
    run: mender-mtls
  type: LoadBalancer
EOF

kubectl apply -f mender-mtls-service.yml
```
