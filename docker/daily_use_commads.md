# Remove Docker Volumes
docker volume prune
docker volume rm Remove one or more volumes

docker run --rm --volumes-from metabase-data -v $(pwd):/backup metabase tar cvf /backup/backup.tar /metabasedata



 - Install Docker on ubuntu
- https://docs.docker.com/install/linux/docker-ce/ubuntu/#upgrade-docker-after-using-the-convenience-script


- Backup : 

https://github.com/loomchild/volume-backup



docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.4


docker run --name elasticsearch  -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -v elasticsearch-data:/usr/share/elasticsearch docker.elastic.co/elasticsearch/elasticsearch:6.2.4


docker run --name elasticsearch  -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -v elasticsearch-data_1:/usr/share/elasticsearch javatechy/elasticseach_dump:1.1 
docker exec elasticsearch sh devexport 35.154.206.110:9200 user-index



   elasticdump  --input=http://$SOURCE_IP/$index_name --output=http://$DESTINATION_IP/$index_name  --type=data
   elasticdump  --input=http://$SOURCE_IP/$index_name --output=http://$DESTINATION_IP/$index_name  --type=mapping
   elasticdump  --input=http://$SOURCE_IP/$index_name --output=http://$DESTINATION_IP/$index_name  --type=analyzer
   

################################################################################################################################################


Docker file 

https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

- Dump ES:

https://www.npmjs.com/package/elasticdump


CMD elasticdump  --input=http://dev.server.com:9200/search-log-index --output=http://127.0.0.1:9200/search-log-index  --type=data
CMD elasticdump  --input=http://dev.server.com:9200/user-index --output=http://127.0.0.1:9200/user-index  --type=data
C

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

https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
https://www.npmjs.com/package/elasticdump
https://stackoverflow.com/questions/26547560/how-to-move-elasticsearch-data-from-one-server-to-another


715186ce24ff4c44b4c60ef51d900f17


Creaitng Docker file:

https://rominirani.com/docker-tutorial-series-writing-a-dockerfile-ce5746617cd

https://www.npmjs.com/package/elasticdump


Cheat Sheet:
https://springframework.guru/docker-cheat-sheet-for-spring-devlopers/









Got to Amazon Elastic Container Registry

Create Repostiry

aws ecr get-login --no-include-email --region ap-south-1

