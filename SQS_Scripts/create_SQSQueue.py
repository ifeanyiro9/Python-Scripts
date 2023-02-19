import boto3

sqs = boto3.resource('sqs') #get service resource

queue = sqs.create_queue(QueueName = 'rextech_queue') #create que with custom name

print("The new SQS queue", queue.attributes['QueueArn'].split(':')[-1], "has been created and the queue URl is", queue.url)

