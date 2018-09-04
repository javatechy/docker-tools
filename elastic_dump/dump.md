
```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.4

docker run --name elasticsearch  -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -v elasticsearch-data:/usr/share/elasticsearch docker.elastic.co/elasticsearch/elasticsearch:6.2.4

docker run --name elasticsearch  -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -v elasticsearch-data_1:/usr/share/elasticsearch javatechy/elast_dump:1.1 
docker exec elasticsearch sh devexport SOURCE_IP:9200 user-index


docker exec elasticsearch sh devexport 35.154.206.110:9200 user-index

docker push XXXX.dkr.ecr.ap-south-1.amazonaws.com/openjdk-8-slim

```

### To dump 2.4 version, use

```
docker run --name elasticsearch  -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -v elasticsearch-data:/usr/share/elasticsearch elasticsearch:2.4

```

Note : To copy nodes data from your local to ES use docker cp command.



# Links :

- https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

- https://www.npmjs.com/package/elasticdump

- https://stackoverflow.com/questions/26547560/how-to-move-elasticsearch-data-from-one-server-to-another
