---
title: Quick Start
taxonomy:
    category: docs
    label: tutorial
---

!!! In this section, we provide a quick start to get the Mender Server running
!!! in a Kubernetes cluster. This is meant for testing and development purposes.
!!! Please refer to the next session for detailed explanation of production deployment.

### Mender as a k8s deployment

 The following commands describe the fastest route to get the Mender Server running
under a configured kubernetes cluster. In the following we assume that the `kubectl`
and the environment is configured to reach the target cluster. In particular you can
use k3s for the quick start:
```bash
curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

 What follows will result in mongodb and seaweedfs running in your cluster together
with the Mender Backend. We also assume you have a Let's Encrypt certificate
for your domain. In the first lines we set all the required variables,
and then start all the required services and configure the cluster.
Finally we install the Mender Helm Chart.

```bash
export MENDER_SERVER_DOMAIN="your.demo.mender.io"

export MENDER_REGISTRY_EMAIL="your@email.com"
export MENDER_REGISTRY_PASSWORD="your_password"
export MENDER_REGISTRY_USERNAME="your_user"

# you do not have to change anything below this line

export MENDER_SERVER_URL="https://${MENDER_SERVER_DOMAIN}"
helm repo add seaweedfs https://seaweedfs.github.io/seaweedfs/helm
helm repo update
helm install seaweedfs --wait -f seaweedfs.yml  seaweedfs/seaweedfs

export STORAGE_ENDPOINT="http://seaweedfs-s3:8333"
export AWS_REGION="us-east-1"
export AWS_SECRET_ACCESS_KEY=$(kubectl  get secret seaweedfs-s3-secret -o jsonpath='{.data.admin_secret_access_key}' |base64 -d)
export AWS_ACCESS_KEY_ID=$(kubectl get secret seaweedfs-s3-secret -o jsonpath='{.data.admin_access_key_id}' |base64 -d)
export STORAGE_BUCKET="mender-artifacts"
export STORAGE_CLASS="default"

kubectl create secret tls mender-ingress-tls --key /etc/letsencrypt/live/${MENDER_SERVER_DOMAIN}/privkey.pem --cert /etc/letsencrypt/live/${MENDER_SERVER_DOMAIN}/fullchain.pem

helm install local-mongo bitnami/mongodb --namespace mongodb --create-namespace
kubectl delete secret mender-mongo
kubectl create secret generic mender-mongo --from-literal=MONGO="mongodb://root:`kubectl get secret --namespace mongodb local-mongo-mongodb -o jsonpath="{.data.mongodb-root-password}" | base64 -d`@local-mongo-mongodb.mongodb.svc/mender?authSource=admin" --from-literal=MONGO_URL="mongodb://root:`kubectl get secret --namespace mongodb local-mongo-mongodb -o jsonpath="{.data.mongodb-root-password}" | base64 -d`@local-mongo-mongodb.mongodb.svc/mender?authSource=admin"

cat <<-EOF > mender-values.yml
ingress:
  enabled: true
  annotations:
    cert-manager.io/issuer: "letsencrypt"
  ingressClassName: traefik
  path: /
  hosts:
    - ${MENDER_SERVER_DOMAIN}
  tls:
    - secretName: mender-ingress-tls
      hosts:
        - ${MENDER_SERVER_DOMAIN}
EOF

helm repo add mender https://charts.mender.io
helm repo update
kubectl create secret docker-registry my-mender-pull-secret \
  --docker-username=${MENDER_REGISTRY_USERNAME} \
  --docker-password=${MENDER_REGISTRY_PASSWORD} \
  --docker-email=${MENDER_REGISTRY_EMAIL} \
  --docker-server=registry.mender.io
cat <<-EOF >> mender-values.yml
default:
  imagePullSecrets:
    - name: my-mender-pull-secret
EOF

cat <<-EOF >> mender-values.yml
global:
  enterprise: true
  mongodb:
    existingSecret: mender-mongo
  s3:
    AWS_URI: "${STORAGE_ENDPOINT}"
    AWS_BUCKET: "${STORAGE_BUCKET}"
    AWS_REGION: "${AWS_REGION}"
    AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
    AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
  url: "${MENDER_SERVER_URL}"

# Disable the MongoDB subchart:
mongodb:
  enabled: false

# Enable Redis
redis:
  enabled: true

api_gateway:
  storage_proxy:
    enabled: true
    url: "${STORAGE_ENDPOINT}"
    customRule: "PathRegexp(\`^/${STORAGE_BUCKET}\`)"
EOF

helm upgrade --install mender mender/mender --wait -f mender-values.yml
```

After the following completes and all the pods are healthy you can access your new Mender installation
with the `https://${MENDER_SERVER_DOMAIN}` where `${MENDER_SERVER_DOMAIN}` stands for the domain of your choice.

#### Open source evaluation

Note that in case you are evaluating the open source variant you do not need docker secret,
and have to replace the above step where you configure the `global:` section, with:
```bash
cat <<-EOF >> mender-values.yml
global:
  mongodb:
    existingSecret: mender-mongo
  s3:
    AWS_URI: "${STORAGE_ENDPOINT}"
    AWS_BUCKET: "${STORAGE_BUCKET}"
    AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
    AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
  url: "${MENDER_SERVER_URL}"

mongodb:
  enabled: false

api_gateway:
  storage_proxy:
    enabled: true
    url: "${STORAGE_ENDPOINT}"
    customRule: "PathRegexp(\`^/${STORAGE_BUCKET}\`)"
EOF
```
