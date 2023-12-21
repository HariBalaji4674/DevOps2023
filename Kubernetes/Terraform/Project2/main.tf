# Creation of S3 Bucket
resource "aws_s3_bucket" "bucket1" {
  bucket = "haridevopsbucket123"

  tags = {
    Name        = "haribucker"
    Environment = "Dev"
  }
}
resource "aws_dynamodb_table" "basic" {
  name = "haridevops123"
  hash_key       = "peddireddy"
  attribute {
    name = "peddireddy"
    type = "S"
  }
}

# backend "s3" {
#         bucket = "haridevopsbucket123"
#         key    = "project1"
#         region = "us-east-1"
#         dynamodb_table = "haridevops123"
#   }