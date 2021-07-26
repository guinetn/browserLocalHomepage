# KUBERNETES (K8s or "kube") 

- https://kubernetes.io/
- https://www.loginradius.com/blog/async/rest-api-kubernetes/  to add

Help to deliver and manage containerized, legacy, and cloud-native apps
Rapidly build new applications and services. Cloud-native development starts with microservices in containers, which enables faster development and makes it easier to transform and optimize existing applications. 
Production apps span multiple containers, and those containers must be deployed across multiple server hosts. Kubernetes gives you the orchestration and management capabilities required to deploy containers, at scale, for these workloads.

Configuring Kubernetes, defining nodes, pods, containers within them. Kubernetes handles orchestrating the containers.

Kubernetes orchestration allows you to build application services that span multiple containers, schedule those containers across a cluster, scale those containers, and manage the health of those containers over time. With Kubernetes you can take effective steps toward better IT security.

Kubernetes also needs to integrate with networking, storage, security, telemetry, and other services to provide a comprehensive container infrastructure.


Containers are a fruitful business, and they have the habit of multiplying rapidly. That's by design. Containers are meant to scale, and they scale by spawning clones. Stick the containers into groups (call them pods), and automate how pod lifecycles are managed. That's all Kubernetes really is, and it's changing how servers can run.


Docker can be used as a container runtime that Kubernetes orchestrates. When Kubernetes schedules a pod to a node, the kubelet on that node will instruct Docker to launch the specified containers.
The kubelet then continuously collects the status of those containers from Docker and aggregates that information in the control plane. Docker pulls containers onto that node and starts and stops those containers.
The difference when using Kubernetes with Docker is that an automated system asks Docker to do those things instead of the admin doing so manually on all nodes for all containers.



https://itnext.io/kubernetes-essential-tools-2021-def12e84c572
Kubernetes has been build with the idea of control loops from the ground up, this means that Kubernetes is always watching the state of the cluster to make sure it matches the desired state, for example, that the number of replicas running matches the desired number of replicas. The idea of GitOps is to extend this to applications, so you can define your services as code, for example, by defining Helm Charts, and use a tool that leverages K8s capabilities to monitor the state of your App and adjust the cluster accordingly. That is, if update your code repo, or your helm chart the production cluster is also updated. This is true continuous deployment. The core principle is that application deployment and lifecycle management should be automated, auditable, and easy to understand.


* SPEAK KUBERNETES

- CONTROL PLANE
The collection of processes that control Kubernetes nodes. This is where all task assignments originate.

- NODES
These machines perform the requested tasks assigned by the control plane.

- POD
A group of one or more containers deployed to a single node. All containers in a pod share an IP address, IPC, hostname, and other resources. Pods abstract network and storage from the underlying container. This lets you move containers around the cluster more easily.

- REPLICATION CONTROLLER
 This controls how many identical copies of a pod should be running somewhere on the cluster.

- SERVICE
This decouples work definitions from the pods. Kubernetes service proxies automatically get service requests to the right pod—no matter where it moves in the cluster or even if it’s been replaced.

- KUBELET
This service runs on nodes, reads the container manifests, and ensures the defined containers are started and running.

- KUBECTL
The command line configuration tool for Kubernetes.


A working Kubernetes deployment is called a cluster. You can visualize a Kubernetes cluster as two parts: the control plane and the compute machines, or nodes.

Each node is its own Linux® environment, and could be either a physical or virtual machine. Each node runs pods, which are made up of containers.

The control plane is responsible for maintaining the desired state of the cluster, such as which applications are running and which container images they use. Compute machines actually run the applications and workloads.

Kubernetes runs on top of an operating system (Red Hat® Enterprise Linux®, for example) and interacts with pods of containers running on the nodes.

The Kubernetes control plane takes the commands from an administrator (or DevOps team) and relays those instructions to the compute machines.

This handoff works with a multitude of services to automatically decide which node is best suited for the task. It then allocates resources and assigns the pods in that node to fulfill the requested work.

The desired state of a Kubernetes cluster defines which applications or other workloads should be running, along with which images they use, which resources should be made available to them, and other such configuration details.

From an infrastructure point of view, there is little change to how you manage containers. Your control over containers just happens at a higher level, giving you better control without the need to micromanage each separate container or node.

Your work involves configuring Kubernetes and defining nodes, pods, and the containers within them. Kubernetes handles orchestrating the containers.

Where you run Kubernetes is up to you. This can be on bare metal servers, virtual machines, public cloud providers, private clouds, and hybrid cloud environments. One of Kubernetes’ key advantages is it works on many different kinds of infrastructure.

![assets/books/cloud/assets/kubernetes.svg]

* EXPLORE KUBERNETES

Kubernetes might seem out of reach at first. It's new, a little scary, and worst yet, it apparently requires a cloud. However, there are a few ways to get started.

Run a local instance of Kubernetes on your personal computer: install Minikube or Minishift. It's not quite as satisfying as building a cluster and opening it up to your friends, but it's a great, safe way to get familiar with the landscape, commands, and toolkit.

Minikube
https://opensource.com/article/18/10/getting-started-minikube

Minishift
https://opensource.com/article/18/10/getting-started-minikube

K8s tools
https://itnext.io/kubernetes-essential-tools-2021-def12e84c572

to add:
https://www.redhat.com/en/topics/containers/what-is-kubernetes ★★★
https://www.c-sharpcorner.com/article/build-cicd-pipeline-for-azure-kubernetes/ ★★★
https://developers.redhat.com/blog/2020/05/11/top-10-must-know-kubernetes-design-patterns/
https://andrewlock.net/running-kubernetes-and-the-dashboard-with-docker-desktop
https://opensource.com/downloads/kubernetes-raspberry-pi
https://opensource.com/article/20/6/kubernetes-raspberry-pi


Course 70+videos
https://www.youtube.com/playlist?list=PLn6POgpklwWqfzaosSgX2XEKpse5VY2v5
https://www.youtube.com/watch?v=37VLg7mlHu8&list=PLn6POgpklwWqfzaosSgX2XEKpse5VY2v5&index=1

2015 Google 
orchestrateur. C'est à dire qu'il ne fait que gérer des conteneurs, leurs volumes, leurs dns, leurs réseaux... Docker reposant lui sur des principes d'isolation de processus.

open source container orchestration platform that automates many of the manual processes involved in deploying, managing, and scaling containerized applications
In other words, you can cluster together groups of hosts running Linux® containers, and Kubernetes helps you easily and efficiently manage those clusters.
Kubernetes clusters can span hosts across on-premise, public, private, or hybrid clouds. For this reason, Kubernetes is an ideal platform for hosting cloud-native applications that require rapid scaling, like real-time data streaming through Apache Kafka.

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

* STATEFUL APPLICATIONS
postgres, mysql, etc which generally exist as single processes and persist to disks. These systems generally should be pinned to a single machine and use a single Kubernetes persistent disk. These systems can be served by static configuration of pods, persistent disks, etc or utilize StatefulSets.

* STATIC DISTRIBUTED APPLICATIONS
zookeeper, cassandra, etc which are hard to reconfigure at runtime but do replicate data around for data safety. These systems have configuration files that are hard to update consistently and are well-served by StatefulSets.

* CLUSTERED APPLICATIONS
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