docker login -u AWS -p eyJwYXlsb2FkIjoiL0dQVWVkK1ZLRjZIbzdUV0w2SHpvcGpNcnFQckxBQmxkelF2VFM5MkpTbFRvOU45cUVYNUZ3Mld2S1VGTzl0VEJUd3QxZmg1SzFpK0h5aW9WSXNPdzJ5UGRXZWg2S1Y4RkV5MEtNYjV2VUdncnZ2a2EzL0Q5Ukc1ZDduellwcFRPY3c5QUZMZDVFQ2pqMW45bXBHMlJ4VnVNN0h4cmd5dHRIdjh3cXNsWktneXFsMERFRUFBdW1yb1EwMUphV21OajhUcmdTaFNpcW9veFdXbjROWFF5d00xNG5VdFNsWk5WaUJPWFI1dk4wRFFtd2ttOW1DT2VXN21hKytYVnZhRlk2NlZHVVNGTW91WnBxODM1RDVXVEtFTlpvTDNTdms0SnRZYUtnMEp4RDNjTjREdURwSWtHY2phdXdaVFdwVkNzRmg1c0R5T0lGa2xFOHpTWXlMdDFVdGFJamxpdXYvaGxCSTVkUDNDdmZOTWhqYUR6a3JNc0pzRzR1SnpQbFFQZHFDRTJFWGtObm94eFF2aUZBNnU0eUNHUTlvY2hYc0dROS9uK2g2NUoxOTZlcTNxUUFjcEUzM2EzZ2w0SUltUHBpV0RNdkZ0OW9naXlHNERUWTVtSFdjMExmdi9yRDBBY1ZCNU9TNEFRQW9ubHlPV3BFZEluNnYwcHFkTXpZaE9DdlhWa3RVRVp6SWFsbVg4T0JHZmRjQ2tuRWUvMStUS2NYM0FmMjhvNzQrY0UvUlVnWnJId2NRQ3VRYWIzLy9mVUJPQlpnZVhiek1BZGo4NWk3aDlwamFDVXltQ1EzUy9VR09hOWdlaTFMR3NZbUFWNVQ3MUNQcmFwYUdscVk0aGdCV3R4aUI5NzJ5RzlMcmZBcVdHVXFyOU8vZC9vS3FlS041Skp5eVlxeC94Yzh1c2V2ZWFxZHFNZHk2c1pXVDlHVGJWUE5rMWtKY0l2ZTYvV1FHTitLTG1aZjQ2TUV0bXpueFlhR1ZCMERURFllRnZwK28zd1AzajEvcXN6UnFUUDNBamFTN1drOXdKTGtweTNYSU52VVU5SXBVcG0zK2ZseU1vczltRE5hUTNTekNoRDJVdkhiazExdHVUV1ZHcS8rTnIxOGRQaHBDVitvemt6WHFqbjF3S3dPOG1LTVBtWm85b2lMVkVyM1hTWDNQSnEwRmNHT2QyZnQ5MnFmMVlmc3g2SzdEcGFiSkpNWHNJZFF4TGhIWG5ET1l3SlBRTEpJMWd3QW1LRWpkamNJdGhTWVpCQmNMMTRsM2hHc2dyK2NpVmNKL2xkTFVDaXdmUEJaU1JweTZMbTFFdmZ2U2hMc2pKMGFqYW9lMjl3OStRRFBBRiIsImRhdGFrZXkiOiJBUUlCQUhpSFdhWVRuUlVXQ2Jueis3THZNRytBUHZUSHpIbEJVUTlGcUVtVjI2QmR3d0ZSb1g5UnZrbWZRVUVEKzQ2RURTblBBQUFBZmpCOEJna3Foa2lHOXcwQkJ3YWdiekJ0QWdFQU1HZ0dDU3FHU0liM0RRRUhBVEFlQmdsZ2hrZ0JaUU1FQVM0d0VRUU1BRC9MdXNuOFF3K2U5SVBHQWdFUWdEdmdPZFA5cnNKWEZJdnJnOU9vamZDNU1GZzdhbjlMY212LzlPcjRFbkY5OEgwd01Pa1hhZ1FCLzdxRTdLYk5IUTE5RnphaUhrdjVDUUlIU2c9PSIsInZlcnNpb24iOiIyIiwidHlwZSI6IkRBVEFfS0VZIiwiZXhwaXJhdGlvbiI6MTUyODMzMTU2Mn0= https://425123548659.dkr.ecr.ap-south-1.amazonaws.com


WARNING! Using --password via the CLI is insecure. Use --password-stdin.

###.  Create a repositry from CLI
aws ecr create-repository --repository-name hotelier

###.  Run a docker images
docker run -it -v  /usr/local/casa/properties:/usr/local/casa/properties -v /var/log/casa:/var/log/casa -p 9000:8000 425123548659.dkr.ecr.ap-south-1.amazonaws.com/hotelier:1.0 --rm

docker run -it -v  /usr/local/casa/properties:/usr/local/casa/properties -v /var/log/casa:/var/log/casa -p 9000:8000 -d 425123548659.dkr.ecr.ap-south-1.amazonaws.com/hotelier:1.0


docker run -it -v /var/log/casa:/var/log/casa -p 9000:8000 -d 425123548659.dkr.ecr.ap-south-1.amazonaws.com/hotelier:1.0

docker push 425123548659.dkr.ecr.ap-south-1.amazonaws.com/openjdk-8-slim

Logback vs Log4j
 https://dzone.com/articles/which-one-faster-log4j-or


Skip Building images:
 mvn clean install -Ddocker.skip

More commands on
- https://dmp.fabric8.io/


http://www.mojohaus.org/properties-maven-plugin/
