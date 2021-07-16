## DOCKER COMMANDS


>docker -v 
Docker allows you to use $PWD as a placeholder for the current directory.

>docker help run





>mkdir -p /var/docker/ubuntu/apache
>touch /var/docker/ubuntu/apache/Dockerfile
>vi /var/docker/ubuntu/apache/Dockerfile

📄 DOCKERFILE
```yaml
FROM ubuntu                            Take the 'latest' image from Docker Hub if no tag is submitted, say 14:10
MAINTAINER  your_name  <user@domain.tld>
RUN apt-get -y install apache2                                                  install Apache daemon 
RUN echo “Hello Apache server on Ubuntu Docker” > /var/www/html/index.html      echo some text into
EXPOSE 80                               Docker container will listen on port 80, but the port will be not available to outside
CMD /usr/sbin/apache2ctl -D FOREGROUND
```

Creating the image
>docker build -t ubuntu-apache /var/docker/ubuntu/apache/
List all available images 
> docker images

Run the Container and Access Apache from LAN
>docker run -d -p 81:80 ubuntu-apache
-d option runs the ubuntu-apache container in background (as a daemon)
-p option maps the container port 80 to your localhost port 81

--name assign a descriptive name for the container: 
>docker run --name my-www -d -p 81:80 ubuntu-apache
Then
>docker stats my-www
>docker stats <name or ID of the container>

[Netstat](https://www.tecmint.com/20-netstat-commands-for-linux-network-management/<7>) command will give you an idea about what ports the host is listening to.
>netstat -tupln | grep :81

Status of the running container
>docker ps 
>docker top <name or ID of the container>
>docker stop <name or ID of the container>

[IP](https://www.tecmint.com/ip-command-examples/) command line to show network interface IP addresses.
>ip addr               [List nework interfaces]

The webpage can be displayed on your host from the command line using curl utility against your machine IP Address, localhost, or docker net interface on port 81.
>curl ip-address:81    [System Docker IP Address]
>curl localhost:81     [Localhost]
http://ip-address:81

Create a System-wide Configuration File for Docker Container
On CentOS/RHEL you can create a systemd configuration file and manage the container as you normally do for any other local service.
>vi /etc/systemd/system/apache-docker.service
📄 apache-docker.service 
```yaml
[Unit]
Description=apache container
Requires=docker.service
After=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker start -a my-www
ExecStop=/usr/bin/docker stop -t 2 my-www

[Install]
WantedBy=local.target
```

Reload the systemd daemon to reflect changes 
>systemctl daemon-reload

Start the container
>systemctl start apache-docker.service
>systemctl status apache-docker.service






* FIND EXISTING IMAGES 
- registry.hub.docker.com/
- docker search redis

* FINDING RUNNING CONTAINERS
docker ps 		  view running instance
docker ps -a 		view all instances (running or not)
docker ps --format "{{.Names}}"

docker volume ls

Check the logs of the container for any errors:
docker logs your_container_id 
docker logs 670e58bd


docker build --tag hi .
docker build -t johnpapa/success .  
  -t, --tag list: Name and optionally a tag in the 'name:tag' format

docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    hi                  latest              50f7b9cc7d25        4 minutes ago       99.2MB
    ubuntu              latest              f643c72bc252        5 weeks ago         72.9MB

docker run <options> <image-name> .
docker run -d redis                       -d, --detach: Run container in background and print container ID
docker run -d redis:3.2
docker run 50f7
docker run -it ubuntu bash      allows  to get access to a bash shell inside of a container (-i = interactive,  -t, --tty  = Allocate a pseudo-TTY)
docker run ubuntu ps            launches an Ubuntu container and executes the command ps to view all the processes running in a container.

running Redis in the background, with a name of redisHostPort on port 6379
docker run -d --name redisHostPort -p 6379:6379 redis:latest
By default, the port on the host is mapped to 0.0.0.0, which means all IP addresses. You can specify a particular IP address when you define the port mapping, for example, -p 127.0.0.1:6379:6379

docker run -d --name redisDynamic -p 6379 redis:latest              Expose Redis but on a randomly available port
docker port redisDynamic 6379                                       To know which port has been assigned


docker rmi 50f7    remove image 50f7

docker inspect <friendly-name|container-id> provides more details about a running container, such as IP address.
docker logs <friendly-name|container-id> will display messages the container has written to standard error or standard out.

* COPY FILES host machine → docker container
docker cp c:\path\to\local\file container_name:/path/to/target/dir/
docker cp php.ini-production  84085df827d4:usr/local/etc/php

* COPY FILES docker container → host machine
docker cp d56a9442ccd0:usr/local/etc/php/php.ini-development .              
docker cp d56a9442ccd0:usr/local/etc/php/php.ini-development temp\xxx.txt

* PERSISTING DATA
data stored keeps being removed when deleting and re-creating a container
data to be persisted and reused when recreating a container:
Containers are designed to be stateless. Binding directories (also known as volumes) is done using the option -v <host-dir>:<container-dir>. When a directory is mounted, the files which exist in that directory on the host can be accessed by the container and any data changed/written to the directory inside the container will be stored on the host. This allows you to upgrade or change containers without losing your data.

official Redis image stores logs and data into a /data directory
Any data which needs to be saved on the Docker Host, and not inside containers, should be stored in /opt/docker/data/redis

docker run -d --name redisMapped -v /opt/docker/data/redis:/data redis





https://docs.docker.com/compose/reference/

```conf

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

docker run       command is used to run a container from an image
If the image does not exist on the host machine, Docker will pull that from [Docker Hub](https://hub.docker.com/)
Once downloaded on your local machine, Docker uses the same image for consecutive container creation. 

docker run alpine ls -l
docker pull ubuntu:12.04
docker pull ubuntu                  will pull an image named ubuntu:latest
  The Docker client contacts the Docker daemon
  The Docker daemon checks local store if the image (alpine in this case) is available locally, and if not, downloads it from Docker Store. (Since we have issued docker pull alpine before, the download step is not necessary)
  The Docker daemon creates the container and then runs a command in that container.
  The Docker daemon streams the output of the command to the Docker client

docker run -d -p 80:80 docker/getting-started
docker run -dp 80:80 docker/getting-started
-d          run the container in detached mode (in the background)
-p 80:80    map port 80 of the host to port 80 in the container

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
443/tcp -> 0.0.0.0:32772       1g8sz4g8sS_DGLSDG5
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