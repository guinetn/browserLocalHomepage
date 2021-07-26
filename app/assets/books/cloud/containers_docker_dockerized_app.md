# DOCKERFILE


📄 DOCKERFILE
```conf
FROM node:12-alpine
WORKDIR /app                   
COPY . .
RUN yarn install --production
CMD ["node", "/app/src/index.js"]
```

📄 DOCKERFILE
```conf
FROM node:12-alpine
WORKDIR /app                   
COPY . .
RUN yarn install --production
CMD ["node", "/app/src/index.js"]
```

📄 DOCKERFILE
```conf
# escape=`    else error cause \ is treated as a line continuation
FROM microsoft/nanoserver
COPY testfile.txt c:\\
RUN dir c:\
```

📄 DOCKERFILE
```conf
ENV abc=hello           Environment variable
ENV abc=bye def=$abc
ENV ghi=$abc
FROM busybox
ENV FOO=/bar
WORKDIR ${FOO}   # WORKDIR /bar
ADD . $FOO       # ADD . /bar
COPY \$FOO /quux # COPY $FOO /quux
```


### DOCKERIZING Node.js
https://www.katacoda.com/courses/docker/3

📄 DOCKERFILE
```conf
# Base Image
FROM node:10-alpine

# Base directories of where the application runs from
RUN mkdir -p /src/app
WORKDIR /src/app

# Install the dependencies required to run the application
COPY package.json /src/app/package.json
RUN npm install

# Deploy Application
COPY . /src/app
# ports the application requires to be accessed 
EXPOSE 3000        

# start application, looks in the package.json file to know how to launch the application 
CMD ["npm", "start"]
```
Building and Launching Container
>docker build -t my-nodejs-app .                                   # build the image
>docker run -d --name my-running-app -p 3000:3000 my-nodejs-app    # launch the built image    
>curl http://docker:3000                                           # test the container

Environment variables. Using -e option, you can set name/value  
>docker run -d --name my-production-running-app -e NODE_ENV=production -p 3000:3000 my-nodejs-app

### GO

https://www.loginradius.com/blog/async/build-push-docker-images-golang/


### DOCKERIZING ASP.NET CORE
https://www.katacoda.com/courses/dotnet-in-docker/deploying-aspnet-core-as-docker-container

📄 DOCKERFILE
```conf
FROM microsoft/dotnet:1.1.1-sdk

RUN mkdir /app
WORKDIR /app

COPY dotnetapp.csproj .
RUN dotnet restore

RUN mkdir /app
WORKDIR /app

COPY dotnetapp.csproj .
RUN dotnet restore

COPY . .
RUN dotnet publish -c Release -o out

EXPOSE 5000/tcp
CMD ["dotnet", "out/dotnetapp.dll"]
```
>docker build -t aspnet-app:v0.1 .
>docker images | head -n2
>docker run -d -t -p 5000:5000 --name app aspnet-app:v0.1
>docker logs app     view the application logs
>curl http://localhost:5000


📄 DOCKERFILE
```conf
# Some docker hub container that is already suitable for unicorn
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app/app
COPY ./requirements.txt ./
# install dependencies (could also use the conda env) but it is more minimal
# we could probably find an image including this
RUN pip install --no-cache-dir -r requirements.txt
COPY ./test.py ./
COPY ./main.py ./
COPY ./model_weights/clf.bin ./model_weights/clf.bin
# do tests, usually better to do before building container, e.g. travis, circelci
RUN python -m test
```


📄 DOCKERFILE
build the image, tag it as v1
>docker build -t nodewebapp:v1 .
running a container with the interactive and detached mode and also exposing the port 3070 to the outside world
>docker run -it -d -p 3070:3070 nodewebapp:v1

```conf
FROM node:10

# set the work directory
WORKDIR /usr/src/app

# copy package.json
COPY package*.json ./

# copy webapp folder
COPY WebApp/package*.json ./WebApp/

# RUN npm install for node js dependencies
RUN npm install \
   && cd WebApp \
   && npm install @angular/cli \
   && npm install

# Bundle app source
COPY . .

# builing Angular UI
RUN cd WebApp && npm run build

EXPOSE 3070

ENTRYPOINT ["node"]
CMD ["index.js"]
```



## DOCKERIZING Docker on ec2 instance (Amazon Linux)
	
```conf    
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


### DOCKERIZING Github sample

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


## DOCKERIZING BLAZOR

- https://cloudblogs.microsoft.com/industry-blog/en-gb/cross-industry/2020/12/15/run-blazor-in-a-docker-container-with-visual-studio-code-remote-development/


## DOCKERIZING WORDPRESS

* php.ini
Create your own `Dockerfile` and `ADD php.ini /usr/local/etc/php`
Mount a volume with your php.ini at `/usr/local/etc/php`

php.ini
; Maximum allowed size for uploaded files.
; http://php.net/upload-max-filesize
upload_max_filesize = 2M

```conf
docker cp php.ini-development  84085df827d4:usr/local/etc/php
docker cp php.ini-production  84085df827d4:usr/local/etc/php
docker cp d56a9442ccd0:usr/local/etc/php/php.ini-development .    			
docker cp d56a9442ccd0:usr/local/etc/php/php.ini-production .    
docker cp d56a9442ccd0:usr/local/etc/php/php.ini-development temp\xxx.txt
```

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

- https://stackoverflow.com/questions/26598738/how-to-create-user-database-in-script-for-docker-postgres
- https://www.digitalocean.com/community/questions/copy-custom-wordpress-theme-with-docker-composer
- https://www.datanovia.com/en/lessons/wordpress-docker-setup-files-example-for-local-development/
- https://www.viralpatel.net/local-wordpress-docker/
- https://upcloud.com/community/tutorials/deploy-wordpress-with-docker-compose/
- https://joshmobley.net/writing/2017/04/09/easy-wordpress-migration-with-docker.html
- https://cntnr.io/setting-up-wordpress-with-docker-262571249d50


### REGULAR SCHEDULE
run a dotnet core console app that parses Reddit posts and posts itself, inside a Docker container, every 30 minutes on set days of the week.

- http://www.anotherchris.net/posts/running-cron-jobs-inside-a-docker-container

cron_task.sh
crontab
docker-cron-job-example
run_app.sh 		dotnet /app/MyApp.dll