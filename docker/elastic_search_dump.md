# Remove Docker Volumes

```
docker volume prune
docker volume rm Remove one or more volumes

docker run --rm --volumes-from metabase-data -v $(pwd):/backup metabase tar cvf /backup/backup.tar /metabasedata
```



#  Install Docker on ubuntu

- https://docs.docker.com/install/linux/docker-ce/ubuntu/#upgrade-docker-after-using-the-convenience-script


# Backup : 

https://github.com/loomchild/volume-backup


```

docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.4

docker run --name elasticsearch  -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -v elasticsearch-data:/usr/share/elasticsearch docker.elastic.co/elasticsearch/elasticsearch:6.2.4

docker run --name elasticsearch  -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -v elasticsearch-data_1:/usr/share/elasticsearch javatechy/elasticseach_dump:1.1 
docker exec elasticsearch sh devexport 35.154.206.110:9200 user-index

```

### Creating a Dump

```
   elasticdump  --input=http://$SOURCE_IP/$index_name --output=http://$DESTINATION_IP/$index_name  --type=data
   elasticdump  --input=http://$SOURCE_IP/$index_name --output=http://$DESTINATION_IP/$index_name  --type=mapping
   elasticdump  --input=http://$SOURCE_IP/$index_name --output=http://$DESTINATION_IP/$index_name  --type=analyzer
```




## Docker file 

https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

#### Dump ES:

https://www.npmjs.com/package/elasticdump


```
CMD elasticdump  --input=http://dev.server.com:9200/search-log-index --output=http://127.0.0.1:9200/search-log-index  --type=data
CMD elasticdump  --input=http://dev.server.com:9200/user-index --output=http://127.0.0.1:9200/user-index  --type=data

CMD elasticdump  --input=http://35.154.206.110:9200/search-log-index --output=http://127.0.0.1:9200/search-log-index  --type=data
CMD elasticdump  --input=http://35.154.206.110:9200/user-index --output=http://127.0.0.1:9200/user-index  --type=data
CMD elasticdump  --input=http://35.154.206.110:9200/property-roomtype-index --output=http://127.0.0.1:9200/property-roomtype-index --type=data
CMD elasticdump  --input=http://35.154.206.110:9200/property-reviews-index --output=http://127.0.0.1:9200/property-reviews-index --type=data

elasticdump  --input=http://35.154.206.110:9200/user-index --output=http://localhost:9200/user-index  --type=analyzer
elasticdump  --input=http://35.154.206.110:9200/user-index --output=http://localhost:9200/user-index  --type=data
elasticdump  --input=http://35.154.206.110:9200/my_index  --output=$ | gzip > /data/my_index.json.gz


CMD elasticdump  --input=$SOURCE_SERVER/user-index --output=http://localhost:9200/user-index  --type=data
CMD elasticdump  --input=$SOURCE_SERVER/search-log-index --output=http://localhost:9200/search-log-index  --type=data

CMD [ "elasticdump  --input=$SOURCE_SERVER/search-log-index --output=http://localhost:9200/search-log-index  --type=data"]
```

### References:

* https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
* https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
* https://www.npmjs.com/package/elasticdump
* https://stackoverflow.com/questions/26547560/how-to-move-elasticsearch-data-from-one-server-to-another