terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "5.24.0"
    }
  }
  backend "s3" {
        bucket = "haridevopsbucket123"
        key    = "peddireddy"
        region = "us-east-1"
        dynamodb_table = "haridevops123"
  }
}
provider "aws" {
    region = "us-east-1"
}

