import boto3

ec2 = boto3.client('ec2')

# Configuration for the new EC2 instance
instance_type = 't2.micro'
image_id = 'ami-03265a0778a880afb'  # Replace with the desired AMI ID
key_name = 'DevOpsPracticeKey'
# security_group_ids = ['SECURITY_GROUP_ID']  # Replace with security group IDs
# subnet_id = 'SUBNET_ID'  # Replace with the desired subnet ID

# Launch the EC2 instance
response = ec2.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    MaxCount=1,
    MinCount=1
)

# Get the instance ID of the launched instance
instance_id = response['Instances'][0]['InstanceId']
print(f"Instance {instance_id} created successfully!")
