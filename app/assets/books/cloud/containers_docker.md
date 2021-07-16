# Docker

Container runtime 
A container is a virtualization on top of the operating system layer. Containers do not need to boot up another operating system to run an application. All you need is your application code and its dependent libraries packaged into a single image. The important advantage of containers is that you do not need to boot up another operating system with all the software packages needed for your application on top of the host machine.

https://www.katacoda.com/courses/docker

VSCode: green indicator at left/bottom → "remote containers...open, attach, clone in..." ★★★

## DOCKER QUICKSTART

Install Docker Desktop
https://hub.docker.com/editions/community/docker-ce-desktop-windows

Windows -> Start → Docker Quickstart Terminal
Start in "C:\Program Files\Docker Toolbox"
"C:\Program Files\Git\bin\bash.exe" --login -i "C:\Program Files\Docker Toolbox\start.sh"


https://johnpapa.net/docker-in-5/

1. DOCKER FILE: COMMANDS
We're asking it to get an existing docker image off the web that has `node 6.11` installed
Then we create a folder named app in that image
copy our local package.json to it
install our express package
copy the node server `index.js` to the image
expose our port
start the server

```conf
FROM node:6.11-alpine  
RUN mkdir -p /app  
WORKDIR /app  
COPY package.json .  
RUN npm install  
COPY index.js .  

EXPOSE 8626  
CMD [ "node", "index.js" ]  
```

2. BUILD IMAGE
Execute Dockerfile commands to builds the image and tags it with the name `johnpapa/success`
docker build -t johnpapa/success .  
                                 ↑	
                Don't forget that . at the end of the docker build command
                It's not dirt on your screen. It's quite essential
docker run -d -p 8626:8626 johnpapa/success  
docker run -it -p 8626:8626 johnpapa/success     interactive mode, can use shell commands  

3. USE APP

Browse to http://localhost:8626

4. STOP APP
$ docker ps
	CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
	2dd314fd6c14        johnpapa/success    "node server.js"    3 minutes ago       Up 3 minutes        0.0.0.0:8626->8626/tcp   tender_shockley
docker stop 2dd314fd6c14

find the container we just created from the image, stops the container from running, removes the container, then removes the image.
docker stop $(docker ps -a -q --filter ancestor=johnpapa/success)  

5. CLEAN
docker rm $(docker ps -a -q --filter status=exited)  
docker rmi johnpapa/success  


- https://docs.microsoft.com/en-us/azure/app-service/tutorial-custom-container

* Container Manipulation in CentOS and RHEL
1. https://www.tecmint.com/install-docker-and-learn-containers-in-centos-rhel-7-6/
2. https://www.tecmint.com/install-run-and-delete-applications-inside-docker-containers/
3. https://www.tecmint.com/build-and-configure-docker-container-images-with-dockerfile/
4. https://www.tecmint.com/ctop-monitor-docker-containers/
ctop is a free open source, simple and cross-platform top-like command-line tool for monitoring container metrics in real-time. It allows you to get an overview of metrics concerning CPU, memory, network, I/O for multiple containers and also supports inspection of a specific container.


download.page(cloud/containers_docker_commands.md)
download.page(cloud/containers_docker_compose.md)
download.page(cloud/containers_docker_dockerfile.md)
download.page(cloud/containers_docker_dockerized_app.md)
download.page(cloud/containers_docker_run.md)
download.page(cloud/containers_docker_terms.md)
download.page(cloud/containers_docker_volumes.md)

to add: https://buddy.works/guides/docker-introduction



Run a project without any environment management = focus on development

