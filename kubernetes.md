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
#### Install kubectl

```
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/darwin/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```
or 

```
brew install kubernetes-cli 
```
#### Starting mini kube

```
minikube start
```

#### For minikube  dash board
http://192.168.99.100:30000/#!/deploy?namespace=default
```
minikube dashboard        
```

#### Push the branch on docker (Refer to the dockument on dockerizing the application)

http://192.168.99.100:30000/#!/deploy?namespace=default


Create this deployment on the cluster using kubectl:

kubectl create -f deployment.yml 

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: demo-service-deployment
  labels:
    app: demo-service
spec:
  replicas: 2
  selector:
    matchLabels:
      app: demo-service
  template:
    metadata:
      labels:
        app: demo-service
    spec:
      containers:
      - name: demo-service
        image: sbrosinski/demo-service
        ports:
        - containerPort: 8090
```


####Service yml

```
kind: Service
apiVersion: v1
metadata:
  name: demo-service
spec:
  selector:
    app: demo-service
    tier: backend
  ports:
  - protocol: TCP
    port: 8090
    targetPort: 8090
  type: NodePort
```


apiVersion: v1
kind: Service
metadata:
name: 
spec:
ports:
    - port: 8090
    targetPort: 8090
selector:
    app: demo-service
type: NodePort

------------------------------------------------------------------------------------------------------------

###Refernecs:
https://kubernetes.io/docs/tasks/tools/install-kubectl/

https://github.com/kubernetes/minikube/releases

https://www.brosinski.com/post/deploying-spring-boot-app-kubernetes/
https://github.com/sbrosinski/spring-boot-on-k8s
https://brosinski.com/post/kubernetes-on-aws-with-kops/

For rollbacks & deployment yml
file:

https://kubernetes.io/docs/concepts/workloads/controllers/deployment/


Service yml

https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/

https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport

Cheeatsheet

https://kubernetes.io/docs/reference/kubectl/cheatsheet/
