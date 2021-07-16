## AUTOSCALING

[autoscaling + stress ★★★](https://www.red-gate.com/simple-talk/cloud/azure/autoscaling-in-microsoft-azure)
    Ability to scale up and down without maintaining extra hardware is one of the best cloud computing features
    Essential cloud feature to ensure that your application is always ON and available for customers
    AWS: “AutoScalingGroup (ASG)”
    Azure: “Virtual Machine Scale Set (VMSS)”
    Google Cloud: “Managed Instance Groups (MIG)”
    Autoscaling = run application or workload with the required resources (vm) without interruption. Autoscaling replaces those faulty virtual machines with new ones
    * Time-Based Autoscaling: based on the scheduled time (weekend...Development environments from 9am-17pm) ~ cron jobs that automatically create/shut down the instances when they are not needed
    * Metrics-Based Autoscaling: based on the key performance metrics of your resource like CPU, Memory, Thread Count... For Web servers that are CPU intensive


- https://www.red-gate.com/simple-talk/cloud/azure/autoscaling-in-microsoft-azure

Creating a resource group called 'autoscalingrg' in the us-west region before creating other resources
> az group create --location westus --name autoscalingrg --subscription [your subscription id]
create the virtual machine scale set with one RHEL virtual machine under the resource group
> az vmss create --resource-group autoscalingrg --name timebasedvmss --image RHEL --upgrade-policy-mode automatic --instance-count 1 --admin-username maheadmin --generate-ssh-keys
view the virtual machine scale set details (or through the Azure portal)
> az vmss list --resource-group autoscalingrg

a. Timed-Based Autoscaling

Create the default autoscale profile and attach it to the virtual machine scale set
> az monitor autoscale create --count 1 --max-count 2 --min-count 1 --name timebasedasg --resource timebasedvmss --resource-group autoscalingrg --resource-type Microsoft.Compute/virtualMachineScaleSets
Create one autoscaling profile to scale out and another one to scale in the virtual machine scale set based on a time schedule. 
I am scaling out the VMSS every day at 12:25 PM PST and scaling in every day at 12:40 PM PST. 
This means that the virtual machine scale set scales from one instance into two instances every day between 12:25 and 12:40 PM PT. 
The reason to create two profiles is that the recurrence profile only has the start time. 
Even though you specify the end time, it is not used in the recurrence profile. 
Feel free to modify the times so that you can see the autoscaling actions more quickly. Verify these settings through the Azure Portal
> az monitor autoscale profile create --resource-group autoscalingrg --autoscale-name timebasedasg --count 2 --name daily-scaleout --recurrence week sat sun mon tue wed thu fri --timezone "Pacific Standard Time" --start 12:25 --end 12:35
> az monitor autoscale profile create --resource-group autoscalingrg --autoscale-name timebasedasg --count 1 --name daily-scalein --recurrence week sat sun mon tue wed thu fri --timezone "Pacific Standard Time" --start 12:40 --end 12:45

List the instances after scale-out and scale-in
> az vmss list-instances --resource-group autoscalingrg --name timebasedvmss | grep name

> az monitor autoscale delete --resource-group autoscalingrg --name timebasedasg

b. Metrics-Based Autoscaling
Scale the virtual machine scale set based on the virtual machine’s average CPU utilization

created the new metric based autoscaling setting called “metricbasedasg”
> az monitor autoscale create --resource-group autoscalingrg --name metricbasedasg --count 1 --max-count 4 --min-count 1 --resource timebasedvmss --resource-type Microsoft.Compute/virtualMachineScaleSets

create the scaling rules to scale out and scale in the virtual machine scale sets.
Az portal: enable inbound NAT rule on port 50000
- Scale-out rule – when the average CPU utilization goes above 75% for 5 minutes, scale out the stack to 2 instances.
- Scale-in rule – when the average CPU utilization goes below 40% for 5 minutes, scale in the stack by 1 instance.
> az monitor autoscale rule create --resource-group autoscalingrg --autoscale-name metricbasedasg --scale out 2 --condition "Percentage CPU > 75 avg 5m"
> az monitor autoscale rule create --resource-group autoscalingrg --autoscale-name metricbasedasg --scale in 1 --condition "Percentage CPU < 40 avg 5m"

> az vmss list --resource-group autoscalingrg

Test the autoscaling activity with some process to trigger the CPU spike 
ssh into the virtual machine
> ssh maheadmin@13.91.17.65 -p 50000
* Install the stress utility and run it.
> wget <a href="https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/s/stress-1.0.4-16.el7.x86_64.rpm">https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/s/stress-1.0.4-16.el7.x86_64.rpm</a>
> sudo yum install stress-1.0.4-16.el7.x86_64.rpm
> stress -c 2
CPU getting spiked to around 100%... autoscaling rule scaled out the stack from 1 instance to 3 instances
Once you execute the stress command, you can check the CPU utilization of the virtual machine either using the “top” command on the instance or through the Azure Portal

