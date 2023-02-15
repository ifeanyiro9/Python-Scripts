import boto3

ec2_resource = boto3.resource('ec2', region_name='us-east-1')

def lambda_handler(event, content):

    instances = ec2_resource.instances.all() #Create iterable of all Instances.

    for instance in instances: #interate through all intances
    
        instance_state = instance.state["Name"] #get instance state
        tag = instance.tags #get instance tags
    
        for tag in instance.tags:
            if ("Dev" == tag['Value']) & (instance_state == 'running'): #check if instance is running and if tag is is Dev Instance
                stop_instance = instance.stop() #Stop instance if condition is satisfied
            
                print('Stopped your Dev instance - ' + str(instance.id))
    
    return "success"