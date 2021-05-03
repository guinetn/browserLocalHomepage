# Kibana

https://www.elastic.co/products/kibana

Real time `DATA VISUALISATION` dashboard
Open source from Elastic company
Elasticsearch web project service
Need a ElasticSearch cluster to store data

To work: 
- Elasticsearch base localisation
- way of presenting data 

    Logs
        ↓ unstructured data
    Logstash (ETL) / Beats (agents) 
        ↓
    ElasticSearch index
        ↓    
    Users can do search in index
        ↓
    dashboard 

- Discover
- Visualize
- Dashboard
- Timelion
- Dev Tools
- Management

1. Get our Kibana up and running
docker run —-link myES:elasticsearch -p 5601:5601 kibana:7.4.
Note: linking our kibana and elastic search server using the --link
2. http://localhost:5601/app/kibana

## More 

- https://openclassrooms.com/fr/courses/4462426-maitrisez-les-bases-de-donnees-nosql/4686486-visualisez-et-prototypez-avec-kibana