import json
import boto3
import os

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']
NAME_VLAUE = os.environ['NAME_VALUE']
ENV_VALUE = os.environ['ENV_VALUE']

ec2_resource = boto3.resource('ec2') #Invoke the resource for EC2

def lambda_handler(event, content):

    instances = ec2_resource.create_instances( 
        #Arguments to launch EC2 Instances
        MinCount = 3,
        MaxCount = 3,
        ImageId = AMI,
        InstanceType = INSTANCE_TYPE,
        KeyName = KEY_NAME,
        SubnetId = SUBNET_ID,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name','Value': NAME_VLAUE}, 
                {'Key': 'Environment','Value': ENV_VALUE}]
            
            }
        ]
    )
    
    message = "3 EC2s has been created."

    return {
            "statusCode": 200,
            'body': json.dumps(message)
        }

