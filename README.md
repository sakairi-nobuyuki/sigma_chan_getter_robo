# What is this?

This is a `sigma-chan-getter-robo`.

# Requirements

Perhaps normal or standard local computer cluster environment is required, but I don't know what is normal or standard.

As far as I can say is, you or we might need,

- `mysql-server` and `mysql-client`
- `docker`
- `minikube`
- `argoworkflow`

# Environment construction

This is my memorundom, and not always applicable to your environment.

## Minikube

### Installation

See,

https://minikube.sigs.k8s.io/docs/start/

For Ubuntu environments, just simply run,

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

### Start `minikube`

```
minikube start
```

### Usage

See,

https://minikube.sigs.k8s.io/docs/

## Argoworkflow

You can learn about `argoworkflow` in the following excellent web-page.

https://argoproj.github.io/argo-workflows/quick-start/

### Installation

Just run,

```
kubectl create namespace argo
kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/download/v<<ARGO_WORKFLOWS_VERSION>>/install.yaml
```

### Port-fowarding the UI

The argoworkflow UI could help you. Run,

```
kubectl -n argo port-forward deployment/argo-server 2746:2746
```

and access to https://localhost:2746/ with your web-browser. The UI might require a password.

```
kubectl -n argo exec -it $(kubectl get --no-headers=true pods -n argo -o name -l app=argo-server) -- argo auth token
```

## K8S

https://kubernetes.io/

# How to use

## Start cron-job


## Stop cron-job


## Update the Docker image

```
make build-app
docker push nsakairi/getter-robo
```

## Images

sha256:cbc3f915119c61ad8a78939f4ba92a13ae50c32bc76b8945978c3a6ec88dafd1