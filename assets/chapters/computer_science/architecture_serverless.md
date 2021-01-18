# Serverless Architecture

Serverless or Function as a Service (FaaS) describes the idea that the deployment unit is a single function. A function takes input and returns output

## Serverless Manifesto
http://blog.rowanudell.com/the-serverless-compute-manifesto/

* Function are the unit of deployment and scaling.
* No machines, VMs, or containers visible in the programming model.
* Permanent storage lives elsewhere.
* Scales per request; Users cannot over- or under-provision capacity.
* Never pay for idle (no cold servers/containers or their costs).
* Implicitly fault-tolerant because functions can run anywhere.
* BYOC - Bring Your Own Code.
* Metrics and logging are a universal right.

AWS Lambda
Google Cloud Functions
https://webtask.io/
Firebase
Knative: open source, based on Kubernetes
https://github.com/anaibol/awesome-serverless