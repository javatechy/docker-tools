ContainerOrchestrationonAWS
● ServiceDiscovery
● Service Load Balancing
● AutoScaling
● Storage
● Continuous Integration & Delivery

What is Container Orchestration?

Technologies which allow us to:
○ Create multi-node container clusters 
○ Managemultiplecontainerseasily
○ Automatecontainerlifecycle


Why Do We Need Container Orchestration?
● Horizontal scalability across multiple hosts
● Grouping of related containers
● Automatic failure detection and recovery ● Seamlessupdates

ECS - EC2 Container Service
● Docker container orchestration service by AWS 
● Operates on top of EC2
● Built-in private Docker registry (ECR)

Why Use ECS?
● Built-insecurity
○ Assign IAM Roles to Docker containers
○ Docker registry authentication using IAM
● Native integration with ELB and Auto Scaling
● Spot fleet + Auto Scaling support (announced Sep. 1, 2016) ● FullsupportfromAWS

ECS Components
● Cluster - a group of container instances
● Container Instance - an EC2 instance that hosts containers
● Task - a set of related Docker containers
● Task Definition - a template which defines a task
● Service - a group of identical tasks
 
 
 Cluster
● A group of container instances
● Supports multiple Availability Zones
● Bound to a specific AWS region


Container Instance
● An EC2 instance running Docker with an ECS agent
● May be deployed from an official AWS AMI
● May be deployed using an Auto Scaling group
● Can be of any EC2 instance type / size
 
 
 Task
● A set of one or more related containers
● Deployed to a cluster
● Containers within a task are placed on the same host


Task Definition
● Serves as a “template” for tasks
● Allows to define most of the Docker features accessible via
docker run (image, volumes, networking, env vars...)
● Allows to define CPU and memory limits for the tasks
● Can assign an IAM role to a task
● Configurable using JSON
 
 
 Service
● An abstraction above tasks
● Deploys multiple “copies” from a task definition
● Maintaines the desired number of running tasks
● May bind to a load balancer
 