# ElasticSearch

NoSQL 
Column oriented
Index text documents (text, json...) ~ parametrizable search engine
Real time search 
Use Lucene search engine for requests
[Lucene](https://lucene.apache.org)
    OpenSource Apache search engine for your website

Search Engine = relevance, given by calculating a score per document
document → count words, frequency => weight → score = f(vector, sinus) 

Elastic Search
1. Get the ElasticSearch up and running
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --name myES docker.elastic.co/elasticsearch/elasticsearch:7.4.1
2. Check if our container is up and running
curl -X GET "localhost:9200/_cat/nodes?v&pretty"
## More

- https://openclassrooms.com/fr/courses/4462426-maitrisez-les-bases-de-donnees-nosql/4474691-etudiez-le-fonctionnement-d-elasticsearch
- https://blog.bitsrc.io/setting-up-a-logging-infrastructure-in-nodejs-ec34898e677e