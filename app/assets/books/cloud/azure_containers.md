# AZURE CONTAINERS

- [Azure for Python Developers](https://docs.microsoft.com/en-us/azure/developer/python/)
- https://www.red-gate.com/simple-talk/devops/containers-and-virtualization/running-container-workloads-in-microsoft-azure/

Microsoft Azure Container services
- ACR - Azure Container Registry
- ACI - Azure Container Instances
- AKS - Azure Kubernetes Service
- ARM - Azure Resource Manager 
- Azure Batch
- Azure Service Fabric
- Azure Functions
- Azure App Service


## Containerize Your Application With Docker

Docker CLI or Visual Studio 

Right-click the project in Solution Explorer, and add DockerFile
- DOCKERFILE file
- launchSettings.json     
    "Docker": {        
        "commandName" : "Docker", 
        "launchBrowser": true,         
        "launchUrl":  "httos://localhost:5001", 
        "publishAllPorts": true, 
        "useSSL": true, 
        "sslPort": 5001
    } 
- Deploy
    Right-click the project in Solution Explorer, and select “Publish…“
    Azure Container Registry
    ...Publish 
    >The resource group containing the newly created resources
    >The Azure Container Registry
    >The Docker image
    >An app service plan
    >The application instance itself, up and running
    https://localhost/5001


## ACR - Azure Container Registry

Private registry storing docker images (Windows/Linux) which gets deployed to your environment. 
Based on the open-source Docker Registry 2.0
The Docker images can be pushed to the Container Registry as part of the development workflow (CICD Pipeline)
Docker Hub can be an alternative as container repository
It is secure, and the access can be controlled by service principal and role-based access control (RBAC)

CI workflow:  
Developper → Github → Jenkins (built image) → ACR  

## ACI - Azure Container Instances

To run isolated containers for use cases like simple applications, task automation and build jobs. 
Full container orchestration is not possible with Azure Container Instances. 
However, creating a multi-container group is still possible. 
That means your main application container can be combined with other supporting containers like logging or monitoring containers. 
This is achieved by sharing the host machine, local network, and storage.

Use images either from 
- Docker Hub (not full link)
- Azure container registry (full link FQDN: mycontrreg01.azurecr.io/mynginximage/nginx:v1)

CREATE AND RUN A CONTAINER INSTANCE
>az group create --name mycontainerrg --location westus
>az container create --resource-group mycontainerrg --name mynginxv1 --image dockdemorepo/myacirepo:nginx-helloworld --ports 80 --dns-name-label mynginxv1 --location westus
The value for –dns-name-label should be unique. If the name you are trying is taken by someone else in the same location (westus), it will error out. 

Start and stop containers
>az container stop --name mynginxv1 --resource-group mycontainerrg
>az container start --name mynginxv1 --resource-group mycontainerrg

View container-related logs:
>az container logs --name mynginxv1 --resource-group mycontainerrg

Execute shell commands inside the container
>az container exec --exec-command /bin/bash --container-name mynginxv1 --resource-group mycontainerrg --name mynginxv1

Access web page served by the NGINX by using the FQDN provided in the container creation output.


## ARM - Azure Resource Manager

ARM template: JSON file declarative syntax defining the infrastructure and configuration for your Azure resources. 

## Container Group

Allow to run multiple containers on the same host machine. All the containers in the container group share the resources, network, and storage volumes
Azure supports two methods of container groups.
METHOD 1
Create multiple containers in the container group, those containers can connect to each other using the localhost and the ports each container listens. One container port can be exposed to the internet through public IP address and DNS name. However, this does not serve the purpose of multi-service architectures: cannot deploy mass production workloads with hundreds of services connecting each other. 
METHOD 2
Create multiple containers on the Azure virtual network but only for Linux containers 
These containers cannot be accessed through the internet. They neither allow assigning a public IP address nor placing the load balancers in front of the containers (It is a limitation from load balancers)
Global virtual network peering is not possible, which limits the container access to only within the virtual network.

Container groups can be created using
- Azure Resource Manager Template
- Yaml file, ex, exports the configuration of the container instance (mynginxv1):
>az container export --output yaml --name mynginxv1 --resource-group mycontainerrg --file mynginxv1.yaml
>az container delete --name mynginxv1 --resource-group mycontainerrg
Create the container group
>az container create --resource-group mycontainerrg --file mynginxv1.yaml

mynginxv1.yml
```yaml
additional_properties: {}
apiVersion: '2018-10-01'
identity: null
location: westus
name: mynginxv1
properties:
  containers:
  - name: mynginxv1
    properties:
      environmentVariables: []
      image: dockdemorepo/myacirepo:nginx-acg
      ports:
      # Port 80 is NGINX container’s port. Port 8081 is springboot App’s Port. 
      - port: 80
      - port: 8081
      resources:
        requests:
          cpu: 1.0
          memoryInGB: 1.5
  - name: myspringbootappv1
    properties:
      environmentVariables: []
      image: dockdemorepo/myacirepo:myappv1
      resources:
        requests:
          cpu: 1.0
          memoryInGB: 1.5
  ipAddress:
    dnsNameLabel: mynginxv1
    #fqdn: mynginxv1.westus.azurecontainer.io
    #ip: 40.81.4.187
    ports:
    - port: 80
      protocol: TCP
    type: Public
  osType: Linux
  restartPolicy: Always
tags: {}
type: Microsoft.ContainerInstance/containerGroups
```
