# AWS

https://aws.amazon.com
https://devopsmyway.com
https://devopsmyway.com/list-of-aws-services/

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

##### ARTICLES

- https://www.freecodecamp.org/news/author/david/
- [node-js-to-display-images-in-a-private-aws-s3-bucket](https://medium.com/javascript-in-plain-english/using-node-js-to-display-images-in-a-private-aws-s3-bucket-4c043ed5c5d0)
- https://developer.okta.com/blog/2019/04/16/graphql-api-with-aspnetcore
- https://developer.okta.com/blog/2019/03/21/build-secure-microservices-with-aspnet-core

