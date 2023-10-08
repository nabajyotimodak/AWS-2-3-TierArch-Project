####### Lambda Function for Runtime - Python3.9 To STOP EC2 automatically

import boto3
region = 'us-east-1'
instances = ['i-04aef953ced4008a9', 'i-04aedskjgdcd45j45']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))



####### Lambda Function for Runtime - Python3.9 To START EC2 automatically

import boto3
region = 'us-east-1'
instances = ['i-04aef953ced4008a9']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))



###########################################################################################

#  Important Link used for this project:

#   https://cloudbytes.dev/aws-academy/how-to-install-and-run-wordpress-on-an-ec2-instance

#   https://repost.aws/knowledge-center/start-stop-lambda-eventbridge

#   https://saturncloud.io/blog/how-to-auto-shutdown-and-start-amazon-ec2-instance/

#   https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html

#############################################################################################