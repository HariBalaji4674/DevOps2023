import json
import requests
import boto3
import sys

# response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# # print(response.json())
# print(response.status_code)
# print(response.links)

# details = response.json()
# print(details[0]["id"])


# for i in range(len(details)):
#     # print(i)
#     print(details[i]["user"]["login"])

# fetching_data = requests.get() 
client = boto3.client('s3')
response = client.create_bucket(
    Bucket='peddireddy-demo-boto3-bkt-123',
)

print(response)
data_fi = response.json()
print(data_fi)