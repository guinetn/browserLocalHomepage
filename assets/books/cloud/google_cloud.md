# GCP - Google Cloud Platform

https://cloud.google.com/
https://cloud.google.com/sdk
[Google Cloud Developer's Cheat Sheet](https://github.com/gregsramblings/google-cloud-4-words)

hébergement sur la même infrastructure que celle que Google utilise en interne pour des produits tels que son moteur de recherche

Google App Engine
une plateforme en tant que service pour tester des applications dans un bac à sable. App Engine offre du changement d'échelle automatique, augmentant les ressources pour faire face à la charge du serveur.

Google Compute Engine
le composant infrastructure en tant que service de la Google Cloud Platform permettant aux utilisateurs de lancer des machines virtuelles (VMs) à la demande.

Google Kubernetes Engine
une version commerciale de Kubernetes, un logiciel open source de gestion de conteneurs.

Google Cloud Storage
un système de stockage en ligne de fichiers.

Google BigQuery
un entrepôt de données à très grande échelle basé sur Dremel.

Plusieurs API de haut niveau

## GCP - Google Cloud Platform
- https://console.cloud.google.com/
- https://towardsdatascience.com/bioinformatics-on-the-cloud-144c4e7b60d1
- https://github.com/DataBiosphere/dsub

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