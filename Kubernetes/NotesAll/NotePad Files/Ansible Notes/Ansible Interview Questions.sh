Anisible Interview Questions
-----------------------------
1. What is Configuration Management?

Ans :  Configuration management is a process for maintaining computer systems, servers, applications, network devices, and other IT components in a desired state. It’s a way to help ensure that a system performs as expected, even after many changes are made over time.  

2. How does Ansible work?

Ans :  Ansible works by connecting to nodes (clients, servers, or whatever you are configuring) on a network, and then sending a small program called an Ansible module to that node. Ansible executes these modules over SSH and removes them when finished.

3. What are the features of Ansible? 
 or  do you think ansible is better than other configuartion management tools ? if yes why ?
Ans : 
	1) Agent Less
	2) ssh authentication
	

4. Explain Infrastructure as Code?

5. What is Ansible Galaxy?

6. Explain Ansible modules in detail?

7. What is a YAML file and how do we use it in Ansible?

8. What are Ansible tasks?

9. How to use YAML files in high programming languages such as JAVA, Python, etc?

10. How to setup a jump host to access servers having no direct access?
11. How to automate the password input in playbook using encrypted files?
12. What are callback plugins in Ansible?
13. What is Ansible Inventory and its types?
14. What is Ansible Vault?
15. How can looping be done over a list of hosts in a group, inside of a template?
16. What is the ad-hoc command in Ansible?
17. Install Nginx using Ansible playbook?
18. How do I access a variable name programmatically?
19. What is the difference between Ansible and Puppet?
20. What is Ansible Tower and what are its features?
21. Explain how you will copy files recursively onto a target host?
22. What is the best way to make Content Reusable/ Redistributable?
23. What are handlers?
24. How to generate encrypted passwords for a user module?
25. How does dot notation and array notation of variables are different?
26. How does Ansible synchronize module works?
27. How does the Ansible firewalld module work?
28. How is the Ansible set_fact module different from vars, vars_file, or include_var?
29. When is it unsafe to bulk-set task arguments from a variable?
30. Explain Ansible register.

31. 

AKIAX3JUAAKLFISIVCQ3
AKd5+x8heQhYYQp8Ro4H051PNq0Kw1mAUDOnviWR


1. Resource Utilization: Containers share the host operating system kernel, making them lighter and faster than VMs. VMs have a full-fledged OS and hypervisor, making them more resource-intensive.

2. Portability: Containers are designed to be portable and can run on any system with a compatible host operating system. VMs are less portable as they need a compatible hypervisor to run.

3. Security: VMs provide a higher level of security as each VM has its own operating system and can be isolated from the host and other VMs. Containers provide less isolation, as they share the host operating system.


The host's file system: Docker containers can access the host file system using bind mounts, which allow the container to read and write files in the host file system.

Networking stack: The host's networking stack is used to provide network connectivity to the container. Docker containers can be connected to the host's network directly or through a virtual network.

System calls: The host's kernel handles system calls from the container, which is how the container accesses the host's resources, such as CPU, memory, and I/O.

Namespaces: Docker containers use Linux namespaces to create isolated environments for the container's processes. Namespaces provide isolation for resources such as the file system, process ID, and network.

Control groups (cgroups): Docker containers use cgroups to limit and control the amount of resources, such as CPU, memory, and I/O, that a container can access.
    
	
	
6 Habits 

1 Reading Books
2 