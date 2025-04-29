1. Start the minikube cluster:
```
minikube start --cpus 4 --memory 8g
```

2. Install ArgoCD on the cluster:
```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

3. Check if all pods are running:
```
kubectl get pods -n argocd
```

4. Configure port for ArgoCD:
```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

5. Get the ArgoCD password:
```
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d && echo
```

6. Install Argo Rollouts:
```
kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://raw.githubusercontent.com/argoproj/argo-rollouts/stable/manifests/install.yaml
```

7. Check if it's running:
```
kubectl get pods -n argo-rollouts
```

8. Apply ArgoCD Application:
```
kubectl apply -f argocd-app.yaml -n argocd
```
After the deployment ArgoCD will check GIT and deploy our application.

9. Install Argo Rollour CLI:
```
curl -LO https://github.com/argoproj/argo-rollouts/releases/latest/download/kubectl-argo-rollouts-linux-amd64
chmod +x kubectl-argo-rollouts-linux-amd64
sudo mv kubectl-argo-rollouts-linux-amd64 /usr/local/bin/kubectl-argo-rollouts
```

10. Run Argo Rollouts Dashboard. (it's running on the port 3100)
```
kubectl argo rollouts dashboard
```