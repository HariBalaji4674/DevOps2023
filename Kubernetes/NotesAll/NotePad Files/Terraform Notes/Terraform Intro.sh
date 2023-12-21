Terraform Notes: 09-10-2023
---------------------------
What is Terraform? and how does it work?

Terraform:
----------
1) Automation Tool
2) The Tool is used to create the Infrastruture As A Code
3) It is a open source tool so that anyone can use and contribute to that
4) Developed By organization HashiCorp
5) It is used to define, manage,Privision,Maintain the Infrastucture.

How it works?
1) It Works like reading the configuration file which we have written as a code (HCL or JSON) and translate them into API Calls to interact with various infra providers
2) HCL --> HashiCorp Configuration Language 

Why we need terraform ?
2) To Build the Infrastructure Automatically when ever we need 

Infrastruture is --> Creating Ec2,LoadBalancers,Fire walls etc..

Uses: different thing uses diffenet tools 

Infrastruture as a Code--> IaaC/IaC
Terraform --> Very Popular IaaC Tool

What Advantages It will give ?
Advantages of IaaC/IaC(Terraform)
-----------------------
1. Version Control
2. Consistent Infra Over Diff Environments
3. can be intergrate with diff cloud providers
4. CRUD Opeation Can be done
5. Inventory Management
6. Cost Optimisation
7. Dependency Management
8. Modules --> Re use Th code
9. Declarative In nature


HashiCorp Configuration Language:
---------------------------------
HCL -->

variables
datatypes
loops --> Count , Count-index, For each
conditions
functions
count and count index
locals
data sources
outputs


What is Terraform Init?
1) It will intialize terraform.
2) and it will create the file of state files

what is terraform plan?
1) terraform will tell us what resources it is going to create 

what is terraform apply?
1) it will create the resources

Terraform Varibles :---> create variables.tf 
-------------------
Two types of variables:
input variables --> gives input
output variable --> retrives output

				variable "varible name" {
							type = string
							default = "Value or the Ami Id"
						}
						
				resource "aws" {
				ami = var.amiid
				instance_type  = var.insttype
				}
				


Terraform Providers:aws,gcp,azure --> create provider.tf 
------------------
How to create infras on multiregion of terraform ?

write two sets:

provider "aws" {
alias = "us-east-1"
region = "us-east-1"
}
provider "aws" {
alias = "us-west-1"
}

resource "region1"{
ami = 
instance_type = 
provider = "aws.us-east-1"
}

resource "region1"{
ami = 
instance_type = 
provider = "aws.us-west-1"
}


					terraform 	{
					required_providers {
						aws {
								source = "hashicorp/aws"
								version = "5.20.0"
							}
						}
					}
					provider "aws" {
					region = "us-east-1"
					}

Terraform Main/Infrastructure file --> Terraform Main File.tf
-----------------------------
			resource "aws_instances" "Main Group" {
					ami 				= "Ami Id"
					instance_type 		= "t2.micro"
					tags = { 
					   Name 			= "PeddireddyDemo1"
					   }
				   }
	   
Creating Security Group
-----------------------
			resource "aws_security_group" "Allow-all" {
				name = "Allow To all resource"
				description = "Allow to all resource"
				
				ingress {
				
				description 
				from_port
				to__port
				protocol 
				cidr_blocks
				}
				egress { 
				from_port
				to__port
				protocol = "-1"
				cidr_blocks ="0.0.0.0/0"
				}
			}

Locals In Terraform:
--------------------
Locals in terraform are named values which can be assigned and used in the code 
uses:
no duplication
increase the readability 
using the same values multiple time from locals 


Data Sources:
-------------
The Data souces are the service provided by the terraform to query the services prom providers 
there should be changes in services 

Terraform State File
terrafrom remote state file

State files in local :

What is state and remote state in terraform?

State file is comaprision file of creating the resource files
Remote state file is where we keep those in storage to rectify the duplicate problems



S3 Bucket --> to store all remote state fiels
DynamoDB --> to lock the terraform remote state files

inside provider files:inside the terraform block we need to write below code:


backend "s3" {
bucket = "unique name over the internet"
key = "key name"
region = "where to create that s3 buket"
dynamodb_table = "table_name"
}
Using S3 and DynamoDB
---------------------
1) No Duplicates
2) No Errors while creating resources saying already exits 
3) No accidental changes.

tfvars:
-------
tfvasrs is used to replace default values in variables or if valuesa are not specified in varibales.tf we can supply from here

to create multi env infra we can control through diffefenyt variable values and diff state.

IaaC :
Consistency across multi ENV, We use same code but different variables

Servers:
mongodb,mysql,catalogue,web,rabbitmq,user,shipping,redis,cart,

Different Variables Values
different state,You need to gve different location to store PROD state

Multi-ENV:
----------
1) Maintain different repos
	for each environment we need to maintain two different repos
	PROD
	DEV
2) Same code but different variable and config

pros: code is reused
cons:you should be very careful while changing same code is refelceting to prod.

3) terraform workspaces


Terrafrom Modules:
------------------
write code in one repository and call from another repository.


Tf vars:

terraform apply -var-file=PROD/prod.tfvars -auto-approve

terraform apply -var-file=DEV/dev.tfvars -auto-approve


****************************************

Session 28 : Terraform:
-----------------------

CIDR,VPC Building manually and With terraform ,route tables,subnets internetgateway etcc...

What is default gateway?
what is NAT?
What is Virtual Private Cloud?
What is Subnetting?
What is Route Table?
What is Public Route ?
What is Private Route?



How to create the Vpc and attach subnets to the VPC?

1) Create VPc With Ipv4 cidr_range = 10.0.0.0/16 
2) Create Sub_nets with ipv4 range : 10.0.1.0/24 --> 
3) Create sub_nets with ipv4 range = 10.0.2.0/24 --> 
4) Create internet gateway
5) create route tables-2
6) assocaite route table to subnets
7) attach public route table with internet gateway




	