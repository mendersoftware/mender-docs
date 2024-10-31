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

! Set the [env variables](../01.Keys-and-certificates/docs.md#environment-variables) and [generate the keys](../01.Keys-and-certificates/docs.md#generating-the-keys) before executing the commands below.

Create the Kubernetes secret:

```bash
kubectl create secret generic mtls-user --from-literal=MTLS_MENDER_USERNAME=${MENDER_USERNAME} --from-literal=MTLS_MENDER_PASSWORD=${MENDER_PASSWORD}
kubectl create secret generic keycert --from-file=server.crt=./server.crt --from-file=server.key=./server.key
kubectl create secret generic mtls-ca --from-file=ca.crt=./ca.crt
kubectl create secret docker-registry registry-mender-io-mtls --docker-server=${DOCKER_REGISTRY_URL} --docker-username=${DOCKER_REGISTRY_USERNAME} --docker-password=${DOCKER_REGISTRY_PASSWORD}
```


## Mender Gateway Deployment
* Create the following Kubernetes resource:

```bash
export SCALABILITY_MAX_REPLICAS=10
export SCALABILITY_AVERAGE_CPU_UTILIZATION=70

cat >mender-gateway-deployment.yml <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: mender-mtls-gateway
  name: mender-mtls-gateway
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 0
  selector:
    matchLabels:
      run: mender-mtls-gateway
  template:
    metadata:
      labels:
        run: mender-mtls-gateway
    spec:
      containers:
      - name: mender-mtls-gateway
        image: ${MENDER_GATEWAY_IMAGE}
        env:
        - name: MTLS_ENABLED
          value: "true"
        - name: HTTP_ENABLED
          value: "true"
        - name: HTTP_LISTEN
          value: ":8080"
        - name: HTTPS_ENABLED
          value: "true"
        - name: HTTPS_LISTEN
          value: ":8443"
        - name: HTTPS_SERVER_CERTIFICATE
          value: "/etc/mender/certs/server.crt"
        - name: HTTPS_SERVER_KEY
          value: "/etc/mender/certs/server.key"
        - name: MTLS_CA_CERTIFICATE
          value: "/etc/ssl/certs/ca.crt"
        - name: UPSTREAM_SERVER_URL
          value: "${UPSTREAM_SERVER_URL}"
        - name: HTTPS_MINIMUM_TLS_VERSION
          value: "1.2"
        envFrom:
        - secretRef:
            name: mtls-user
        volumeMounts:
        - name: server-cert
          mountPath: /etc/mender/certs/server.crt
          subPath: "server.crt"
          readOnly: true
        - name: server-cert
          mountPath: /etc/mender/certs/server.key
          subPath: "server.key"
          readOnly: true
        - name: mtls-ca
          mountPath: /etc/ssl/certs/ca.crt
          subPath: "ca.crt"
          readOnly: true
        resources:
          limits:
            cpu: 200m
            memory: 128Mi
          requests:
            cpu: 100m
            memory: 32Mi
        ports:
        - containerPort: 8443
          name: https
          protocol: TCP
        - containerPort: 8080
          name: http
          protocol: TCP

        readinessProbe:
          httpGet:
            path: /api/internal/v1/gateway/alive
            port: 8080
          periodSeconds: 15
        livenessProbe:
          httpGet:
            path: /api/internal/v1/gateway/alive
            port: 8080
          periodSeconds: 5
        startupProbe:
          httpGet:
            path: /api/internal/v1/gateway/alive
            port: 8080
          failureThreshold: 36
          periodSeconds: 5

      imagePullSecrets:
      - name: registry-mender-io-mtls
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
  name: mender-mtls-gateway
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
    name: mender-mtls-gateway
EOF

kubectl apply -f mender-gateway-deployment.yml
```


## Expose the mTLS service
You can expose the Mender Gateway service with a L4 Load balancer.
Please refer to your cloud provider documentation for a complete overview.
Here you can have sample setups, that could be different for your specific use case:

* AWS sample setup:

```bash
cat >mender-gateway-service.yml <<EOF
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout: "600"
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
  labels:
    run: mender-mtls-gateway
  name: mender-mtls-gateway
spec:
  ports:
  - port: 443
    protocol: TCP
    targetPort: 8080
    name: https
  selector:
    run: mender-mtls-gateway
  type: LoadBalancer

EOF

kubectl apply -f mender-gateway-service.yml
```

* Azure sample setup:

```bash
cat >mender-gateway-service.yml <<EOF
apiVersion: v1
kind: Service
metadata:
  labels:
    run: mender-mtls-gateway
  name: mender-mtls-gateway
spec:
  ports:
  - port: 443
    protocol: TCP
    targetPort: 8080
    name: https
  selector:
    run: mender-mtls-gateway
  type: LoadBalancer
EOF

kubectl apply -f mender-gateway-service.yml
```
