$Disadvantages of shell scripting:
---------------------------------
Shell scripting is Homogenous
Shell Scripting is Imperative
shell scripting by default does not contain validations
Slow execution speed.
Not suited for large and complex tasks.
Design flaws within the language syntax.
Provides minimal data structure, unlike other scripting languages.
Prone to costly errors.


$Ansible Introduction:
---------------------
What is Ansible? manging the remote servers and cotrols their desired state.

Ansible is an open soure IT automation tool.
Ansible automates the provisioning , configuration management, app deployment with secure way, orchestration and many other manual process
Ansible automation used to install software, automate daily tasks,provisioning,security ,patch systems automate repitative tasks etc..


### What is difference between push mechanisham and pull machanism ?




# A Basic ansible environment has 3 components:
control node:
Where ansible loacted and contorls the remote servers
Manager node:
Inventory file:

### What Programming language is used to build Ansible? ---> Python Programming Language 

###How ansible connects to another servers ? --->
1) Ansibel uses SSH In background and makes the configurations between two  or more servers 

###Will Ansible used agents to connect and install software in nodes --> 
no Ansible does not use agents to run the scripts or to install the software.

# Inventory file Follows one way to represent the servers or group the servers

geography based --> in,us,uk,automate
environment based --> DEV,QA,PROD
component based --> web,app,db
serevr based -->database,web,backend etcc...

### What kind of language is Ansible ? 1) Ansible is a Declarative Language

### What is declarative language ?
Declarative Language is easy syantax and does not follow particular sequence to install the softwares 
As ansible build with python  by default it supports easy syantax and structure 

### What are the adavantages of Ansible over Shell Scripting?
1) No need to log in to run the scripts --> ansible will connect and run automatically in the nodes 
2) No need to write the sequence steps --> ansible can write the conditions anywhere it will get that
3) shell has more complicated syntax --> ansible has simple syntax
in shell we need to explicitly mention the validations --> ansible by default will come up with validations
4) Shell script is homogeneous (Different commands for different os) --> ansible will change commands based on OS

### Does ansible supports windows and linux ? 

Yes Ansible supports Both linux and windows 
Linux is used protocol is used SSH Authentication uses
Windows is used protocol connect with winRM


### What is diff between puppet and ansible ?
Pull and push Mechanism
Master slave and AgentLess
XML Format and YAML Scripting Format
Complex Structure and Simple Structure
No Inventory Files and Has inventroy files where store all server details 

### Does it depends on different cloud platforms
ansible does not depends on cloud platforms
the cloud platform should allow to configure with shh 
and it should be public cloud and shh for linux and winRMfor windows
------------------------------------

## What is ansible playbooks ?

$playbooks
keep all the modules and collections in a yaml file and run that file


A Playbook is file where we mention different commands/collections/modules which needs to be executed when we run that file by using command called
$ansible-playbook -i inventory file <palybookfile>

### Playbook is in YAML Format

### what is ansible adhoc commands?

Adhoc is for emergency purpose 
We use adhoc commands we use have emergency congiguration changes

when we need to execute some 2-3 commands we used to run through command line tool is called ansible adhoc commands

syntax:
ansible -i inventoryfile hostnames -m "modulename" -a "arguments"

### what is ansible roles?

Ansible roles is simple structure to create a ansible-playbook in a more efficient way
it makes a structure of playbook in more efficient way
when we are writing any complex playbook we need to use ansible roles

roles will create bunch of files like below each has own definitions:
------------------------------------ 
templates
README.md  
defaults  
handlers  
meta  
tasks  
tests  
vars

syntax:
-------
ansible-galaxy role init <filenameto create>

git hub repository--> ansible roles examples
https://github.com/ansible/ansible-examples 


Procedure of ansible:
--------------------
Before ansible: --> chef and puppet (Pull Mechanism)

it follows pull mechanism --> it means there should be one chef server and connected with another server/host in that one agent will be there to run the scripts 

first write the scripts and sent to chef server and agent in the node will fetch every 30 min if there are any code changes if there any changes it will run script 

After ansible: Ansible Server :  (Push Mechanism)
-------------------------------

No Agent(AgentLess) in host or nodes --> uses SSH machnism to connect
whenever there is changes in script we can push the changes to host/node  


Ansible 
-----------------
How to connect to node server with ansible server

ansible -i <nodeipaddress>, all -e <nodeusername> -e <nodepassword> -m ping 

ansible -i 172.31.83.56, all -e ansible-user=centos -e ansible-password=DevOps321 -m ping

In shell we call yum install as : Commands
in ansible we call yum install : as modules


### Ansible Modules:
--------------------
Modules are the commands or methods in ansible to download or execute commands 

The units of code Ansible executes. Each module has a particular use, from administering users on a specific type of database to managing VLAN interfaces on a specific type of network device. You can invoke a single module with a task, or invoke several different modules in a playbook. For an idea of how many modules Ansible includes, take a look at the list of all modules  

Ansible is more readable 
ansible is more declarative

Yellow color : Symbol is change
Green color : already it is changed or present 

ansible -i inventory all -m "name=nginx state=installed"

 $Ansible Variables:
 *******************
 
 Debug Module :
 debug:
	msg: "I am learning Ansible Module"

1) Play Level Variables:
************************
	#Play Varibles Inside the playbook we mention
	vars:
	  course: DevOps321
	  name: Hari
	  year: 2023
	debug:
	  msg: "{{course}},{{name}},{{year}}"

2) Variables from Files:
************************
declare all variables in file like below:
varsfile.yaml
	name: Hari
	section: DevOps321
	year: 2023
vars_file:
- varsfile.yaml
tasks:
  debug:
    msg: "I am Learning {{name}},I am new to section {{section}}"

3) Variables from prompt:
*************************

- name: Prompt Variables
  hosts: localhost
  vars_prompt:
  - name: USERNAME
    PROMPT: Give Me User name
	private: false
  vars_prompt:
  - name: PASSWORD
    PROMPT: Give Me User name
	private: false
	
 


