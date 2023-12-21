terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "5.26.0"
    }
  }
  backend "s3" {
        bucket = "roboshophari"
        key    = "ec2"
        region = "us-east-1"
        dynamodb_table = "haritable"
  }
}
provider "aws" {
    region = "us-east-1"  
}