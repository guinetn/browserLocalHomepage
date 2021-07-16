## Serverless Functions in azure

VSCode Azure Functions Extension: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions

easy to get a basic API/microservice up and running quickly!
set-up an API endpoint using the HTTP Trigger invocation that you can use with any front-end site

* Azure Function HTTP trigger
- To build serverless APIs and respond to webhooks
- Invoke a function with an HTTP request/webhooks
- JavaScript, Python, C#, F#, Java

- Az login
- Create a resource
- Function App
- Once it has successfully been deployed, click Go to resource to view your new function app.
Click the + sign next to Functions on the left-hand side menu
select New Function 
Click Create: base function is generated with some default code

* Secure your Serverless HTTP Trigger by Adding Identity Management

Go to your function and select Integrate underneath it. Uncheck the POST checkbox, change the Authorization Level to Anonymous (users will not be prompted to log) and click Save.

* Azure Functions

Azure Functions can run in a serverless mode, which means that you only pay for the virtual machine executing the scheduled task as long as it is running. Azure Functions is a great and cheap way to implement scheduled tasks if you are already on Azure.

```C#
// Azure Function scheduled to run hourly
public class MyScheduledFunction
{
    [FunctionName("MyScheduledFunction")]
    public async Task Run([TimerTrigger("0 0 * * * *")]TimerInfo myTimer)
    {
        // Add your scheduled code here
        
        return Task.CompletedTask;
    }
}
```

## Devops: automate building and deployment

Azure DevOps Project simplifies the setup of an entire continuous integration (CI) and continuous delivery (CD) pipeline to Azure  
Deploy to Azure services
- Virtual Machines
- App Service
- Azure Kubernetes Services (AKS)
- Azure SQL Database
- Azure Service Fabric

DevOps Projects does all the work to configure of a DevOps pipeline
- setting up initial Git repository
- configuring the CI/CD pipeline
- creating an Application Insights resource for monitoring
- providing a single solution's view with the creation of a DevOps Projects dashboard in the Azure portal
