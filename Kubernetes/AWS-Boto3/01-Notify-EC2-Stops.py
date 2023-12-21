# Required AWS Resources
'''
1: EC2
2: SNS topics
3: IAM Role For Lambda to Access SNS Topics
4: Lambda
5: CloudWatch Events - To Schedule

Iam Roles
Access for CloudWatch
Access for Lambda Function

Aws Cloud watch trigger
create new rule
new ruule name
event pattent
rule type
resource ec2

'''
from mailbox import Message
import boto3

client = boto3.client('sns')

def lambda_handler(event,context):
    topic_arn = "arn:aws:sns:us-east-1:711638438109:prod-alerts-design"
    message = "prod server stopped pleaasse look into it "
    client.publish(TopicArn=topic_arn,Message=message)