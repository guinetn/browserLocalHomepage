# KUBERNETES (K8s) 

https://kubernetes.io/

to add:
https://www.c-sharpcorner.com/article/build-cicd-pipeline-for-azure-kubernetes/ ***
https://developers.redhat.com/blog/2020/05/11/top-10-must-know-kubernetes-design-patterns/
https://andrewlock.net/running-kubernetes-and-the-dashboard-with-docker-desktop

Course 70+videos
https://www.youtube.com/playlist?list=PLn6POgpklwWqfzaosSgX2XEKpse5VY2v5
https://www.youtube.com/watch?v=37VLg7mlHu8&list=PLn6POgpklwWqfzaosSgX2XEKpse5VY2v5&index=1

2015 Google 
orchestrateur. C'est à dire qu'il ne fait que gérer des conteneurs, leurs volumes, leurs dns, leurs réseaux... Docker reposant lui sur des principes d'isolation de processus.

Open-source orchestration tool for automation: deployment, management and monitoring of containerized applications, workloads and services. All cloud providers are offering their own branded versions of Kubernetes, including Google, Microsoft, Amazon

Automate deployments, management, networking, scaling and availability of containerized applications.

More extensive than Docker Swarm and is meant to coordinate clusters of nodes at scale in production in an efficient manner

- kubernetes master
    API server that communicates with kubelets to ensure that packages are running as it should. 
- Kubelet 
    Primary node agent that runs on a node. It is responsible for the state of each node, ensuring that all containers on the node are up and running.
- Pod
    a group of one or more containers with shared storage and network. 
- Sidecar 
    Utility container in a pod that's loosely coupled to the main application container
    It was only a nominal distinction, and sidecar containers were basically regular containers in a pod.

open-source system for automation used to manage containerized workloads and services. All cloud providers are offering their own branded versions of Kubernetes, including Google, Microsoft, Amazon

Applications are built using containers (Docker...) allowing you to segment your application into microservices and thus have different configurations for each, making it possible to deploy these microservices independently of each other to speed up certain functionality deliveries.

### Package management

download.page(cloud/pm_helm.md)

- Scaling
CPU, RAM +- => automatic new/remove containers instances 
- Standardisation
Templating tools (Helm) allow standardized resource configuration files
This makes it possible to standardize all the applications deployed in a Kubernetes cluster, and thus maintain a consistent quality standard.
Versioning of K8s resource files also allows for an automated code review and deployment process to significantly reduce the introduction of bugs.
- Disponibilité, stabilité
rolling update: progressive deployment: deploy pods, keep old pods sometimes to rollback if a bug occurs

### Kubernetes Applications

*Stateless applications
trivial to scale, with no coordination. These can take advantage of Kubernetes deployments directly and work great behind Kubernetes Services or Ingress Services.

* Stateful applications
postgres, mysql, etc which generally exist as single processes and persist to disks. These systems generally should be pinned to a single machine and use a single Kubernetes persistent disk. These systems can be served by static configuration of pods, persistent disks, etc or utilize StatefulSets.

* Static distributed applications
zookeeper, cassandra, etc which are hard to reconfigure at runtime but do replicate data around for data safety. These systems have configuration files that are hard to update consistently and are well-served by StatefulSets.

* Clustered applications
etcd, redis, prometheus, vitess, rethinkdb, etc are built for dynamic reconfiguration and modern infrastructure where things are often changing. They have APIs to reconfigure members in the cluster and just need glue to be operated natively seemlessly on Kubernetes, and thus the Kubernetes Operator concept

### Kubernetes vs OpenStack
Openstack was launched in 2010. AWS was the only Cloud, GCP didn't exist, Docker was not a thing. The goal was to provide an open source and private alternative to AWS; building on top of VMs.

Kubernetees was launched in 2014. AWS, Azure, GCP became dominant players of Cloud computing, Docker became the synonym of container. The goal was to be a bridge among the big 3, and between public cloud and private data centers; building on top of containers.

OpenStack is dying down. Kubernetes is the winner, for now.

## More
- https://github.com/priximmo/sommaire-xavki-devops-fr
- https://blog.bitsrc.io/setting-up-a-logging-infrastructure-in-nodejs-ec34898e677e
- https://www.fluentd.org/architecture
- https://medium.com/swlh/setup-own-kubernetes-cluster-via-virtualbox-99a82605bfcc