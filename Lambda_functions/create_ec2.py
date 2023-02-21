import json
import boto3


def lambda_handler(event, content):
    ec2_resource = boto3.resource('ec2') #Invoke the resource for EC2
   
    instances = ec2_resource.create_instances( 
        #Arguments to launch EC2 Instances
        MinCount = 3,
        MaxCount = 3,
        ImageId = 'ami-0aa7d40eeae50c9a9',
        InstanceType ='t2.micro',
        KeyName = 'levelupkeypair',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name','Value': 'Dev Instance Server'}, 
                {'Key': 'Environment','Value': 'Dev'}]
            
            }
        ]
    )
    
    message = "3 EC2s has been created."

    return {
            "statusCode": 200,
            'body': json.dumps(message)
        }

