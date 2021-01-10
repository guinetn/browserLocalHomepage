# Docker

https://www.docker.com/

Applications are built using containers (Docker...) allowing you to segment your application into microservices and thus have different configurations for each, making it possible to deploy these microservices independently of each other to speed up certain functionality deliveries.

Open-source orchestration tool which is used for the creation, packaging, and deployment of applications using containers. It allows you to package the application with all its libraries, dependencies, and other objects that is needed to run the application. It will allow you to deploy containers as needed to the production environment, development environment, or other environments that you might need.

Containerization software for automating the deployment and management of applications within an isolated environment. This software allows us to “pack” and ship an application, along with all of its needed files, libraries, and dependencies, into a “docker container“. That container can then be easily ported to any Linux system that contain cgroups support within the kernel, and provides a container management environment. Docker is one of several containerization implementations (not to be confused with virtualization) based on this cgroups mechanisms built into the Linux kernel.

## Docker on ec2 instance (Amazon Linux)
	
```bash    
$ sudo yum update -y
$ sudo yum install docker -y
$ Service docker start
$ docker -v	

Create a docker file (instructions to build an image)
$ mkdir images
$ cd images
$ nano Dockerfile
    FROM ubuntu
    MAINTAINER chandan
    RUN apt-get update
    CMD [ "echo", "Hello World !" ]
$ docker ps 		view running instance
$ docker ps -a 		view all instances (running or not)
$ docker build --tag hi .

$ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    hi                  latest              50f7b9cc7d25        4 minutes ago       99.2MB
    ubuntu              latest              f643c72bc252        5 weeks ago         72.9MB
$ docker run 50f7

$ docker images
$ docker rmi 50f7    remove image 50f7
```

## More
- https://github.com/priximmo/sommaire-xavki-devops-fr
- https://devopsmyway.com/install-docker-on-windows/
- https://www.liquidweb.com/kb/how-to-install-and-use-containerization/
- [install Docker on Ubuntu](https://www.liquidweb.com/kb/install-docker-ubuntu-16-04/)
- https://www.padok.fr/technologies/kubernetes