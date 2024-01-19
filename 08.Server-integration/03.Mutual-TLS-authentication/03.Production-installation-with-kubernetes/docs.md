---
title: Production installation with Kubernetes
taxonomy:
    category: docs
---



This section shows how to set up the mtls ambassador server with kubernetes.
Before starting this section we suggest you read the [prerequisites](../01.Keys-and-certificates/docs.md) and complete the [evaluation](../02.Evaluation-with-docker-compose/docs.md). 


## Prerequisites

You can use the same steps to generate the keys as defined in the [prerequisites](../01.Keys-and-certificates/docs.md).


## Create required secrets

! Set the [env variables](../01.Keys-and-certificates/docs.md#env-variables) and [generate the keys](../01.Keys-and-certificates/docs.md#generating-the-keys) before executing the commands below.

Create the Kubernetes secret:

```bash
kubectl create secret generic mtls-user --from-literal=MTLS_MENDER_USER=${MENDER_USERNAME} --from-literal=MTLS_MENDER_PASS=${MENDER_PASSWORD}
kubectl create secret generic keycert --from-file=server.crt=./server.crt --from-file=server.key=./server.key
kubectl create secret generic mtls-ca --from-file=ca.crt=./ca.crt
kubectl create secret docker-registry registry-mtls-secret --docker-server=${DOCKER_REGISTRY_URL} --docker-username=${DOCKER_REGISTRY_USERNAME} --docker-password={$DOCKER_REGISTRY_PASSWORD}
```


## mTLS Deployment
* Create the following Kubernetes resource:

```bash
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
          subPath: "server.crt"
          readOnly: true
        - name: server-cert
          mountPath: /etc/mtls/certs/server/server.key
          subPath: "server.key"
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

TODO: For the exact same credentials the docker based commands works but kuberentes gives a
  Warning  Failed     14m (x4 over 16m)   kubelet            Failed to pull image "registry.mender.io/mendersoftware/mtls-ambassador:mender-3.6.3": rpc error: code = Unknown desc = failed to pull and unpack image "registry.mender.io/mendersoftware/mtls-ambassador:mender-3.6.3": failed to resolve reference "registry.mender.io/mendersoftware/mtls-ambassador:mender-3.6.3": unexpected status from HEAD request to https://registry.mender.io/v2/mendersoftware/mtls-ambassador/manifests/mender-3.6.3: 401 Unauthorized

I've checked kubectl get secret registry-mtls-secret -o jsonpath="{.data['\.dockerconfigjson']}" | base64 --decode and the data is the same


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

