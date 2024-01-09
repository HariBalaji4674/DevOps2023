# import boto3
# import json
# #Boto Core has : Exceptions
# #
# client = boto3.client('s3')
# client = boto3.client('sns')
# # response = client.create_bucket(
# #     Bucket='peddireddy-demo-boto3-bkt-123',
# # )
# response = client.delete_bucket(
#     Bucket='peddireddy-demo-boto3-bkt-123',
#     # ExpectedBucketOwner='string'
# )
#
# # print(response)
# # resource_data = json.loads(response)
#
# # print(resource_data)
import boto3
import pandas
def create_ec2_instances():
    # Initialize the EC2 client
    ec2 = boto3.client('ec2')

    # Specify the parameters for the instances
    instance_params = {
        'ImageId': 'ami-03265a0778a880afb',  # Replace with your desired AMI ID
        'InstanceType': 't2.micro',  # Replace with your desired instance type
        'KeyName': 'DevOpsPracticeKey',  # Replace with your key pair name
        'MinCount': 1,
        'MaxCount': 10,  # Create 10 instances
        # 'SecurityGroupIds': ['your_security_group'],  # Replace with your security group ID
        # 'SubnetId': 'your_subnet_id',  # Replace with your subnet ID
        # Add any additional parameters you require (e.g., UserData, BlockDeviceMappings)
    }

    # Create the instances
    response = ec2.run_instances(**instance_params)

    # Print information about the created instances
    for instance in response['Instances']:
        print(f"Created instance: {instance['InstanceId']}")


# Execute the function to create instances
create_ec2_instances()

# print(response)

# Need to see how to read json data to Dictionary

# Project Section: Boto3
# Lambda Function: Cloud Cost Optimization, Monitoring,Creating resources etc..
