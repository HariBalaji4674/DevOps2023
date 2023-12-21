variable "cidr_block" {
  type = string
  default = "10.0.0.0/16"
}
# variable "tags" {
#   type = map
#   default = {
#     Name = "ModuleVPC"
#     Terraform = "True"
#     Environment = "DEV"
#     Project = "Roboshop"
#   }
# }
variable "common_tags" {
  default = {
    Terraform = "True"
    Environment = "DEV"
    Project = "Roboshop"
  }
}
variable "vpc_tags" {
  default = {
    Name = "VPC-Roboshop"
  }
}

variable "igw_tags" {
  type =map
  default = {
    Name = "igw-gate1"
  }
}
variable "enable_dns_hostnames" {
  type = string
  default = true
}
variable "enable_dns_support" {
  type = string
  default = true
}

variable "public_subnet_cidr" {
  default = ["10.0.1.0/24","10.0.2.0/24"]
}

variable "private_subnet_cidr" {
  default = ["10.0.11.0/24","10.0.12.0/24"]
}

variable "db_subnet_cidr" {
  default = ["10.0.21.0/24","10.0.22.0/24"]
}
variable "azs" {
  default = ["us-east-1a","us-east-1b"]
}

variable "public_subnet_names" {
  default = ["roboshop-public-1a", "roboshop-public-1b"]
}
variable "private_subnet_names" {
  default = ["roboshop-private-1a", "roboshop-private-1b"]
}
variable "db_subnet_names" {
   default = ["roboshop-db-1a", "roboshop-db-1b"]
}
variable "public_route_name" {
    default = {
        Name  = "public_route"  
  }
}
variable "private_route_names" {
    default = {
      Name = "private_route"
      }  
}
variable "db_route_names" {
    default = {
      Name = "db_route"
    }  
}








# variable "ami_id" {
#     default = "ami-03265a0778a880afb"
# }
# variable "tags" {
#     type = map
#     default = {
#         Name = "First-Instance"
#         Environment = "DEV"
#         Terraform = true
#         Component = "MongoDB"
#         Project = "Roboshop"
#     }
# }
# variable "instance_type" {
#     default = "t2.micro"  
# }
# variable "sg_cidr" {
#     type = list
#     default = ["0.0.0.0/0"]
# }
# variable "instance_names" {
#   type = list
#   default = ["mongodb",
#   "cart",
#   "catalogue",
#   "web",
#   "redis",
#   "rabbitmq",
#   "shipping",
#   "payment",
#   "mysql",
#   "user"
#   ]
# }
# variable "zone_id" {
#   default = "Z04508813AN6FY8NXYMG5"
# }
# variable "domain_name" {
#   default = "haridevopspractice.online"
# }

# variable "inst_names" {
#     type = map
#     default = {
#         mongodb = "t3.medium",
#         web = "t2.micro",
#         redis = "t2.micro",
#         rabbitmq = "t2.micro",
#         catalogue = "t2.micro",
#         mysql = "t2.micro",    
#         cart = "t2.micro",
#         user = "t2.micro",
#         payment = "t2.micro",
#         shipping = "t2.micro",
#     }  
# }

# variable "sgrules" {
#     type = list
#   default = [ 
#    {
#     description      = "Port No HTTPS in TCP"
#     from_port        = 443
#     to_port          = 443
#     protocol         = "tcp"
#     cidr_blocks      = ["0.0.0.0/0"] 
#     } ,
#   {
#     description      = "Port No 80 From TCP "
#     from_port        = 80
#     to_port          = 80
#     protocol         = "tcp"
#     cidr_blocks      = ["0.0.0.0/0"]
#   },
#   {
#     description      = "Port No 22 SSH Connection"
#     from_port        = 22
#     to_port          = 22
#     protocol         = "tcp"
#     cidr_blocks      = ["0.0.0.0/0"]
#   },
#   {
#     description      = "Port No 8080 From TLC"
#     from_port        = 8080
#     to_port          = 8080
#     protocol         = "tcp"
#     cidr_blocks      = ["0.0.0.0/0"]
#   }
# ]
# }

# variable "sg_name" {
#     default = "Allow-all"  
# }