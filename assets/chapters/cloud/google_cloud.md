# GOOGLE CLOUD

https://cloud.google.com/
https://cloud.google.com/sdk

## GCP - Google Cloud Platform

## GCP data processing/analytics products

### Cloud Dataproc
Google's internal Flume (Flume and Spark = next generation Hadoop/MapReduce)
### Cloud DataFlow
large scale data processing 

## API Gateway
a replacement for Cloud Endpoint
API Gateway reduces the complexity of deploying and managing APIs, and it is comparable to Amazon API Gateway and Azure API Management

## GCP serverless products
### App Engine (2008)
PaaS 
Serverless

### Cloud Functions (2016)
Functions as a Service
Serverless

### Cloud Run (2019)
Code is packaged into standard Docker containers
Knative (open source) under the hood
    https://knative.dev/
    Kubernetes-based platform to deploy and manage modern serverless workloads.
    Serverless users are afraid of vendor lock-in, so Knative is created to make serverless standardized and portable.
    Google Cloud Run is a re-implementation of the same Knative Serving API.


# Deploying a .NET Core 3.1 App to Google App Engine
|||
|---|---|
|https://console.cloud.google.com|welcome screen<br/>select Create Application<br/>Choose any Region<br/>Add .NET as Language<br/>Set 'Flexible' as Environment|
|dotnet publish -o my-app|Open a terminal in project folder<br/>cd my-app|
|gcloud init|Log in Cloud SDK|
|gcloud app deploy|Deploy the application<br/>Go back to the Cloud Platform Console and click the service to see it working|
|||
|||
|||


### NO CODE APPS

- https://www.blog.google/products/google-cloud/learn-to-create-software-applications-no-experience-needed

- https://community.appsheet.com/