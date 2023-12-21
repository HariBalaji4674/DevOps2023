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