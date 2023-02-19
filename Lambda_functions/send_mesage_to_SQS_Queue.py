import json
import boto3
from datetime import datetime

current_date_time = datetime.now()
sqs = boto3.resource('sqs', region_name='us-east-1')

def lambda_handler(event, content):
    
    queue = sqs.get_queue_by_name(QueueName='rextech_queue') #get the queue

    date_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S") #get the current date and time
    message = ("The current date and time at point of trigger was " + str(date_time) + ".") #concatonate strings to create a custom message
    
    
    responce = queue.send_message(MessageBody = message) #send message to queue

    return {
        "statusCode": 200,
        'body': json.dumps(message)
    }
