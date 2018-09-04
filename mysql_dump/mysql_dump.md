### mysqldump command 

```
mysqldump --column-statistics=0 --single-transaction -h 35.154.206.110 -P 3306 -u fabreadwrite -p'HsxmfL$5H6L$$_cD' --databases user_microservice > dump.sql
```
### Using Docker Run


```
docker run --name mysql -p 6306:3306 -v /Users/deepak/docker_dirs/mysql-data:/var/lib/mysql --env-file ./vars.env -d javatechy/mysql_dump
```

### Start Export using this command

```
docker exec mysql sh export
```

### Using Docker Compose 

use this docker compose file

```
version: '2'
 
services:
  mysql:
    image: javatechy/mysql_dump
    container_name: mysql
    ports:
      - 6306:3306
    environment:
      MYSQL_ROOT_PASSWORD: "1"
      SOURCE_MYSQL_IP: "35.154.206.110"
      SOURCE_MYSQL_PORT: "3306"
      SOURCE_MYSQL_PASSWORD: "HsxmfL$$5H6L$$$$_cD"
      DATABASES_LIST: "user_microservice"
      EXTRA_ARGS: ""
    command:
     - dump_mysql
    volumes:
      - /users/deepak/docker_dirs/mysql-data:/var/lib/mysql
```

#### Taking a dump

```
mysqldump --column-statistics=0 --single-transaction -h docker.for.mac.localhost -P 3306 -u username -p'PASSWORD' --all-databases > dump.sql
```

### PRIVILEGES :

```
GRANT ALL PRIVILEGES ON *.* TO 'fabreadwrite'@'%' IDENTIFIED BY 'HsxmfL$5H6L$$_cD';
FLUSH PRIVILEGES;
```


#### Using ENV variables

```
docker run --name mysql -p 6306:3306 -v /Users/deepak/docker_dirs/mysql-data:/var/lib/mysql --env-file /Users/deepak/projects/dock_compose/mysql/vars.env -d javatechy/mysql_dump
```