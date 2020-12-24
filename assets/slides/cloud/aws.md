# AWS

|Concepts| Meaning | |
|---|---|
|Image  | An image is a complete copy of a hard disk that includes the operating system and a lot of installed software. Server comes alive With this disk. |
|Firewall  | It acts like a filter on either source or target IP addresses or target port numbers. |
|PEM file  | PEM encoded RSA private key is a format that stores an RSA private key for SSH connection. |
|chmod 400  | SSH will not allow connections until the key file has been made read-only. |
|EC2  | An Amazon Elastic Compute 2 instance is a virtual server in the AWS cloud. |
|Instance  | An instance on AWS is just a virtual machine. |

https://medium.com/adamedelwiess/data-acquisition-7-an-introduction-to-the-amazon-web-services-e927c68132cb

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




## Deploying a .NET Core 3.1 App to AWS Beanstalk

Creating the deployment package
|||
|---|---|
|dotnet publish -o my-app||
||Compress the newly created my-app folder to a zip archive. This will be our deployment package|
|Deploying the package||
||Visit the AWS Elastic Beanstalk Console|
||Go ahead and Create Application: name, select platform|
||Upload deployment package by hand: press 'Choose file', select .zip file|
||Create Application|

##### ARTICLES

- [node-js-to-display-images-in-a-private-aws-s3-bucket](https://medium.com/javascript-in-plain-english/using-node-js-to-display-images-in-a-private-aws-s3-bucket-4c043ed5c5d0)