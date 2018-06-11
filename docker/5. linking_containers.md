
# Linking Containers

- Run redis in detached mode (-d)

```
docker run -d --name redis1 redis
```
Now we will try to access this redis from another container.

# linking one contianer to another

```
docker run -it --link redis1:redis --name redisclient1 busybox
```
Note: — link flag is sourcecontainername:containeraliasname

above launch of container (redisclient1) will lead you to the shell prompt.

after linking you will find contianeraliasname in hosts file.

```
/ # cat /etc/hosts
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.17.0.6	redis 15e202fc8b17 redis1
172.17.0.7	ffb62ec5a468

/ # ping redis
PING redis (172.17.0.6): 56 data bytes
64 bytes from 172.17.0.6: seq=0 ttl=64 time=0.274 ms
64 bytes from 172.17.0.6: seq=1 ttl=64 time=0.137 ms
64 bytes from 172.17.0.6: seq=2 ttl=64 time=0.131 ms
```


If you print out the environment variables you will see the following (I have removed the other environment variables):

```
/ # set
...
PWD='/'
REDIS_ENV_GOSU_VERSION='1.10'
REDIS_ENV_REDIS_DOWNLOAD_SHA='df4f73bc318e2f9ffb2d169a922dec57ec7c73dd07bccf875695dbeecd5ec510'
REDIS_ENV_REDIS_DOWNLOAD_URL='http://download.redis.io/releases/redis-4.0.9.tar.gz'
REDIS_ENV_REDIS_VERSION='4.0.9'
REDIS_NAME='/redisclient1/redis'
REDIS_PORT='tcp://172.17.0.6:6379'
REDIS_PORT_6379_TCP='tcp://172.17.0.6:6379'
REDIS_PORT_6379_TCP_ADDR='172.17.0.6'
REDIS_PORT_6379_TCP_PORT='6379'
REDIS_PORT_6379_TCP_PROTO='tcp'
SHLVL='1'
TERM='xterm'
_='set'
```

Now create another redis container (client) to access old redis server container.

```
docker run -it --link redis1:redis --name client1 redis sh
```

 --`redis` is alias for old redis server. 

Got inside the new container and execute

```
redis-cli -h redis
```

# Reference:

* https://rominirani.com/docker-tutorial-series-part-8-linking-containers-69a4e5bf50fb