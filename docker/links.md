 # Install Docker on ubuntu
- https://docs.docker.com/install/linux/docker-ce/ubuntu/#upgrade-docker-after-using-the-convenience-script


# Backup : 

https://github.com/loomchild/volume-backup

http://www.filepermissions.com/file-permission/555



# Logback vs Log4j
 https://dzone.com/articles/which-one-faster-log4j-or

 
# Cheat Sheet:

https://springframework.guru/docker-cheat-sheet-for-spring-devlopers/


# Creaitng Docker file:

https://rominirani.com/docker-tutorial-series-writing-a-dockerfile-ce5746617cd

https://www.npmjs.com/package/elasticdump





# Docker file 

https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

#  Dump ES:

https://www.npmjs.com/package/elasticdump


#  Creaitng Docker file:
https://rominirani.com/docker-tutorial-series-writing-a-dockerfile-ce5746617cd
https://www.npmjs.com/package/elasticdump
https://springframework.guru/docker-cheat-sheet-for-spring-devlopers/


# Graphite :

docker run -d --name graphite  -p 8081:80  -p 2003:2003 sitespeedio/graphite
docker run -d  --name graphite -p 8081:80 -p 2003:2003 -v /Users/deepak/docker_dirs/graphite/.htpasswd:/etc/nginx/.htpasswd -v /Users/deepak/docker_dirs/graphite/storage/whisper:/opt/graphite/storage/whisper  -v /Users/deepak/docker_dirs/graphite/storage-schemas.conf:/opt/graphite/conf/storage-schemas.conf sitespeedio/graphite

#  New Relic integration:
 https://discuss.newrelic.com/t/need-help-using-new-relic-with-spring-boot-docker/53521/4
 http://central.maven.org/maven2/com/newrelic/agent/java/newrelic-java/4.4.0/newrelic-java-4.4.0.zip
  
 ## Gerrit
  
 docker run \
         -e MIGRATE_TO_NOTEDB_OFFLINE=1 \
         -v ~/gerrit_volume:/var/gerrit/review_site \
         -p 8099:8080 \
         -p 29418:29418 \
         -d openfrontier/gerrit
 