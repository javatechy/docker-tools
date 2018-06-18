# Docker swarn


# Create a docker machine 1 manger and 5 workers

```
docker-machine create --driver virtualbox manager1
docker-machine create --driver virtualbox worker1
docker-machine create --driver virtualbox worker2
docker-machine create --driver virtualbox worker3
docker-machine create --driver virtualbox worker4
docker-machine create --driver virtualbox worker5
```

# Going inside a machine

```
docker-machine ssh <machine-name>
```

# get Docker machines Ip

```
docker-machine ls
```

# Create a swarm

```
docker swarm init --advertise-addr 192.168.99.101
```
