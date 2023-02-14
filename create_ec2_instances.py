import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

instances = ec2_resource.create_instances(
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

print(instances)