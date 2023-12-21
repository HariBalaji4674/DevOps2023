import boto3
import json
#Boto Core has : Exceptions
# 
client = boto3.client('s3')
client = boto3.client('sns')
# response = client.create_bucket(
#     Bucket='peddireddy-demo-boto3-bkt-123',
# )
response = client.delete_bucket(
    Bucket='peddireddy-demo-boto3-bkt-123',
    # ExpectedBucketOwner='string'
)

# print(response)
# resource_data = json.loads(response)

# print(resource_data)






















# print(response)

# Need to see how to read json data to Dictionary

# Project Section: Boto3
# Lambda Function: Cloud Cost Optimization, Monitoring,Creating resources etc..
