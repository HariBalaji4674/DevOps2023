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
variable "instance_names" {
  type = list
  default = ["mongodb",
  "cart",
  "catalogue",
  "web",
  "redis",
  "rabbitmq",
  "shipping",
  "payment",
  "mysql",
  "user"
  ]
}
variable "zone_id" {
  default = "Z04508813AN6FY8NXYMG5"
}
variable "domain_name" {
  default = "haridevopspractice.online"
}

variable "inst_names" {
    type = map
    default = {
        mongodb = "t3.medium",
        web = "t2.micro",
        redis = "t2.micro",
        rabbitmq = "t2.micro",
        catalogue = "t2.micro",
        mysql = "t2.micro",    
        cart = "t2.micro",
        user = "t2.micro",
        payment = "t2.micro",
        shipping = "t2.micro",
    }  
}