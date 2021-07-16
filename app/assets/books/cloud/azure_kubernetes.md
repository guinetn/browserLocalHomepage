# AKS - Azure Kubernetes Service

easy deployment and management of Kubernetes clusters in Azure. Azure handles the monitoring and maintenance of the Kubernetes clusters for you. The Kubernetes master nodes are managed by Azure and leave the management of worker nodes to you. The Kubernetes service itself is free, and you pay only for the worker nodes that run the PODs ( In Kubernetes, a POD is a group of one or more containers). The Azure cluster can be created through the CLI, Resource Manager templates/Terraform or through Azure Portal.

Azure Kubernetes Service is suitable to run production container workloads which demand the full orchestration capabilities like scheduling, failover, service discovery, scaling, health monitoring, advanced networking/routing, security, and easy application upgrades. Azure Kubernetes service supports both Linux and Windows containers.

To learn more, next you’ll create a Kubernetes cluster and deploy the same docker image built earlier (which was deployed to Azure Container Instances) to the AKS cluster. This example uses Azure CLI to create the cluster and deploy the application.

Create an Azure Kubernetes Cluster with 3 Nodes
>az aks create --resource-group mycontainerrg --name myakscluster01 --node-count 3 --generate-ssh-keys --enable-addons http_application_routing
>az extension add --name aks-preview
>az extension list                          list the extensions 

Configure the kubectl on your cloud-shell
>az aks get-credentials --resource-group mycontainerrg --name myakscluster01
Create a new namespace for the application to deploy, logically group the cluster resources in Kubernetes
>kubectl create namespace mynginxapp
 set this namespace in the kubectl config level so that all the future kubectl commands will execute under this namespace
>kubectl config set-context –-namespace=mynginxapp
use the kubectl commands to interact and manage the Kubernetes cluster
>kubectl get nodes

stop/start the Worker nodes in the AKS cluster
>az vmss list 
>az vmss stop --resource-group MC_MYCONTAINERRG_MYAKSCLUSTER01_WESTUS --name aks-nodepool1-35851458-vmss
>az vmss start --resource-group MC_MYCONTAINERRG_MYAKSCLUSTER01_WESTUS --name aks-nodepool1-35851458-vmss

deploy the application to Kubernetes cluster
1. yaml deployment file
2. apply that yaml to the Kubernetes cluster using kubectl command

```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
 name: mynginx-deployment
spec:
 selector:
   matchLabels:
     app: mynginxapp01
 replicas: 2
 template:
   metadata:
     labels:
       app: mynginxapp01
   spec:
      containers:
      # If you need to deploy multiple containers on the same POD, you can add the container configs below. This POD contains one container.  
        - name: mycluster01
          image: dockdemorepo/myacirepo:nginx-helloworld 
          ports:
          - containerPort: 80
          resources:
            requests:
             cpu: 1
             memory: 250Mi
            limits:
             cpu: 1
             memory: 250Mi
          livenessProbe:
            httpGet:
               path: /myhtml.html
               port: 80
            initialDelaySeconds: 10
            periodSeconds: 5
          readinessProbe:
            httpGet:
               path: /myhtml.html
               port: 80
            initialDelaySeconds: 10
            periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: my-external-lb
spec:
 ports:
  - port: 80
    protocol: TCP
    targetPort: 80
 selector:
   app: mynginxapp01
 type: ClusterIP
---
apiVersion: extensions/v1beta1
kind: Ingress                               Create the Ingress Service to enable the external access to the application
metadata:
  name: mynginxapp01
  annotations:
     kubernetes.io/ingress.class: addon-http-application-routing
spec:
  rules:
  - host: mynginxapp01.c2dc921a42db48bcbab4.westus.aksapp.io
    http:
      paths:
      - backend:
          serviceName: my-external-lb
          servicePort: 80
        path: /
```

create the Kubernetes resources
>kubectl apply -f mynginxapp01.yaml
    Deploys 3 PODs
    Creates the ClusterIP service to route the traffic from Ingress Controller to the PODs.
    Ingress Controller Service.
get the details of these resources 
>kubectl get pods -o wide
>kubectl get services
>kubectl get ingress