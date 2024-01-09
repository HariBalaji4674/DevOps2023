import boto3

def destroy_running_instances():
    # Initialize the EC2 client
    ec2 = boto3.client('ec2')

    # Get all running instances
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    instance_ids = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_ids.append(instance_id)

    if instance_ids:
        # Stop the instances
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped instances: {instance_ids}")

        # Terminate the instances
        ec2.terminate_instances(InstanceIds=instance_ids)
        print(f"Terminated instances: {instance_ids}")
    else:
        print("No running instances found.")


# Execute the function to stop and terminate instances
destroy_running_instances()
