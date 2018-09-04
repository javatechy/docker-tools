STEPS:
  - Create Cluster
  	- ECS -> create cluster -> Confiure cluster -> 
		- give name + Select vpc + select 2 subnets + secutiry groups 
		- Press create 
		
	- Create Task instance
	    - name the container - 
		- select network mode bridge
		- add contriants - for ex.  if you want to run your task only on m4.large machine(instancetype==t2.micro)
		- add container
			- add a name 
			- add image url
			- limit the memory 
			- sepecify your cpu units for the container in ENvironent section
			- Sepcify env variables
				- env : dev
			- Add log vars:
				- awslogs-group: my_cloud_watch_log_group
				- awslogs-region: ap-south-1
				- awslogs-stream-prefix: app_name
				- awslogs-create-group : true
				
			- Add Secutity section : 
				- if you want to create your own user for docker container, add username in this section
			- RESOURCE LIMIT SECTION
				- in this section you can limit no of cores, cpus etc.
			- VOLUME SECTION
				- if you add a volume in this section it will be shared with evry container running on that instance.
				
	- Create Services
 		- ECS -> cluster-> open a cluster -> go to services sections -> click on create service
		- select a Task Defination
		- select a cluster
		- specify number of tasks - 2/3/4 ...
		- change min helathy max healthy percent
		- select AZ balance spread  as placement templates
		- Load Balance
			- create a load balancer first - ALB
		- Container to Load balance
			- seelcet the container and Target group 
			- no need to configure health check bcoz already defined in ALB
		- Click on NEXT
		- Configure Autoscaling
			- select Minimum no of task + Desired number of tasks(At starting) + Maximum number of tasks
		- Automatic task scaling policies
			- Scaling policy type: Step scaling
			- Scale out (increase desired count)
				- AVERAGE + of CPUUtilization >=20 for 1 miniute - SAVE
				- Scaling action : ADD 1 tasks ....
			- SET cooldown period
		- Scale in (decrease desired count)
			- Scale out (increase desired count)
				- AVERAGE + of CPUUtilization <=10 for 1 miniute - SAVE
				- Scaling action : REMOVE 1 tasks ....
			- SET cooldown period
		- Create Service 
 

### Cluster
ECS cluster are region specific
can have different type of machines

###.  Create a repositry from CLI
aws ecr create-repository --repository-name hotelier

 
### AWS ECS Reference:

https://medium.com/boltops/gentle-introduction-to-how-aws-ecs-works-with-example-tutorial-cea3d27ce63d

https://gist.github.com/duluca/ebcf98923f733a1fdb6682f111b1a832

 