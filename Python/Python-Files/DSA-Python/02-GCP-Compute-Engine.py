from google.cloud import compute_v1

# Create a Compute Engine client
compute_client = compute_v1.InstancesClient()

# Project and Zone information
project = 'My First Project'
zone = 'us-central1-a'

# Instance configuration
instance_name = 'new-instance'
machine_type = f'zones/{zone}/machineTypes/n1-standard-1'
image = 'projects/debian-cloud/global/images/debian-10-buster-v20220110'  # Change the image as needed

config = {
    'name' : peddireddy ,
    'machine_type' : 'n1-standard-1'
}

# Create the instance
operation = compute_client.insert(project=project, zone=zone, body=config)
result = operation.result()

print(f"Instance created: {result.name}")
