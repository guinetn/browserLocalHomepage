# CLOUD

https://www.cncf.io/

Pool of configurable shared resources (vm, network, storage, applications, services) that can be quickly created with a minimal interaction with the cloud provider

digital infrastructure: computing, storage, data management + cloud services (business enterprise systems )

Leading cloud vendors: Amazon AWS, Microsoft Azure, Google Cloud

![what-is-the-cloud](assets/books/cloud/assets/what-is-the-cloud.png)

- Scalable (unlimited capacity of processing/storage)
- Reliabe (from everywhere, redondant)
- Efficient (free up resources for innovation/development)

Systems (most distributed systems), with the hardware procurement and maintenance and many other things abstracted away from software developers.
Evolution: bare metal → virtualized → containerized → cloud → serverless

Cloud services are popular because they reduce the cost and complexity of owning and operating infrastructure, computers and networks. And some cloud providers offers advanced services that a single company might not be able to afford or develop.

• Characteristics
- service on demand
- access to resources by the network
- Shared resources
- resources flexibility
- Realtime service consumption measure

• Key concept: Virtualisation
    The key enabler of the Cloud so that the resources can be split and re-packaged to sell: 
    virtual machine(hypervisor)
    virtualized (software-defined) storage and network

    Hyper-converged infrastructure (HCI): 
        software-defined infrastructure
        virtualizes all of the elements of conventional "hardware-defined" systems.
• Datacenter software-defined (SDDC)
• Architecture orientée service (SOA)
• Services Cloud
    Cloud offers dozens of services but there are 3 key categories:
    - COMPUTE: VM, containers, serverless functions…
    - STORAGE: databases, datawarehouses, object stores…
    - NETWORKING: DNS, VPC, load balancing…
• Cloud models
    IaaS (Infrastructure as a Service) : hardware infrastructure location
    PaaS (Platform as a Service): hardware infrastructure + applications location
    SaaS (Software as a Service) : service Cloud all inclusive
    DaaS (Desktop as a Service - bureau virtuel): Toute infrastructure du client est hébergée. Chaque utilisateur peut accéder à son bureau depuis n’importe quel terminal PC, Mac, tablette, smartphone, connecté à internet.

    ![saas-paas-iaas](assets/books/cloud/assets/saas-paas-iaas-diagram.svg)

download.page(cloud/cloud_models_deployment_ways.md)
::::
![cloud-devops-modele-deploiement](assets/books/cloud/assets/cloud-devops-modele-deploiement.webp)
::::
download.page(cloud/cloud_models.md)
::::
download.page(cloud/free_tiers.md)
::::
download.page(cloud/cloud_design_patterns.md)
::::
## The Stack
* Servers (including bare metal, VMs, containers, serverless functions to run the applications and backends: AWS EC2 or GCP GCE
* Databases to store data and make them readily available for appliations, and indexes to speed up searches and filters.
* Caches to speed up reads by remembering results of expensive operations
* Data Warehouse to store historical data for analytics
* Storage to store files and objects (can also be used to serve static websites)
* Message queues to communicate between processes and enable async operations.
* Logging: AWS Kinesis, Fluentd, GCP Cloud Logging
* Monitoring to monitor system health and key business metrics, and send out alerts: GCP Cloud Monitoring, Datadog
* Service Discovery, Configs and Secrets: Consul/Vault
* Orchestration / Provision: Kubernetes, Terraform
* Package format: a common way to package all the applications, e.g. Docker
* Code management: git or hg
* CI/CD: continuous integration and deployment
::::
download.page(cloud/edge_computing.md)
::::
## CLOUD ROLES

- System administrator
Manage cloud plateforms: operational condition, issues/support L1-L3
- Development Engineer
develop software solutions, new functionalities
- Cloud architect
Design architectures, app deployment plan on cloud environnemnts
- QA engineer
Define functionnal tests strategy and tests automation
- DevOps
Define integration systems automation and continuous deployement. Guide development teams and daily collaborate with operations for a better quality service

::::
download.page(cloud/infrastructure_as_code.md)
::::
download.page(cloud/cloud_automation.md)
::::
download.page(cloud/cloud_orchestration.md)
::::
download.page(cloud/cloud_monitoring.md)
::::
download.page(cloud/containers.md)
::::
download.page(cloud/vm.md)
::::
download.page(cloud/containers_docker.md)
::::
download.page(cloud/containers_kubernetes.md)
::::
download.page(cloud/containers_vagrant.md)
::::
download.page(cloud/aws.md)
::::
download.page(cloud/azure.md)
::::
download.page(cloud/google_cloud.md)
::::
download.page(cloud/vps.md)
::::

