# terraform {
#   required_providers {
#     aws = {
#       source = "hashicorp/aws"
#       version = "5.26.0"
#     }
#   }
# }
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "one" {
  ami = "ami-03265a0778a880afb"
  instance_type = "t2.micro"
}