---
title: Kubernetes
taxonomy:
    category: docs
    label: tutorial
---

!!! The installation and maintenance of the Kubernetes cluster and the related
!!! infrastructure is the responsibility of the user.

### Kubernetes cluster

You need a running Kubernetes cluster on one of the platforms listed in the
[Requirements section](../docs.md#platform-and-software-dependencies).
Please refer to your provider's documentation to create the cluster and to
configure `kubectl` to access it.

The following snippets are minimal examples that create a cluster with three
nodes of 4 vCPUs and 16 GB RAM each. Adapt the node count and size to the
[Hardware requirements](../docs.md#hardware-requirements), and review
networking, access control and backups before using the cluster in production.

[ui-tabs position="top-left" active="0" theme="default" ]
[ui-tab title="Azure AKS"]
Requirements: the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli),
logged in with `az login`.

The snippet also enables the
[Application Gateway Ingress Controller](https://learn.microsoft.com/en-us/azure/application-gateway/tutorial-ingress-controller-add-on-new)
add-on, used by the Azure AKS Ingress example in the
[Mender Server](../03.Mender-server/docs.md#ingress-controller) section.

```bash
export AZ_RESOURCE_GROUP="mender"
export AZ_LOCATION="westeurope"
export CLUSTER_NAME="mender"

az group create --name ${AZ_RESOURCE_GROUP} --location ${AZ_LOCATION}
az aks create \
  --resource-group ${AZ_RESOURCE_GROUP} \
  --name ${CLUSTER_NAME} \
  --node-count 3 \
  --node-vm-size Standard_D4s_v5 \
  --network-plugin azure \
  --enable-addons ingress-appgw \
  --appgw-name ${CLUSTER_NAME}-appgw \
  --appgw-subnet-cidr "10.225.0.0/16" \
  --ssh-access disabled
az aks get-credentials --resource-group ${AZ_RESOURCE_GROUP} --name ${CLUSTER_NAME}

# Azure Disk StorageClass, created by AKS
export STORAGE_CLASS="default"
```
[/ui-tab]
[ui-tab title="AWS EKS"]
Requirements: the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
with valid credentials, and [eksctl](https://eksctl.io/installation/).

```bash
export AWS_REGION="eu-central-1"
export CLUSTER_NAME="mender"

eksctl create cluster \
  --name ${CLUSTER_NAME} \
  --region ${AWS_REGION} \
  --nodes 3 \
  --node-type m6i.xlarge \
  --with-oidc
```

`eksctl` updates your kubeconfig automatically.

A new EKS cluster has no driver for persistent volumes. Install the
[Amazon EBS CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html)
add-on and create a `gp3` StorageClass, set as the default one of the cluster:

```bash
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

eksctl create iamserviceaccount \
  --name ebs-csi-controller-sa \
  --namespace kube-system \
  --cluster ${CLUSTER_NAME} \
  --region ${AWS_REGION} \
  --role-name ${CLUSTER_NAME}-ebs-csi-driver \
  --role-only \
  --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
  --approve
eksctl create addon \
  --name aws-ebs-csi-driver \
  --cluster ${CLUSTER_NAME} \
  --region ${AWS_REGION} \
  --service-account-role-arn arn:aws:iam::${AWS_ACCOUNT_ID}:role/${CLUSTER_NAME}-ebs-csi-driver

kubectl apply -f - <<EOF
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: gp3
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
  encrypted: "true"
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
EOF

export STORAGE_CLASS="gp3"
```

!!! A new EKS cluster has no Ingress controller. Install the
!!! [AWS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html),
!!! used by the AWS EKS Ingress example in the
!!! [Mender Server](../03.Mender-server/docs.md#ingress-controller) section.
[/ui-tab]
[ui-tab title="Google GKE"]
Requirements: the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
with the `gke-gcloud-auth-plugin` component, logged in with `gcloud auth login`.

!! GKE Autopilot is not supported. Use a GKE Standard cluster.

```bash
export GCP_PROJECT="replace-with-your-project-id"
export GCP_REGION="europe-west1"
export CLUSTER_NAME="mender"

# Regional cluster: --num-nodes is per zone, this creates one node in each of the 3 zones
gcloud container clusters create ${CLUSTER_NAME} \
  --project ${GCP_PROJECT} \
  --location ${GCP_REGION} \
  --num-nodes 1 \
  --machine-type e2-standard-4
gcloud container clusters get-credentials ${CLUSTER_NAME} \
  --project ${GCP_PROJECT} \
  --location ${GCP_REGION}

# Persistent Disk StorageClass, created by GKE
export STORAGE_CLASS="standard-rwo"
```
[/ui-tab]
[/ui-tabs]

To verify that `kubectl` can reach the cluster, run:

```bash
kubectl get nodes
```

All the nodes must be in the `Ready` status.

### Installation of Helm

Helm is the package manager for Kubernetes. Please refer to the
[Helm official documentation](https://helm.sh/docs/intro/install/) to install the Helm CLI
on your system.

! Read and confirm shell script content before piping from curl to the shell.<br>
! Never run scripts from the internet before knowing what they do.

To install the latest version of the Helm package manager, run:

<!--AUTOVERSION: "https://raw.githubusercontent.com/helm/helm/%/scripts/get-helm-3"/ignore -->
```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
```

To verify `helm` is correctly installed, you can list the installed applications running:

```bash
helm version
```

To list the applications installed, run:

```bash
helm list
```

> ```
> NAME	NAMESPACE	REVISION	UPDATED	STATUS	CHART	APP VERSION
> ```

### Installation of cert-manager (optional)

[cert-manager](https://cert-manager.io) automates certificate management in cloud native environments.
It builds on top of Kubernetes to provide X.509 certificate management, including integration with Let's Encrypt.

To install cert-manager on the Kubernetes cluster using the Helm chart, run:

<!--AUTOVERSION: "--version v%"/ignore -->
```bash
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.16.1 \
  --set crds.enabled=true
```

Create the Let's Encrypt issuer:

```bash
export LETSENCRYPT_SERVER_URL="https://acme-v02.api.letsencrypt.org/directory"
export LETSENCRYPT_EMAIL="your-email@example.com"

cat >issuer-letsencrypt.yml <<EOF
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: letsencrypt
spec:
  acme:
    server: ${LETSENCRYPT_SERVER_URL}
    email: ${LETSENCRYPT_EMAIL}
    privateKeySecretRef:
      name: letsencrypt
    solvers:
    - http01:
        ingress: {}
EOF

kubectl apply -f issuer-letsencrypt.yml
```
