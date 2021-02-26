# PowerShell DSC

PowerShell Desired State Configuration
To manage IT and development infrastructure with configuration as code (declarative configuration)

***Configurations***
Declarative PowerShell scripts which define and configure instances of resources.
A special kind of PowerShell function

***Resources***
Contain the code that put and keep the target of a configuration in the specified state. 
PowerShell modules ("how" to execute a task) modeling something...
- generic: a file, a Windows process
- specific: an IIS server, an Azure VM

***LCM Local Configuration Manager***
Engine by which DSC facilitates the interaction between resources and configurations. LCM polls the system using the control flow implemented by resources to ensure that the state defined by a configuration is maintained. If the system is out of state, the LCM makes calls to the code in resources to "make it so" according to the configuration.

```bash
# Create a share in Windows Server 8
New-SmbShare -Name MyShare -Path C:\Demo\Temp -FullAccess Alice -ReadAccess Bob
```

```bash
# A configuration is a special kind of PowerShell function
Configuration Sample_Share
{
   Import-DscResource -Module xSmbShare
   # Nodes are the endpoint we wish to configure
   # A Configuration block can have zero or more Node blocks
   Node $NodeName
   {
      # Next, specify one or more resource blocks
      # Resources are simply PowerShell modules that
      # implement the logic of "how" to execute a task
      xSmbShare MySMBShare
      {
          Ensure      = "Present"
          Name        = "MyShare"
          Path        = "C:\Demo\Temp"
          ReadAccess  = "Bob"
          FullAccess  = "Alice"
          Description = "This is an updated description for this share"
      }
   }
}
#Run the function to compile the configuration
Sample_Share
#Pass the configuration to the nodes we defined and configure them
Start-DscConfiguration Sample_Share
```

## More