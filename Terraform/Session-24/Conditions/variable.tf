variable "ami_id" {
    default = "ami-03265a0778a880afb"
}
variable "tags" {
    type = map
    default = {
        Name = "First-Instance"
        Environment = "DEV"
        Terraform = true
        Component = "MongoDB"
        Project = "Roboshop"
    }
}
variable "instance_type" {
    default = "t2.micro"  
}
variable "sg_cidr" {
    type = list
    default = ["0.0.0.0/0"]
}
variable "instance_name" {
    default = "mongodb"  
}