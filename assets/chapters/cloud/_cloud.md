# CLOUD

Pool of configurable shared resources (vm, network, storage, applications, services) that can be quickly created with a minimal interaction with the cloud provider

digital infrastructure: computing, storage, data management + cloud services (business enterprise systems )

Leading cloud vendors: Amazon AWS, Microsoft Azure, Google Cloud

![what-is-the-cloud](assets/slides/cloud/assets/what-is-the-cloud.png)

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

    ![saas-paas-iaas](assets/slides/cloud/assets/saas-paas-iaas-diagram.svg)

• Cloud Deployment Types    
  
    PUBLIC: your infrastructure is running by...
        - Amazon AWS
        - Microsoft Azure
        - Google Cloud Platform
        - Alibaba Cloud (China) 
        - Oracle
        - IBM

        Relying on massive data centers supplying the desired cloud capacity on demand.
        
        [GCP vs AWS](https://cloud.google.com/docs/compare/aws#service_comparisons)
        [GCP vs Azure](https://cloud.google.com/docs/compare/azure#service_comparisons)
    
    PRIVATE: you own your data center but resource request and allocation is done through software UI
    
    HYBRID: taking the best parts of public and private cloud (+on premises).  Easier to share data and information amongst partners that follow different application and data standards and architectures.

    MULTICLOUD: use several public clouds
    Businesses have started to move into multi-cloud hybrid environments. This ensure better interoperability of their digital assets with their larger network of partner/vendor systems that may be hosted on different cloud environments.
    
    EDGE COMPUTING: Puts storage and servers where the data is

::::
![cloud-devops-modele-deploiement](assets/slides/cloud/assets/cloud-devops-modele-deploiement.webp)
::::
download.md(assets/slides/cloud/cloud_models.md)
::::
download.md(assets/slides/cloud/cloud_design_patterns.md)
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
download.md(assets/slides/cloud/edge_computing.md)
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
download.md(assets/slides/cloud/infrastructure_as_code.md)
::::
download.md(assets/slides/cloud/cloud_automation.md)
::::
download.md(assets/slides/cloud/cloud_orchestration.md)
::::
download.md(assets/slides/cloud/cloud_monitoring.md)
::::
download.md(assets/slides/cloud/containers.md)
::::
download.md(assets/slides/cloud/vm.md)
::::
download.md(assets/slides/cloud/containers_docker.md)
::::
download.md(assets/slides/cloud/containers_kubernetes.md)
::::
download.md(assets/slides/cloud/containers_vagrant.md)
::::
download.md(assets/slides/cloud/aws.md)
::::
download.md(assets/slides/cloud/azure.md)
::::
download.md(assets/slides/cloud/google_cloud.md)
::::
download.md(assets/slides/cloud/vps.md)
::::

