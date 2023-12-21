### Ansible playbook concepts:
------------------------------
Coding Has Two types :
1) Programming 
2) Scripting

## Concepts
1) Variables
2) Data Types
3) conditions
4) loops
5) functions
6) Modules


$Ansible Loops:
***************
# Ietarte over the list of items 
# Item is used to call the list items in loops 
# it is special type to call the items from list

debug:
  msg: "{{item}}"

loop:
  - nginx
  - postfix
  - mailx
  - cyrus-sasl-plain
  
$Advanced Loops: # a list of hashes
***********************************
loop:
  - {name: 'nginx', state:'absent'}
  - {name: 'postfix',state: 'present'}

# We Call them as a item.state or item.name

yum:
  - name:"{{item.name}}"
  - state: "{{item.state}}"
  
  
ansible-playbook -i inventory -e ansible_user=centos -e ansible_password=DevOps321 catalogue.yaml


ansible-playbook -i inventory -e ansible_user=centos -e ansible_password=DevOps321 web.yaml


ansible-playbook -i inventory -e ansible_user=centos -e ansible_password=DevOps321 cart.yaml


ansible-playbook -i inventory -e ansible_user=centos -e ansible_password=DevOps321 catalogue.yaml