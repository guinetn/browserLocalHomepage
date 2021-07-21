# AWS

https://aws.amazon.com
https://devopsmyway.com
https://devopsmyway.com/list-of-aws-services/
https://static.coggle.it/diagram/XhbybXDSoKh9k_fr/t/amazon-web-services



- https://aws.amazon.com/fr/products/

- Tutorials by https://github.com/jacksonyuan-yt
- [AWS + lambda + ci/cd](https://www.youtube.com/watch?v=mWtnd-0Sm18)
 A lambda handler that uploads a file to an S3 bucket based on an API Gateway trigger.
    * Setting up the IAM User
    * Setting up the CI/CD pipeline w/ GitHub Actions
    * Setting up & Deploying the AWS S3 Bucket
    * Verifying the bucket deployment

    - Serverless Framework: https://www.serverless.com/
    - GitHub Actions: https://github.com/features/actions
    - src: https://github.com/jacksonyuan-yt/s3-file-upload-api

- [AWS SERVICES - fireship ★★★](https://www.youtube.com/watch?v=JIbIYCM48to&t=174s)
 calcul
 stockage
 bases de données
 analyse
 mise en réseau
 services mobiles
 outils de développement
 outils de gestion
 Internet des Objets
 sécurité
 applications d'entreprise

* AWS Origin: 2006 STORAGE, COMPUTE, MESSAGING
* RoboMaker: simulate robots
* IoT Core: get data
* Ground Station: connect to your satellites

GOMPUTE
* Braket: interact with Quantum Computing
* EC2: Elastic Compute Cloud, virtual computer in the cloud, typically instance = web app
* Load Balancer: zpp grows, distribute traffic to multiples instances automatically
* Cloud Watch: collect logs and metrics from instances
* Auto Scale: polcies that from logs can create new instances needed based on the traffic
* Beanstalk: easier that above, ec2+autoscale, paas
* Lightsail: more easier that above
* Lambda: even need a server? FAAS, serverless. upload your code and choose an event that code should run
* Serverless Repos: templates for lambda, pre-built function
* Outposts: run aws on your own infrastructure without throwing your old servers
* Snow: interact with aws from remote extreme environments (arctic...). snow devices = mini data centers working without internet in hotile environments

* ECR: elastic container registry. Many app are standardized with docker containers to run on multiple clouds/env. Create a docker image and store it somewhere
* ECS: elastic  container service will use image from ECR; starting, stopping, allocating vm to ypur containers and connect to products like load balancers
* EKS: kubernetes service. more control on how apps scale
* Fargate: containers behave in a more automated way. make containers ~ serverless functions removing ec2 instances need
* App Runner: point to a containerized image and it handle all the orchestration and scaling behind the scene

STORAGE
* S3: Simple sotrage service: store data in the cloud. store any file (img, video), objects
* Glacier: s3 with low latency, for files not often used, lower cost
* Block Storage: fast storage, lot of throughput. apps with intensive data process requirements (but need more manual config)
* EFS: Elastic File System, high perf, fully managed (no config), moez expensive

DATABASE - store structured data
* SimpleDB: nosql database
* DynamoDB: nosql document database that scale horizontally easily. fast read, inexpensive but limited in modeling relational data. 
* DocumentDB: ~mongodb
* ElasticSearch: full text search engine
* RDS: Relational Database Service. Traditional sql. Support sql flavors (mysql, sqlserver, mariadb, oracle...). Backups, patching, scale
* Aurora: amazon 'mysql', great perf at lower cost. serverless (pay as use)
* Neptune: graph database for highly connected datasets (social graphs, recommendations)
* ElasticCache: to be fast, this use a fully managed redis (in memory db). fast read
* TimeStream: for time series data (stock market). A time serie db + buil-in function for time-based queries and analytics features
* QLDB: Quantum ledger db, to make immutable set of cryptographically signed transactions ~ decentralized blockchain

ANALYTICS: to analyze data
* Redshift: store data in warehouse
* Lake Formation: store large amount of unstructured data
* Kinesis: capture real-time streams to analyze real time data
* EMR: Elastic map reduce service that operate on massive datasets, parallel distributed algorithm (spark: stream processing framework)
kafka
flume           → Spark streaming → HDFS, Database, Dashboard
hdfss3
Kinesistwitter
* MSK: kafka (open source)

AUTOMATIC
* Glue:  serverless ETL, automatic connect to aurora, s3, redshift... Glue Studio = create jobs

MACHINE LEARNING
* Data Exchange: 3rd party data sources
* Sagemaker: build ml model with TF, pi torch
* Rekognition: image recognition, classify objects
* Lex : conversational bot (idem alexa)
I'd like to book a hotel
  sure, wich city
New york
    What date are you leaving?
November 20th, 2021
    Are you sure to book the hotel in NYC?
Yes
    Thank you, The reservation went through successfully
* Deep Racer: actual race car you can drive with your own ML code

DEVELOPER ESSENTIALS
* IAM: identity and access management: create rules on who can access what
* Cognito: to have few users logged, it manages auth methods, user sessions for our web, mobile app

Notifications
* SNS: simple notification service, send oush notifications
* SES: simple email service, to send emails to your users 

* CloudFormation: create yaml/json template of our infrastructure to enable services by a click
* Amplify: connect services above with your frontend sks (react, vue, js...)
* Budget: costs explorer










## AWS TRAINING

https://www.youtube.com/watch?v=yPHt0slwMVQ

00:02:54​ = Overview Cloud Computing
00:13:55​ = Introduction to AWS
00:18:49​ = Global Infrastructure
00:26:28​ = AWS Services
00:36:29​ = IAM Services
00:47:20​ = Compute Services
00:55:20​ = Storage Services
01:02:46​ = Network Services
01:11:18​ = Database Services
01:17:54​ = Automation & Configuration Management
01:24:12​ = Audit & Monitoring
01:28:43​ = SNS, SES, SQS, SWF Application Services
01:38:04​ = DevOps Tools
01:46:48​ = AWS Architecture
01:52:12​ = Access Services
01:53:50​ = AWS : Create a Free Cloud Account
02:34:45​ = Reset Password for Windows in EC2
02:41:00​ = Configure Web Server (IIS) on EC2
03:18:40​ = How to use AWS CLI
03:41:40​ = Learning path for AWS certified Solution Architect Asscociate [SAA-C02]
03:42:38​ = Free Training on Amazon AWS Solution Architect Certification for Beginners
03:42:56​ = Registration Link for AWS Solution Architect Certification for Beginners
03:42:59​ = Learning path for AWS certified DevOps Engineering Professional [DOP-C01]
03:44:02​ = Free Training on AWS DevOps Certification for Beginners
03:44:17​ = Registration Link for AWS DevOps Certification for Beginners




2006
>Amazon Web Services (AWS) began offering IT infrastructure services to businesses in the form of web services—now commonly known as cloud computing. One of the key benefits of cloud computing is the opportunity to replace up-front capital infrastructure expenses with low variable costs that scale with your business. With the cloud, businesses no longer need to plan for and procure servers and other IT infrastructure weeks or months in advance. Instead, they can instantly spin up hundreds or thousands of servers in minutes and deliver results faster.

175 services complets issus de centres de données du monde entier. Des millions de clients dont certaines des startups les plus dynamiques au monde, de très grandes entreprises et des agences fédérales de premier plan utilisent AWS pour réduire leurs coûts, gagner en agilité et innover plus rapidement. »

2 main products
- EC2: Amazon’s virtual machine service
- S3: Amazon’s storage system. 

Furthermore, some of the major services AWS provides include Amazon Cloud Front, Amazon Elastic Compute Cloud (EC2), Amazon Relational Database Service (Amazon RDS), Amazon Simple Notification Service (Amazon SNS), Amazon Simple Queue Service (Amazon SQS), Amazon Simple Storage Service (Amazon S3), Amazon SimpleDB, and Amazon Virtual Private Cloud (Amazon VPC).
AWS regroupe une centaine de services répartis en diverses catégories telles que le 
stockage cloud
puissance de calcul
analyse de données
intelligence artificielle
développement de jeux vidéo

populaires
Amazon Elastic Compute Cloud (EC2) - un service permettant à des tiers de louer des serveurs sur lesquels exécuter leurs propres applications web
Amazon Simple Storage Service (S3) - un service d'hébergement de fichiers qui propose du stockage à travers des services Web (REST, SOAP et BitTorrent) -.


EC2, RDS, S3, ECS, ELB

|Concepts| Meaning | |
|---|---|
|Image  | An image is a complete copy of a hard disk that includes the operating system and a lot of installed software. Server comes alive With this disk. |
|Firewall  | It acts like a filter on either source or target IP addresses or target port numbers. |
|PEM file  | PEM encoded RSA private key is a format that stores an RSA private key for SSH connection. |
|chmod 400  | SSH will not allow connections until the key file has been made read-only. |
|EC2  | An Amazon Elastic Compute 2 instance is a virtual server in the AWS cloud. |
|Instance  | An instance on AWS is just a virtual machine. |

https://medium.com/adamedelwiess/data-acquisition-7-an-introduction-to-the-amazon-web-services-e927c68132cb

Amazon Services
- S3: hosting for the React.JS application
- CloudFront: content delivery network
- Route53: domain management service
- Amazon Certificate Manager (ACM): certification provision for our domains

## Free tier t2.micro instance
Play with a micro instance for 12 months. Simply create a new account on http://aws.amazon.com/, and create a new t2.micro instance. 

https://www.hackingnote.com/en/cloud/aws
https://aws.amazon.com/fr/free

## AZ - Availability Zone
One or more discrete Data Centers in an AWS Region with redundant power, networking, and connectivity.
The no of AZs may varies from 2 to 5 in different AWS Regions.
Good practice to distribute your web/applications/databases in multiple subnets in multiple AZs. In case , one AZ goes down due to power outage, lightning, earthquake etc, your application will be still running in another AZ.

## Elastic IP

Elastic IP address is a Public IP(IPv4) address provided by AWS Cloud and this Public IP address is static and easily attachable and de-attachable to any instance. You can attach or de-attach an Elastic IP any time(without shutting down the instance) and,  to any Instance as per your requirement.Due to this flexible behavior, AWS named this IP address as Elastic IP.

## WS Nitro System
Offload network, storage and management to dedicated hardware, so CPU can be used for more important computing jobs. Thanks to the ASIC(Application-specific integrated circuit) from Annapurna Labs, a company that Amazon acquired.
Nitro Hypervisor: built on KVM, but does not include general purpose operating system components.

## [CloudShell](https://aws.amazon.com/fr/cloudshell)
browser-based shell that makes it easy to securely manage, explore, and interact with your AWS resources
Bash, Python, Node.js, PowerShell, VIM, git...  outils de ligne de commande et scripts directement dans la console AWS (Déjà présent sur Azure=interpréteur bash et powershell dans le navigateur et Google)

## Amazon EMR - Amazon Elastic MapReduce  

https://itnext.io/running-spark-jobs-on-amazon-emr-with-apache-airflow-2e16647fea0c
Cloud-based big data platform for processing vast amounts of data using common open-source tools such as Apache Spark, Hive, HBase, Flink, Hudi, and Zeppelin, Jupyter, and Presto. 


## DynamoDB
https://aws.amazon.com/dynamodb/

## SNS - Simple Notification Service 

## SAM - AWS Serverless Application Model
set up serverless applications on AWS  
https://aws.amazon.com/serverless/sam/

## AWS FARGATE
AWS Fargate est un moteur de calcul sans serveur pour les conteneurs. Il fonctionne avec Amazon Elastic Container Service (ECS) et Amazon Elastic Kubernetes Service (EKS). 
Fargate vous aide à vous concentrer sur la création de vos applications. Ce service évite d’avoir à provisionner et gérer des serveurs, permet de spécifier et payer pour les ressources en fonction des applications et améliore la sécurité grâce à une isolation intégrée de l’application

https://aws.amazon.com/fr/fargate
https://medium.com/@tribasukikurniawan/deploy-docker-container-as-serverless-architecture-to-aws-fargate-1121bafa1d8c

## SAGEMAKER

https://venturebeat.com/2020/06/27/a-closer-look-at-sagemaker-studio-aws-machine-learning-ide

for orchestrating robotics workflows (from perception to controls and optimization, and to create end-to-end solutions)


## microservices


## Deploying a .NET Core 3.1 App to AWS Beanstalk

|||
|---|---| 
|Creating the deployment package|dotnet publish -o my-app|
||Compress the newly created my-app folder to a zip archive. This will be our deployment package|
|Deploying the package||
|Visit the AWS Elastic Beanstalk Console|https://console.aws.amazon.com/elasticbeanstalk|
||Go ahead and Create Application: give a name, select platform|
||Set Application Code to Upload your code<br/>Upload deployment package by hand: press 'Choose file', select .zip file|
||Create Application.<br/>wait a few minutes for the deployment to complete|


## IaC
https://aws.amazon.com/fr/cloudformation/


## Configuring AWS

Required permissions: AWS S3
s3:ListAllMyBuckets
s3:GetObject
s3:PutObject
s3:PutObjectAcl
s3:DeleteObject
s3:ListBucket
Required permissions: CloudFront
cloudfront:ListDistributions
cloudfront:CreateInvalidation

https://buddy.works/guides/reactjs-to-aws

A. AWS S3
1. Create a bucket with desired names for your production and staging deployments.
2. configure your S3 bucket for Static Website Hosting
https://docs.aws.amazon.com/AmazonS3/latest/user-guide/static-website-hosting.html

B. Route 53 and CloudFront
1. Create and configure a Route 53 hosted zone with your domain name that we'll use to route DNS traffic to your website bucket (you can also do this on your DNS provider e.g. GoDaddy). 
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/RoutingToS3Bucket.html
2. Next step is setting up Amazon CloudFront to speed up the distribution of your static content (such as HTML, CSS, JS, and image files) to your users. There's a separate guide on distributing traffic from Amazon S3 with CloudFront, too.
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins.html#adding-cloudfront-to-s3

C. Creating Staging pipeline
Log in to Buddy. Select GitHub repository. Click "Add a new pipeline"
Force Buddy to trigger the execution on every change to the development code
- Set trigger mode to 'On push'
- Set branch to 'develop'. 
- Build and Deploy Sample React Frontend to AWS S3 and CloudFront"

Preparing environment


## AWS Cloud9
    
https://aws.amazon.com/fr/cloud9/

a cloud-based integrated development environment (IDE) that lets developers write, run and debug code with just a browser, providing a code editor, debugger and terminal. It comes with essential tools for popular programming languages such as JavaScript, Python, PHP and more, so devs don't need to install files or configure a development machine to start new projects.

With AWS Cloud9, you start with an environment pre-packaged with essential tools for popular programming languages, coupled with the power of Amazon EC2

advantage of AWS Cloud9's built-in auto-shutdown capability which powers off your instance when you're not actively connected to it.

##### ARTICLES

- https://www.freecodecamp.org/news/author/david/
- [react on aws + buddy ci/cd](https://buddy.works/guides/reactjs-to-aws)
- [node-js-to-display-images-in-a-private-aws-s3-bucket](https://medium.com/javascript-in-plain-english/using-node-js-to-display-images-in-a-private-aws-s3-bucket-4c043ed5c5d0)
- https://developer.okta.com/blog/2019/04/16/graphql-api-with-aspnetcore
- https://developer.okta.com/blog/2019/03/21/build-secure-microservices-with-aspnet-core

- https://www.scarydba.com/2020/08/10/my-first-hand-built-aws-codepipeline/
- https://medium.com/@adhasmana/how-to-quickly-deploy-react-and-node-app-on-aws-80e5dfe7d86e
https://dev.to/edwardmercado/build-a-modern-web-application-3o4f

- [GitHub Codespaces Alternative: AWS Cloud9, SSH & VS Code](https://visualstudiomagazine.com/articles/2021/07/01/aws-vscode.aspx?oly_enc_id=3671F4217256E2X)