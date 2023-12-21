$Kubernetes:
-----------
Kubernetes of the future of DevOps:

Kubernetes Plays a Marathon in DevOps:

# Pre-reequisite is Docker:

### Difference between Kubernetes and Docker?

$Docker is Container platform

Kubernetes is a container orchestration platform

Containers are ephimeral in nature
1) short lived (Die at anytime)
2) simple revived
3) easy installation.

## Problems in docker:
-----------------------
1) Docker is Single Host ( Containers will die due to lack of resources)
2) Think Like One member killed docker container then the application inside that container will not accessble --> hence needed auto healing method
3) Container Down at Occasion times--> Auto Scaling.
4) Docker is a minilistic or simple platform 
Docker does not support enterprise projects 

### Enterprise Support/Level Standard
-------------------------------------
Application should have load balancer
It should contain firewall
autoscalability
self healing capabilities
api gateways
etcc/...


## Terminologies:
-----------------

1) AutoHealing
2) AutoScaling 
(Horizantal Scaling and Vertical Scaling)
3) LoadBalancing
4) Firewalls
5) API Gateways
6) WhiteListing
7) BlackListing
8) DDoS Attack

## Kubernetes:
--------------
Container Orchestration tool where the platform is providing autoscalability,autohealing,Firewall support,api gateways support etcc/

By Default it is Clusters
It Supports AutoHealing
it Supports AutoScaling
It supports Enterprise level Standard

Kubernetes is a cluster 
Cluster is a group of nodes 
nodes here is group of machines 

### Kubernetes Architecture: K8S: 
-----------------------------
### Kubernetes has: 2 Parts

$Study #Here about K8'S Architecture: $#https://avinetworks.com/glossary/kubernetes-architecture/

Control Plane and Data Plane:

Master or Control Plane: 
Parts or Components
------------------------
API Server
Scheduler
ETCD
Controll Managers 
Cloud Controller Managers
Request Pass through the control Plane
Pod: Wrapper over the container over some additinal functionalities

Data Plane or Slave Node 
-------------------------
### Components in Data Plane:

$Container Runtime:
	responsible to run the pods

$Kubelet:
	Responsible for taking care of pods all CRUD Opearations
$Kubeproxy: 
	Responsible for providing the security to the pods ipaddress etcc...
	it uses iptables to provide networking to the pods or containers.


### Kubernetes Cluster managements:

kubectl or minikube









