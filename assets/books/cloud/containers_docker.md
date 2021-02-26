# Docker

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



Images - The file system and configuration of our application which are used to create containers. To find out more about a Docker image, run docker inspect alpine. In the demo above, you used the docker pull command to download the alpine image. When you executed the command docker run hello-world, it also did a docker pull behind the scenes to download the hello-world image.

Containers - Running instances of Docker images — containers run the actual applications. A container includes an application and all of its dependencies. It shares the kernel with other containers, and runs as an isolated process in user space on the host OS. You created a container using docker run which you did using the alpine image that you downloaded. A list of running containers can be seen using the docker ps command.

Docker daemon - The background service running on the host that manages building, running and distributing Docker containers.

Docker client - The command line tool that allows the user to interact with the Docker daemon.

Docker Store - A registry of Docker images, where you can find trusted and enterprise ready containers, plugins, and Docker editions. You'll be using this later in this tutorial.

Docker Swarm - allows you to run your containers on more than one machine. 
To quickly create a multiple node machine:
[Docker for AWS](https://beta.docker.com/)
[Docker for Azure](https://beta.docker.com/)


* Dockerfile
- Named "Dockerfile" by default, in the root of the context
- text instructions to assemble an image (add packages, copy files...)
- commands a user could call on the command line 
- The Docker daemon runs the instructions in the Dockerfile
- https://docs.docker.com/engine/reference/builder

```bash
FROM node:12-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "/app/src/index.js"]
```

```bash
# Comment

# syntax=[remote image reference]      parser directives
# syntax=docker/dockerfile:1.0
# escape=` (backtick)
# escape=\ (backslash)

ARG VERSION=latest
FROM 'parentimage'                     Dockerfile must begin with a FROM instruction
FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]
FROM busybox:$VERSION

INSTRUCTION arguments                  INSTRUCTION are not case-sensitive

RUN <command> (shell form, the command is run in a shell, which by default is /bin/sh -c on Linux or cmd /S /C on Windows)
RUN ["executable", "param1", "param2"] (exec form, parsed as a JSON array so use ", not ')     

RUN echo 'we are running some # of cool things'
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y ...
RUN ["c:\\windows\\system32\\tasklist.exe"]
RUN /bin/bash -c 'source $HOME/.bashrc; echo $HOME'
RUN ["/bin/bash", "-c", "echo hello"]    use a shell,other than '/bin/sh'

CMD ["executable","param1","param2"] (exec form, this is the preferred form)
CMD ["param1","param2"] (as default parameters to ENTRYPOINT)
CMD command param1 param2 (shell form)

ARG
    defines a variable that users can pass at build-time to the builder 
    with the docker build command using the --build-arg <varname>=<value>
    FROM busybox
    ARG user1
    ARG buildno
    
    AUTOMATIC ARG VARIABLES
    TARGETPLATFORM - platform of the build result. Eg linux/amd64, linux/arm/v7, windows/amd64.
    TARGETOS - OS component of TARGETPLATFORM
    TARGETARCH - architecture component of TARGETPLATFORM
    TARGETVARIANT - variant component of TARGETPLATFORM
    BUILDPLATFORM - platform of the node performing the build.
    BUILDOS - OS component of BUILDPLATFORM
    BUILDARCH - architecture component of BUILDPLATFORM
    BUILDVARIANT - variant component of BUILDPLATFORM
    
    FROM alpine
    ARG TARGETPLATFORM
    RUN echo "I'm building for $TARGETPLATFORM"

ADD
    copies new files, directories or remote file URLs from <src> 
    and adds them to the filesystem of the image at the path <dest>
    ADD [--chown=<user>:<group>] <src>... <dest>
    ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]
    <dest> is an absolute path, or a path relative to WORKDIR
    ADD test.txt relativeDir/
    ADD test.txt /absoluteDir/
    ADD hom?.txt /mydir/
    ADD --chown=55:mygroup files* /somedir/
    ADD --chown=bin files* /somedir/
    ADD --chown=1 files* /somedir/
    ADD --chown=10:11 files* /somedir/
COPY
    copies new files or directories from <src> 
    and adds them to the filesystem of the container at the path <dest>
    COPY [--chown=<user>:<group>] <src>... <dest>   
    COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
    COPY hom?.txt /mydir/
    COPY hom* /mydir/
ENV <key>=<value> ...
    sets the environment variable. Persist if container is run from the resulting image
    ENV MY_NAME="John Doe"
    docker inspect     
    docker run --env <key>=<value>
ENTRYPOINT
    configure a container that will run as an executable
    ENTRYPOINT ["executable", "param1", "param2"]
    ENTRYPOINT command param1 param2    
    
    starts nginx with its default content, listening on port 80:
    docker run -i -t --rm -p 80:80 nginx
    
    FROM ubuntu
    ENTRYPOINT ["top", "-b"]
    CMD ["-c"]
    docker run -it --rm --name test  top -H    see that top is the only process
    docker exec -it test ps aux

EXPOSE <port> [<port>/<protocol>...]
    container listen on the specified network ports at runtime.
    EXPOSE 80/tcp
    EXPOSE 80/udp
    docker run -p 80:80/tcp -p 80:80/udp ...
FROM
LABEL
    key-value pair that adds metadata to an image
    LABEL version="1.0"
    docker image inspect --format='' myimage
SHELL ["executable", "parameters"]    
    To overridde the default shell that is on: 
    - Linux is ["/bin/sh", "-c"]
    - Windows is ["cmd", "/S", "/C"]
    useful on Windows where there are two commonly used and quite different native shells: cmd and powershell
    
    FROM microsoft/windowsservercore
    # Executed as cmd /S /C echo default
    RUN echo default
    # Executed as cmd /S /C powershell -command Write-Host default
    RUN powershell -command Write-Host default
    # Executed as powershell -command Write-Host hello
    SHELL ["powershell", "-command"]
    RUN Write-Host hello
    # Executed as cmd /S /C echo hello
    SHELL ["cmd", "/S", "/C"]
    RUN echo hello

    # escape=`
    FROM microsoft/nanoserver
    SHELL ["powershell","-command"]
    RUN New-Item -ItemType Directory C:\Example
    ADD Execute-MyCmdlet.ps1 c:\example\
    RUN c:\example\Execute-MyCmdlet -sample 'hello world'

STOPSIGNAL
USER
    Sets the user name (or UID) and optionally the user group (or GID) to use when running the image and for any RUN, CMD, ENTRYPOINT
    USER <user>[:<group>]
    USER <UID>[:<GID>]
    
    FROM microsoft/windowsservercore
    # Create Windows user in the container
    RUN net user /add patrick
    # Set it for subsequent commands
    USER patrick

VOLUME ["/data"]
    creates a mount point with the specified name 
    marks it as holding externally mounted volumes from native host or other containers. 
    VOLUME ["/var/log/"]    JSON array
    VOLUME /var/log 
    VOLUME /var/log /var/db   plain string with multiple arguments
    
    image that causes docker run to 
    - create a new mount point at /myvol 
    - copy the greeting file into the newly created volume
    FROM ubuntu
    RUN mkdir /myvol
    RUN echo "hello world" > /myvol/greeting
    VOLUME /myvol
    
WORKDIR
    sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD
    WORKDIR /a
    WORKDIR b
    WORKDIR c
    RUN pwd

ONBUILD
    adds to the image a trigger instruction to be executed at a later time, when the image is used as the base for another build
    ONBUILD ADD . /app/src
    ONBUILD RUN /usr/local/bin/python-build --dir /app/src
```

```bash
# escape=`    else error cause \ is treated as a line continuation
FROM microsoft/nanoserver
COPY testfile.txt c:\\
RUN dir c:\
```

```bash
ENV abc=hello           Environment variable
ENV abc=bye def=$abc
ENV ghi=$abc
FROM busybox
ENV FOO=/bar
WORKDIR ${FOO}   # WORKDIR /bar
ADD . $FOO       # ADD . /bar
COPY \$FOO /quux # COPY $FOO /quux

```

* .dockerignore
```bash
# comment
*/temp*
*/*/temp*
temp?
```


* Build images 
>docker build .
>docker build -f /path/to/a/Dockerfile .     -f for a specific dockerfile
>$ docker build -t shykes/myapp .            tag if success 
Builds an image from 
- a Dockerfile
- a build’s context: set of files at a specified location PATH or URL
The PATH is a directory on your local filesystem
The URL is a Git repository location


## install

* Docker Desktop for Windows
Community version of Docker for Microsoft Windows
Windows 10 Home, Pro, Enterprise, Education

- Docker Engine
https://docs.docker.com/engine/
- Docker CLI client
- Docker Compose
https://docs.docker.com/compose/
 tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services.
 
1. Dockerfile: Define your app’s environment so it can be reproduced anywhere.
2. docker-compose.yml: Define the services that make up your app so they can be run together in an isolated environment.
3. Run docker-compose up and Compose starts and runs your entire app.

Compose files 
- docker-compose.yml 
- docker-stack.yml
 
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
    - Oracle VirtualBox
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

## Docker Quickstart

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

```bash
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
                Don't forget that . at the end of the docker build command. 
                It's not dirt on your screen. It's quite essential
docker run -d -p 8626:8626 johnpapa/success  
docker run -it -p 8626:8626 johnpapa/success  

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


## Docker Desktop

a MINGW64 environment

## Commands

https://docs.docker.com/compose/reference/

```bash

history
clear
dir
pwd
cd /
cd  /c/Temp/wordpress
ls
ls -l /var/www/html/wp-content/themes/mytheme

# CREATE DOCKER FILE
mkdir wp-local && cd wp-local 
touch docker-compose.yml
docker create docker-compose.yml

touch readme.md    

# cat > readme.md << EOF
blabla...
blabla... CTRL-C
cat readme.md


# START CONTAINER 
docker-compose up
docker-compose up -d
docker run hello-world   Most basic use of a Docker image is to run it and let it exist

# FETCH IMAGES
docker pull alpine    Fetches the alpine image from the Docker registry and saves it in our system

# LIST IMAGE
docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
alpine                 latest              c51f86c28340        4 weeks ago         1.109 MB
hello-world             latest              690ed74de00f        5 months ago        960 B

# RUN CONTAINER
docker run alpine ls -l
docker pull ubuntu:12.04
docker pull ubuntu                  will pull an image named ubuntu:latest
  The Docker client contacts the Docker daemon
  The Docker daemon checks local store if the image (alpine in this case) is available locally, and if not, downloads it from Docker Store. (Since we have issued docker pull alpine before, the download step is not necessary)
  The Docker daemon creates the container and then runs a command in that container.
  The Docker daemon streams the output of the command to the Docker client

docker run -d -p 80:80 docker/getting-started
docker run -dp 80:80 docker/getting-started
-d - run the container in detached mode (in the background)
-p 80:80 - map port 80 of the host to port 80 in the container

docker run --name static-site -e AUTHOR="Your Name" -d -P dockersamples/static-site
--name allows you to specify a container name
-d will create a container with the process detached from our terminal
-P will publish all the exposed container ports to random ports on the Docker host
-e is how you pass environment variables to the container
AUTHOR is the environment variable name and Your Name is the value that you can pass
 
docker run --name static-site-2 -e AUTHOR="Your Name" -d -p 8888:80 dockersamples/static-site     
This run a second webserver at the same time, specifying a custom host port mapping to the container webserver

See the ports by running
docker port static-site
443/tcp -> 0.0.0.0:32772
80/tcp -> 0.0.0.0:32773

http://localhost:[YOUR_PORT_FOR 80/tcp] →  http://localhost:32773

docker-machine ip default      To find the hostname
192.168.99.100
http://<YOUR_IPADDRESS>:[YOUR_PORT_FOR 80/tcp] → http://192.168.99.100:32773

# CONTAINER RUNNING
docker ps         shows you all containers that are currently running
docker ps -a      shows you all containers that you ran
docker ps --filter "status=exited" | grep 'weeks ago' | awk '{print $1}' | xargs --no-run-if-empty docker rm

# DOCKER MACHINE (IP)
docker-machine
docker-machine ip
docker-machine logs
docker-machine ls


docker exec command     allows you to run commands inside a Docker container

LIST OF ALL CONTAINERS THAT YOU RAN:
docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
36171a5da744        alpine              "/bin/sh"                5 minutes ago       Exited (0) 2 minutes ago                        fervent_newton
a6a9d46d0b2f        alpine             "echo 'hello from alp"    6 minutes ago       Exited (0) 6 minutes ago                        lonely_kilby
ff0a5c3750b9        alpine             "ls -l"                   8 minutes ago       Exited (0) 8 minutes ago                        elated_ramanujan
c317d0a9e3d2        hello-world         "/hello"                 34 seconds ago      Exited (0) 12 minutes ago                       stupefied_mcclintock

RUN MORE THAN JUST ONE COMMAND IN A CONTAINER:
docker run alpine /bin/sh         exit after running any scripted commands, unless they are run in an interactive terminal 
docker run -it alpine /bin/sh     -it attaches an interactive tty in the container. Now you can run as many commands in the container as you want.
/ # ls
bin      dev      etc      home     lib      linuxrc  media    mnt      proc     root     run      sbin     sys      tmp      usr      var
/ # uname -a
Linux 97916e8cb5dc 4.4.27-moby #1 SMP Wed Oct 26 14:01:48 UTC 2016 x86_64 Linux
 
Give you a bash shell inside your mysql container:
docker exec -it some-mysql bash
docker logs some-mysql


# STOP 
docker-compose down
docker-compose down --volumes
docker-compose down -v

docker stop $(docker ps -a -q --filter status=running)  

docker ps
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
    2dd314fd6c14        joe/success    "node server.js"    3 minutes ago       Up 3 minutes  ...
docker stop 2dd314fd6c14

1. Find the container we just created from the image
2. Stops the container from running
3. Removes the container
4. Removes the image
docker stop $(docker ps -a -q --filter ancestor=joe/success)  
docker rm $(docker ps -a -q --filter status=exited)  
docker rmi joe/success  
    
# CLEAN

docker {container,image,volume,network} prune
docker container prune
docker system prune        Remove (for images) only dangling images, or images without a tag:
docker system prune -a     Delete ALL unused data (containers stopped, volumes without containers and images with no containers):

docker rm [OPTIONS] CONTAINER [CONTAINER...] will remove one or more containers
docker volume rm $(docker volume ls)
docker volume rm * 
docker rm 0d

Remove ALL STOPPED CONTAINERS
docker rm $(docker ps -a -q)
docker rm `docker ps --no-trunc -aq`
FOR /f "tokens=*" %i IN ('docker ps -a -q') DO docker rm %i
PS>docker rm @(docker ps -aq)

Remove ALL CONTAINERS (STOPPED AND NON STOPPED)
docker rm -f $(docker ps -a -q)

Remove containers created before an other container
docker rm $(docker ps --before 9c49c11c8d21 -q)

Remove containers created after a certain container
docker rm $(docker ps --since a6ca4661ec7f -q)

# LOGS
docker volume ls
Check the logs of the container for any errors:
docker logs your_container_id 
docker logs 670e58bd

# VOLUMES
docker volume
docker volume ls
docker volume inspect
docker volume inspect $b836eb82dcfe3616e0aaa2ade66218b4f837462818c482d392ea28af19d2
docker volume inspect wordpress_db_data

Docker create the volume in the /var/lib/docker/volumes folder. This volume persist as long as you are not typing docker-compose down -v or delete it 

docker ps -a    Find the ID of your container and then run:
docker exec -it your_container_id bash  
Then once you are attached run:
ls -l /var/www/html/wp-content/themes/mytheme
Detach: CTRL+P+Q
Check the logs of the container for any errors:
docker logs your_container_id 
```


## DATA IN DOCKER

By default all files created inside a container are stored on a writable container layer 
→ data doesn’t persist when that container no longer exists
→ difficult to get the data out of the container if another process needs it.

Docker has options for containers to store files in the host machine, so that the files are persisted even after the container stops: 
- volumes
Stored in a part of the host filesystem which is managed by Docker (/var/lib/docker/volumes/)
Stored within a directory on the Docker host
Are isolated from the core functionality of the host machine (bind mounts are not)
A given volume can be mounted into multiple containers simultaneously. When no running container is using a volume, the volume is still available to Docker and is not removed automatically. You can remove unused volumes using docker volume prune
When you mount a volume, it may be named or anonymous
Volumes also support the use of volume drivers, which allow you to store your data on remote hosts or cloud providers, among other possibilities.
- bind mounts
Stored anywhere on the host system
The file or directory is referenced by its full path on the host machine. The file or directory does not need to exist on the Docker host already.
- tmpfs mount (Docker on Linux)
Stored in the host system’s memory only
Not persisted on disk
- named pipe (Docker on Windows)
Used for communication between the Docker host and a container

https://docs.docker.com/storage/
http://localhost/tutorial/persisting-our-data/

### Volumes
Mechanism for persisting data generated by and used by Docker containers
If you start a container with a volume that does not yet exist, Docker creates the volume for you. 
New volumes can have their content pre-populated by a container.

https://docs.docker.com/storage/volumes/
https://docs.docker.com/compose/compose-file/#volume-configuration-reference

* CREATE AND MANAGE VOLUMES OUTSIDE THE SCOPE OF ANY CONTAINER
docker volume create my-vol        Create a volume
docker volume ls                   List volumes
    local               my-vol
docker volume inspect my-vol       Inspect a volume: 
    [
        {
            "Driver": "local",
            "Labels": {},
            "Mountpoint": "/var/lib/docker/volumes/my-vol/_data",
            "Name": "my-vol",
            "Options": {},
            "Scope": "local"
        }
    ]


Docker stores containers in 
- /var/lib/docker/containers in Ubuntu
- /var/lib/docker/volumes


. is for local dir
Use . and relative paths to copying between containers

```bash
docker-volumes ls

If you don't know what's the name of the container, you can find it using:
docker ps --format "{{.Names}}"

# COPY FILES host machine → docker container
docker cp c:\path\to\local\file container_name:/path/to/target/dir/

docker cp /Docker/init.sql wordpress_db_data
docker cp c:\abc.doc <containerid> :C:\inetpub\wwwroot\abc.doc
cd /d/
docker cp Temp/my-super-file.txt container-name:/tmp/
docker cp php.ini-development  84085df827d4:usr/local/etc/php
docker cp php.ini-production  84085df827d4:usr/local/etc/php
# Absolute path may not supported: 
docker cp /d/Temp/my-super-file.txt container-name:/tmp/   

# COPY FILES docker container → host machine
If you don't know what's the name of the container, you can find it using:
docker ps --format "{{.Names}}"

docker cp d56a9442ccd0:usr/local/etc/php/php.ini-development .    			
docker cp d56a9442ccd0:usr/local/etc/php/php.ini-production .    
docker cp d56a9442ccd0:usr/local/etc/php/php.ini-development temp\xxx.txt
```

## TIPS



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

It 
- copies our package.json
- runs npm install 
- starts the server

To make sure our file is correct, from the root folder:
> docker build -t abhinavdhasmana/github-action-example-node . 
To see our latest image
>docker images 
Run our container
>docker run -d -p 3000:3000 abhinavdhasmana/github-action-example-node. 
Browser to http://localhost:3000/ 






## WORDPRESS

* php.ini
Create your own `Dockerfile` and `ADD php.ini /usr/local/etc/php`
Mount a volume with your php.ini at `/usr/local/etc/php`

php.ini
; Maximum allowed size for uploaded files.
; http://php.net/upload-max-filesize
upload_max_filesize = 2M

```bash
docker cp php.ini-development  84085df827d4:usr/local/etc/php
docker cp php.ini-production  84085df827d4:usr/local/etc/php
docker cp d56a9442ccd0:usr/local/etc/php/php.ini-development .    			
docker cp d56a9442ccd0:usr/local/etc/php/php.ini-production .    
docker cp d56a9442ccd0:usr/local/etc/php/php.ini-development temp\xxx.txt
```

- https://stackoverflow.com/questions/26598738/how-to-create-user-database-in-script-for-docker-postgres
- https://www.digitalocean.com/community/questions/copy-custom-wordpress-theme-with-docker-composer
- https://www.datanovia.com/en/lessons/wordpress-docker-setup-files-example-for-local-development/
- https://www.viralpatel.net/local-wordpress-docker/
- https://upcloud.com/community/tutorials/deploy-wordpress-with-docker-compose/
- https://joshmobley.net/writing/2017/04/09/easy-wordpress-migration-with-docker.html
- https://cntnr.io/setting-up-wordpress-with-docker-262571249d50

```Dockerfile
version: '2'
services:
  wordpress:
    depends_on:
      - db
    image: wordpress:4.7.1
    restart: always
    volumes:
      - ./wp-content:/var/www/html/wp-content           mount the `wp-content` folder, containing the themes and plugins, on my local machine into the container.       
    environment:                                        The other files in the base wordpress installation will be provided by the container itself. 
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_PASSWORD: p4ssw0rd!
    ports:
      - 80:80
      - 443:443
    networks:
      - back
  db:                                                   the 'db' database
    image: mysql:5.7
    restart: always
    volumes:
       - db_data:/var/lib/mysql                         database will be persisted to a named volume db_data, so that even when I remove the container,        
    environment:                                        the data will still live somewhere on my machine and can be mounted again in a new container.
      MYSQL_ROOT_PASSWORD: p4ssw0rd!
    networks:
      - back
  phpmyadmin:
    depends_on:
      - db                                          phpmyadmin will connect to the 'db' database service over the backnetwork and serve on port 8080.
    image: phpmyadmin/phpmyadmin
    restart: always
    ports:
      - 8080:80
    environment:
      PMA_HOST: db
      MYSQL_ROOT_PASSWORD: p4ssw0rd!
    networks:
      - back
networks:
  back:
volumes:
  db_data:
```

## Mysql

https://hub.docker.com/_/Mysql

docker run --name some-mysql -v /my/own/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag

The -v /my/own/datadir:/var/lib/mysql part of the command mounts the /my/own/datadir directory from the underlying host system as /var/lib/mysql inside the container, where MySQL by default will write its data files.


Creating database dumps
$ docker exec some-mysql sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > /some/path/on/your/host/all-databases.sql

Restoring data from dump files
$ docker exec -i some-mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < /some/path/on/your/host/all-databases.sql

## SAMPLES

Most basic use of a Docker image is to run it and let it exist: docker run hello-world

* Regular schedule
http://www.anotherchris.net/posts/running-cron-jobs-inside-a-docker-container
run a dotnet core console app that parses Reddit posts and posts itself, inside a Docker container, every 30 minutes on set days of the week.
cron_task.sh
crontab
docker-cron-job-example
run_app.sh 		dotnet /app/MyApp.dll
    
## Terms

Container image: A package with all the dependencies and information needed to create a container. An image includes all the dependencies (such as frameworks) plus deployment and execution configuration to be used by a container runtime. Usually, an image derives from multiple base images that are layers stacked on top of each other to form the container’s filesystem. An image is immutable once it has been created.

Dockerfile: A text file that contains instructions for building a Docker image. It’s like a batch script, the first line states the base image to begin with and then follow the instructions to install required programs, copy files, and so on, until you get the working environment you need.

Build: The action of building a container image based on the information and context provided by its Dockerfile, plus additional files in the folder where the image is built. You can build images with the following Docker command:
docker build

Container: An instance of a Docker image. A container represents the execution of a single application, process, or service. It consists of the contents of a Docker image, an execution environment, and a standard set of instructions. When scaling a service, you create multiple instances of a container from the same image. Or a batch job can create multiple containers from the same image, passing different parameters to each instance.

Volumes: Offer a writable filesystem that the container can use. Since images are read-only but most programs need to write to the filesystem, volumes add a writable layer, on top of the container image, so the programs have access to a writable filesystem. The program doesn’t know it’s accessing a

layered filesystem, it’s just the filesystem as usual. Volumes live in the host system and are managed by Docker.

Tag: A mark or label you can apply to images so that different images or versions of the same image (depending on the version number or the target environment) can be identified.

Multi-stage Build: Is a feature, since Docker 17.05 or higher, that helps to reduce the size of the final images. In a few sentences, with multi-stage build you can use, for example, a large base image, containing the SDK, for compiling and publishing the application and then using the publishing folder with a small runtime-only base image, to produce a much smaller final image.

Repository (repo): A collection of related Docker images, labeled with a tag that indicates the image version. Some repos contain multiple variants of a specific image, such as an image containing SDKs (heavier), an image containing only runtimes (lighter), etc. Those variants can be marked with tags. A single repo can contain platform variants, such as a Linux image and a Windows image.

Registry: A service that provides access to repositories. The default registry for most public images is Docker Hub (owned by Docker as an organization). A registry usually contains repositories from multiple teams. Companies often have private registries to store and manage images they’ve created. Azure Container Registry is another example.

Multi-arch image: For multi-architecture, it’s a feature that simplifies the selection of the appropriate image, according to the platform where Docker is running. For example, when a Dockerfile requests a base image mcr.microsoft.com/dotnet/sdk:5.0 from the registry, it actually gets 5.0-nanoserver-1909, 5.0-nanoserver-1809 or 5.0-buster-slim, depending on the operating system and version where Docker is running.

Docker Hub: A public registry to upload images and work with them. Docker Hub provides Docker image hosting, public or private registries, build triggers and web hooks, and integration with GitHub and Bitbucket.
Azure Container Registry: A public resource for working with Docker images and its components in Azure. This provides a registry that’s close to your deployments in Azure and that gives you control over access, making it possible to use your Azure Active Directory groups and permissions.

Docker Trusted Registry (DTR): A Docker registry service (from Docker) that can be installed on-premises so it lives within the organization’s datacenter and network. It’s convenient for private images that should be managed within the enterprise. Docker Trusted Registry is included as part of the Docker Datacenter product. For more information, see Docker Trusted Registry (DTR).

Docker Community Edition (CE): Development tools for Windows and macOS for building, running, and testing containers locally. Docker CE for Windows provides development environments for both Linux and Windows Containers. The Linux Docker host on Windows is based on a Hyper-V virtual machine. The host for Windows Containers is directly based on Windows. Docker CE for Mac is based on the Apple Hypervisor framework and the xhyve hypervisor, which provides a Linux Docker host virtual machine on macOS X. Docker CE for Windows and for Mac replaces Docker Toolbox, which was based on Oracle VirtualBox.

Docker Enterprise Edition (EE): An enterprise-scale version of Docker tools for Linux and Windows development.

Compose: A command-line tool and YAML file format with metadata for defining and running multi-container applications. You define a single application based on multiple images with one or more .yml files that can override values depending on the environment. After you’ve created the definitions, you can deploy the whole multi-container application with a single command (docker-compose up) that creates a container per image on the Docker host.

Cluster: A collection of Docker hosts exposed as if it were a single virtual Docker host, so that the application can scale to multiple instances of the services spread across multiple hosts within the cluster. Docker clusters can be created with Kubernetes, Azure Service Fabric, Docker Swarm and Mesosphere DC/OS.

Orchestrator: A tool that simplifies management of clusters and Docker hosts. 
Orchestrators enable you to manage their images, containers, and hosts through a command-line interface (CLI) or a graphical UI. You can manage container networking, configurations, load balancing, service discovery, high availability, Docker host configuration, and more. An orchestrator is responsible for running, distributing, scaling, and healing workloads across a collection of nodes. Typically, orchestrator products are the same products that provide cluster infrastructure, like Kubernetes and Azure Service Fabric, among other offerings in the marke

## More
- [Running your first container](https://github.com/docker/labs/blob/master/beginner/chapters/alpine.md)

- https://github.com/clue/docker-json-server
- https://github.com/priximmo/sommaire-xavki-devops-fr
- https://devopsmyway.com/install-docker-on-windows/
- https://www.liquidweb.com/kb/how-to-install-and-use-containerization/
- [install Docker on Ubuntu](https://www.liquidweb.com/kb/install-docker-ubuntu-16-04/)
- https://www.padok.fr/technologies/kubernetes
- https://blog.logrocket.com/node-js-docker-improve-dx/
- https://blog.bitsrc.io/setting-up-a-logging-infrastructure-in-nodejs-ec34898e677e
- https://blog.bitsrc.io/

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