Docker Image: It’s a template containing instructions to create containers
Docker Container: A Container is the running instance of an image
>docker run       command is used to run a container from an image
If the image does not exist on the host machine, Docker will pull that from [Docker Hub](https://hub.docker.com/)
Once downloaded on your local machine, Docker uses the same image for consecutive container creation. 

Windows: [Docker Desktop](https://docs.docker.com/desktop/#download-and-install)
Linux: download [Docker Engine](https://docs.docker.com/engine/install/)
 
https://hub.docker.com/
Service provided by Docker for finding and sharing container images with your team. 
- Repositories: Push and pull container images.
- Teams & Organizations: Manage access to private repositories of container images.
- Official Images: Pull and use high-quality container images provided by Docker.
- Publisher Images: Pull and use high- quality container images provided by external vendors.
- Builds: Automatically build container images from GitHub and Bitbucket and push them to Docker Hub.
- Webhooks: Trigger actions after a successful push to a repository to integrate Docker Hub with other services.

https://store.docker.com/
https://www.docker.com/
https://docs.docker.com/glossary/


- open-source project
- automate the deployment of applications as portable, self-sufficient containers that can run on the cloud or on-premises

Docker containers can run anywhere
- on-premises (customer datacenter)
- external service provider
- in the cloud (Aws, Azure...) 
Docker image containers can run natively on Linux and Windows.
- Windows images can run only on Windows hosts 
- Linux images can run on Linux hosts and Windows hosts (using a Hyper-V Linux VM, so far), where host means a server or a VM

A docker creates a container out of the application you build. And it is untouched by any changes done around it. So if you have multiple applications talking to each other, then each can be independently maintained if they are turned into individual containers.
Kubernetes is the glue that sticks everything together. It orchestrates the “talking to” of containers which each other.

Applications are built using containers (Docker...) allowing you to segment your application into microservices and thus have different configurations for each, making it possible to deploy these microservices independently of each other to speed up certain functionality deliveries.

Open-source orchestration tool which is used for the creation, packaging, and deployment of applications using containers. It allows you to package the application with all its libraries, dependencies, and other objects that is needed to run the application. It will allow you to deploy containers as needed to the production environment, development environment, or other environments that you might need.

Containerization software for automating the deployment and management of applications within an isolated environment. This software allows us to “pack” and ship an application, along with all of its needed files, libraries, and dependencies, into a “docker container“. That container can then be easily ported to any Linux system that contain cgroups support within the kernel, and provides a container management environment. Docker is one of several containerization implementations (not to be confused with virtualization) based on this cgroups mechanisms built into the Linux kernel.

![](assets/books/cloud/assets/docker_architecture.svg)


# Docker underlying technology

Docker is written in the Go programming language and takes advantage of several features of the Linux kernel to deliver its functionality. Docker uses a technology called namespaces to provide the isolated workspace called the container. When you run a container, Docker creates a set of namespaces for that container.
These namespaces provide a layer of isolation. Each aspect of a container runs in a separate namespace and its access is limited to that namespace.

* DOCKER SWARM - allows you to run your containers on more than one machine. 
To quickly create a multiple node machine:
[Docker for AWS](https://beta.docker.com/)
[Docker for Azure](https://beta.docker.com/)

## install

* Docker Desktop for Windows
Community version of Docker for Microsoft Windows
Windows 10 Home, Pro, Enterprise, Education

- Docker Engine
https://docs.docker.com/engine/
- Docker CLI client
- Docker Compose
 
- Notary
https://docs.docker.com/notary/getting_started/
tool for publishing and managing trusted collections of content. Publishers can digitally sign collections and consumers can verify integrity and origin of content.

- Kubernetes
https://github.com/kubernetes/kubernetes/

- Credential Helper
https://github.com/docker/docker-credential-helpers/
to keep Docker login credentials safe by storing in platform keystores

- Docker Hub: library of certified images and templates 
  
  https://docs.docker.com/docker-for-windows/install-windows-home/
  
* Docker for Windows (Hyper-V)

  https://docs.docker.com/docker-for-windows/
  Hyper-V and Containers Windows features must be enabled.

    
* Open Source Hypervisor
    - Microsoft Hyper V
    - VMware Free ESXi
    - Lguest
    - Oracle VirtualBox: https://connect.ed-diamond.com/Linux-Pratique/LPHS-045/Decouvrez-la-virtualisation-avec-VirtualBox
    - Xvisor
    - VMware Workstation Player
    - OpenVZ
    - SmartOS

    Hyper-V and Oracle VM VirtualBox can both be used to handle a businesses server virtualization needs

    * Hyper-V 
    Microsoft's hardware virtualization product. It lets you create and run a software version of a computer, called a virtual machine. Each virtual machine acts like a complete computer, running an operating system and programs.
    Hyper-V Highlights and Features:
    - High performance virtualization layer: Virtualization necessarily adds some overhead to all guest activities. ...
    - Support for up to 1,024 virtual machines running on a single host.
    - Even balancing of resources across guests.
    Provides hardware virtualization: each virtual machine runs on virtual hardware. Hyper-V lets you create virtual hard drives, virtual switches, and a number of other virtual devices all of which can be added to virtual machines.

## Docker Desktop

a MINGW64 environment

## More
- [Running your first container](https://github.com/docker/labs/blob/master/beginner/chapters/alpine.md)

- https://python.plainenglish.io/turn-your-python-script-into-a-real-program-with-docker-c200e15d5265
- https://github.com/clue/docker-json-server
- https://github.com/priximmo/sommaire-xavki-devops-fr
- https://devopsmyway.com/install-docker-on-windows/
- https://www.liquidweb.com/kb/how-to-install-and-use-containerization/
- [install Docker on Ubuntu](https://www.liquidweb.com/kb/install-docker-ubuntu-16-04/)
- https://www.padok.fr/technologies/kubernetes
- https://blog.logrocket.com/node-js-docker-improve-dx/
- https://blog.bitsrc.io/setting-up-a-logging-infrastructure-in-nodejs-ec34898e677e
- https://blog.bitsrc.io/

- https://blog.bitsrc.io/best-practices-for-writing-a-dockerfile-68893706c3

- https://medium.com/swlh/deploy-your-net-core-3-1-application-to-heroku-with-docker-eb8c96948d32

- https-medium-com-adhasmana-how-to-do-ci-and-cd-of-node-js-application-using-github-actions-860007bebae6
- https://intellitect.com/docker-postgresql/
- https://intellitect.com/docker-scaffold/
- https://intellitect.com/asp-net-core-dynamic-routing-with-constraints/
- https://dev.to/rinkiyakedad/cross-container-communication-and-networking-in-docker-39n0
- https://docs.microsoft.com/fr-fr/windows/wsl/tutorials/wsl-containers
- https://dev.to/nas5w/how-to-serve-a-vue-app-with-nginx-in-docker-4p54
- https://hub.docker.com/r/clue/json-server/~/dockerfile/
-https://levelup.gitconnected.com/asynchronous-tasks-in-python-with-celery-rabbitmq-redis-480f6e506d76
- https://codeburst.io/direct-connection-to-a-docker-container-with-ssh-56e1d2744ee5

## TO READ

- https://medium.com/spatial-data-science/how-to-create-your-first-docker-for-geospatial-environment-c6893d98ce0e
- https://andrewlock.net/running-kubernetes-and-the-dashboard-with-docker-desktop
- https://www.kdnuggets.com/2021/04/dockerize-any-machine-learning-application.html
- https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers
- https://betterprogramming.pub/how-to-get-docker-to-play-nicely-with-your-python-data-science-packages-81d16f1080d2