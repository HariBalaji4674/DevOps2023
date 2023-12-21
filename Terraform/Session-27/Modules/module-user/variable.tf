variable "ami_id" {
    type = string
  default = "ami-03265a0778a880afb"
}
variable "instance_type" {
    type  = string
    default = "t2.micro"
}
variable "inst_name" {
    type  = string
    default = "Roboshop"
}