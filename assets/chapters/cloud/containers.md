# Containers

Containerization is the new norm in DevOps. The DevOps culture has adopted containers, which are essential building blocks for modern pipelines, clusters, applications, etc. The collaboration process usually consists of the development (staging), build, and live phase. In the development phase, developers build or update containers without worrying if and how they will work in a live environment. The build phase is initiated when developers push their changes to the repository, and the tests are triggered automatically. If tests are successful, new production containers are built and deployed, replacing the old ones that are destroyed.

### VMs vs Containers?

* CONTAINERS 
run on the underlying operating system 
container system will provide services from the underlying host and isolate the applications using virtual memory hardware.
A container will virtualize the operating system. Containers are generally smaller, used in a more limited way (like for testing applications before deployment), and do not have a built-in operating systems like VM’s

* VM
have their own operating system using hardware VM support. Hypervisors manage VM’s 
Virtualize the hardware thanks to a hypervisor 
Mimic and entire servers, networks, databases, etc.


![](assets/slides/cloud/assets/vm_vs_container.png)

Containers are the future of application development and hosting. They enable DevOps, developers, and system administrators to build, test, deploy, and maintain applications quickly, securely, and efficiently. Tools built around the containerization concept provide simple solutions for basic web applications. These advanced granular configuration options provide the control many enterprise applications may need. 

### Containerization
Containerization is the process of packaging software code, its required dependencies, configurations, and other detail to be easily deployed in the same or another computing environment. In simpler terms, containerization is the encapsulation of an application and its required environment. 

The containerization process extends the capabilities Virtualization has provided compared to bare metal solutions. Containers offer more flexibility as they are much easier and faster to deploy, require fewer resources to run, and are generally more manageable.

### Containers
A container is a standardized unit of software abstracted from the operating system. It contains code and all its dependencies that can be transferred and run without changing one environment to another. Container states are easily stored in an image that is lightweight, standalone, easily transferable, and provides everything needed for the application to run: code, runtime, system tools, system libraries, and other settings. Containers will always provide the same state, regardless of the infrastructure they run on. Containers isolate software from its environment and ensure that it works uniformly despite differences, for instance, between development and staging.

Benefits
 Ease of Deployment 
 Scalability and Flexibility 
 Consistent 

### Microservices 
Containers usually run a single process that is dedicated to one application function. A simple application can consist of two roles: database and web server, which would be two microservices that are run within two containers. This makes the application scalable both up and down. If you need an additional web server to handle incoming traffic spikes, you can spin up a new web server container within seconds. Once the traffic spike is over, unneeded containers are destroyed, keeping resource usage optimal and keeping costs at a minimum. Various tools allow us to define an application using interdependent services using simple human-readable files that can start containerized applications on any platform running our choice of containerization solution.