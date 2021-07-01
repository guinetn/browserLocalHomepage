# NGINX

https://www.nginx.com/

a server
a load balancer
a proxy

sudo apt-get update
sudo apt-get install nginx

/etc/nginx/sites-available/default/nginx.conf
```yaml
upstream httpservers {
   server ip_address:8001; 
   server ip_address:8002; 
   server ip_address:8003; 
}
server {
   listen 80; 

   location / {
      proxy_pass http://httpservers;
   }
}
```


openssl req -x509 -newkey rsa:2048 -nodes -sha256 -subj '/CN=localhost' \
  -keyout localhost-privatekey.pem -out localhost-certificate.pem
  
```
upstream grpcnodes {
    server ip_address:8001;
    server ip_address:8002;
    server ip_address:8003;
}
server {

    listen 1443 http2;
	  ssl_certificate /home/ubuntu/interserviceCommunication/http2/certificates/localhost-certificate.pem;
          ssl_certificate_key /home/ubuntu/interserviceCommunication/http2/certificates/localhost-privatekey.pem;

	  location / {
                grpc_pass grpcnodes;
    ## try_files $uri $uri/ =404; // Don't forget to comment this else you will get 404 as a response
	}  
```
    
## NGINX Plus    
Based on NGINX Open Source, NGINX Plus is the only software 
- load balancer
- reverse proxy
- API gateway

gRPC health checks
Actively testing that a gRPC service can handle requests before sending them significantly boosts reliability. When deployed as a load balancer, NGINX Plus can monitor the health of backend (upstream) servers by making active health checks. NGINX Plus R23 supports the gRPC health checking protocol, enabling it to accurately test whether backend gRPC servers are able to handle new requests. This is particularly valuable in dynamic and containerized environments. When spinning up new instances of a gRPC service, it’s important to send requests only once the service is “fully up”. This requires a health check that goes deeper than looking at the TCP port or verifying HTTP URI availability – one where the service itself indicates whether it’s ready to receive requests.

Unprivileged installation support
NGINX Plus can now be installed by, and upgraded as, an unprivileged (non‑root) user. This fully supported solution aligns with the growing trend toward zero‑trust security models.

OpenID Connect PKCE support
NGINX Plus R23 implements the Proof Key for Code Exchange (PKCE) extension to the OpenID Connect Authorization Code flow. PKCE prevents several types of attack and enables secure OAuth exchanges with public clients.