# DOCKERFILE

Docker images can be automatically built from text files, named Dockerfiles. A Docker file contains step-by-step ordered instructions or commands used to create and configure a Docker image.

- Named `Dockerfile` by default, in the root of the context
- Text instructions to assemble an image (add packages, copy files...)
- Commands a user could call on the command line 
- The Docker daemon runs the instructions in the Dockerfile
- https://docs.docker.com/engine/reference/builder



📄 DOCKERFILE
```conf
FROM node:12-alpine                    pull the base image from which you are building the new image
WORKDIR /app                   
COPY . .
RUN yarn install --production          Runs any commands after a Docker image has been created. Many Run...can exists
CMD ["node", "/app/src/index.js"]      Run a command when the Docker image is started. Only one CMD can exists
```
Creating the image
>docker build -t node .
>docker build -t mycontainername /var/docker/ubuntu/apache/


## DOCKERFILE COMMANDS

```conf
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

RUN
    can be used on multiple lines and runs any commands after a Docker image has been created.
RUN <command> (shell form, the command is run in a shell, which by default is /bin/sh -c on Linux or cmd /S /C on Windows)
RUN ["executable", "param1", "param2"] (exec form, parsed as a JSON array so use "" not '')     

Using the RUN <command> we can execute commands as if they are running from a command shell
RUN mkdir -p /src/app
Define a working directory using WORKDIR <directory> to ensure that all future commands are executed from the directory relative to our application.

RUN echo 'we are running some # of cool things'
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y ...
RUN ["c:\\windows\\system32\\tasklist.exe"]
RUN /bin/bash -c 'source $HOME/.bashrc; echo $HOME'
RUN ["/bin/bash", "-c", "echo hello"]    use a shell,other than '/bin/sh'
CMD ["executable","param1","param2"] (exec form, this is the preferred form)
CMD ["param1","param2"] (as default parameters to ENTRYPOINT)
CMD command param1 param2 (shell form)
CMD ["npm", "start"]

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

CMD
    Run any command when the Docker image is started. Use only one CMD instruction in a Dockerfile.

COPY
    copies new files or directories from <src> 
    and adds them to the filesystem of the container at the path <dest>
    COPY [--chown=<user>:<group>] <src>... <dest>   
    COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
    COPY hom?.txt /mydir/
    COPY hom* /mydir/

ENV <key>=<value> ...
    Set container environment variables. Persist if container is run from the resulting image
    ENV MY_NAME="John Doe"
    docker inspect     
    docker run --env <key>=<value>

ENTRYPOINT
    configure a container that will run as an executable
    Same as CMD but used as the main command for the image.
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
    container listen on the specified network ports at runtime
    Instructs the container to listen on network ports when running. The container ports are not reachable from the host by default.
    EXPOSE 80/tcp
    EXPOSE 80/udp
    docker run -p 80:80/tcp -p 80:80/udp ...

FROM
    Instructs Docker to pull the base image from which you are building the new image

LABEL
    key-value pair that adds metadata to an image
    LABEL version="1.0"
    docker image inspect --format='' myimage

MAINTAINER
    Author of the build image

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
    ensure that all future commands are executed (ie RUN mkdir -p /src/app) from the directory relative to our application.
    WORKDIR /a
    WORKDIR b
    WORKDIR c
    RUN pwd

ONBUILD
    adds to the image a trigger instruction to be executed at a later time, when the image is used as the base for another build
    ONBUILD ADD . /app/src
    ONBUILD RUN /usr/local/bin/python-build --dir /app/src
```

```conf
# escape=`    else error cause \ is treated as a line continuation
FROM microsoft/nanoserver
COPY testfile.txt c:\\
RUN dir c:\
```

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

* .dockerignore
```conf
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
