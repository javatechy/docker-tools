# Kubernetes
This project aimed to setup tools on MAC

#### install virtual box on MAC
```
brew cask install virtualbox
```
#### Install minikube
```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.25.0/minikube-darwin-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```
#### Remove container

```
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/darwin/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```

#### Starting mini kube

```
minikube start
```

#### For minikube  dash board
```
minikube dashboard        
```


Refernecs:
https://kubernetes.io/docs/tasks/tools/install-kubectl/

https://github.com/kubernetes/minikube/releases

https://www.brosinski.com/post/deploying-spring-boot-app-kubernetes/
https://github.com/sbrosinski/spring-boot-on-k8s
https://brosinski.com/post/kubernetes-on-aws-with-kops/
