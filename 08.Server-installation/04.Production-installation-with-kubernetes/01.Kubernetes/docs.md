---
title: Kubernetes
taxonomy:
    category: docs
    label: tutorial
---

!!! In this section, we guide you by installing a Kubernetes cluster using k3s for
!!! evaluation purposes. Please don't consider installing the Kubernetes cluster
!!! described here as a complete, production-grade setup. The installation of the
!!! cluster and the related infrastructure is the responsibility of the user.

### Installation of Kubernetes

If you don't have a ready-to-use Kubernetes cluster you can install [K3S](https://k3s.io/),
a lightweight certified Kubernetes distribution.

For example, on a machine with Ubuntu 22.04 (e.g. an instance from AWS EC2 or DigitalOcean),
you can install Kubernetes running:

```bash
curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

! Read and confirm shell script content before piping from curl to the shell.<br>
! Never run scripts from the internet before knowing what they do.

After a few seconds, your Kubernetes cluster will be ready:

```bash
kubectl get nodes
```

<!--AUTOVERSION: "control-plane,%"/ignore -->
> ```
> NAME     STATUS   ROLES                  AGE   VERSION
> host     Ready    control-plane,master   2m    v...
> ```

### Installation of Helm

Helm is the package manager for Kubernetes. Please refer to the
[Helm official documentation](https://helm.sh/docs/intro/install/) to install the Helm CLI
on your system.

To install the latest version of the Helm package manager, run:

<!--AUTOVERSION: "https://raw.githubusercontent.com/helm/helm/%/scripts/get-helm-3"/ignore -->
```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
```

! Read and confirm shell script content before piping from curl to the shell.<br>
! Never run scripts from the internet before knowing what they do.

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
