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

Elastic Search
1. Get the ElasticSearch up and running
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --name myES docker.elastic.co/elasticsearch/elasticsearch:7.4.1
2. Check if our container is up and running
curl -X GET "localhost:9200/_cat/nodes?v&pretty"

### Github sample

https://github.com/abhinavdhasmana/github-action-example-node

```Dockerfile
FROM node:10.16.0-alpine
WORKDIR /source/github-action-example-node
COPY package.json /source/github-action-example-node
RUN cd /source/github-action-example-node && npm i --only=production
COPY . .
EXPOSE 3000
CMD ["sh", "-c", "node server.js"]
```

It copies our package.json, runs npm install and starts the server. To make sure our file is correct, we can run docker build -t abhinavdhasmana/github-action-example-node . from the root folder. If we run docker images , we will see our latest image. We can also run our container with docker run -d -p 3000:3000 abhinavdhasmana/github-action-example-node. Point the browser to http://localhost:3000/ and text will appear.

## More
- https://github.com/priximmo/sommaire-xavki-devops-fr
- https://devopsmyway.com/install-docker-on-windows/
- https://www.liquidweb.com/kb/how-to-install-and-use-containerization/
- [install Docker on Ubuntu](https://www.liquidweb.com/kb/install-docker-ubuntu-16-04/)
- https://www.padok.fr/technologies/kubernetes
- https://blog.logrocket.com/node-js-docker-improve-dx/
- https://blog.bitsrc.io/setting-up-a-logging-infrastructure-in-nodejs-ec34898e677e
- https://blog.bitsrc.io/
- https-medium-com-adhasmana-how-to-do-ci-and-cd-of-node-js-application-using-github-actions-860007bebae6
- https://intellitect.com/docker-postgresql/
- https://intellitect.com/docker-scaffold/
- https://intellitect.com/asp-net-core-dynamic-routing-with-constraints/