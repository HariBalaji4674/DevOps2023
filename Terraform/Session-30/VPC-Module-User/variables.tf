variable "cidr_block" {
  default = "10.0.0.0/16"
}
variable "enable_dns_hostnames" {
  default = true
}
variable "enable_dns_support" {
  default = true
}
variable "common_tags" {
  default = {
    Environement = "DEV"
    Terraform = "TURE"
    Status = "Allowed"
  }
}
variable "project_name" {
  default  = "roboshop"
}
variable "vpc_tags" {
  default = {
    VPC-name = "VPC-DEV"
  }
}