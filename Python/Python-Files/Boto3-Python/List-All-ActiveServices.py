import boto3

def list_active_services():
    # Create a session using the default profile in your AWS credentials file
    session = boto3.Session()

    # Initialize the AWS service client for the AWS Resource Groups Tagging API
    client = session.client('resourcegroupstaggingapi')

    # Use the client to list all tagged resources
    response = client.get_resources()

    # Extract active services
    active_services = set()
    for resource in response['ResourceTagMappingList']:
        if 'aws:service' in resource['Tags']:
            active_services.add(resource['Tags']['aws:service'])

    return active_services

if __name__ == "__main__":
    active_services = list_active_services()
    print("Active Services in AWS:")
    for service in active_services:
        print(service)
