### Route Table

Every VPC has an implicit Router and that router use route table to control network traffic or directs the traffic to a destination.
You can associate the Route Table with an Internet Gateway or Nat Gateway for Internet access.

Windows
>netstat -r
>netsh interface ipv4 show route
>netsh interface ipv6 show route

Linux
>ip route
>netstat -r
