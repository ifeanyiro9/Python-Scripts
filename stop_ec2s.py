import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

instances = ec2_resource.instances.all()

for instance in instances:
    instance_state = instance.state["Name"]
    print(instance.id)
    print(instance_state)
    
  #  if instance_state == 'running':
    #   responce = ec2_client.stop_instances(InstanceIds=[instance])
       # print('Stopped your instance ' + str(instance))
        
