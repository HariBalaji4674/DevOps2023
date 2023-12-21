variable "cidr_block" {
 
}
variable "common_tags" {
    type = map
  default = { }
}

variable "vpc_tags" {
  type  = map
  default = {}
}

variable "igw_tags" {
    type =map
    default = {}
}

variable "enable_dns_hostnames" {
  default = true
}
variable "enable_dns_support" {
  default = true
}

variable "public_subnet_cidr" {
#   default = " "
}
variable "private_subnet_cidr" {
#   default = " "
}
variable "db_subnet_cidr" {
#   default = " "
}
variable "public_subnet_names" {
  
}
variable "private_subnet_names" {
  
}
variable "db_subnet_names" {
  
}
variable "azs" {
}
variable "public_route_name" {
  
}
variable "db_route_names" {
  
}
variable "private_route_names" {
  
}