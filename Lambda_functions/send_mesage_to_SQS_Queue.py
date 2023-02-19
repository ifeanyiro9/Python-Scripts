import json
import boto3
from datetime import datetime

current_date_time = datetime.now()
sqs = boto3.resource('sqs', region_name='us-east-1')

def lambda_handler(event, content):
    
    date_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
    message = ("The current date and time at point of trigger was " + str(date_time) + ".")
    
    responce = sqs.send_message(MessageBody = message)

    return {
        "status_Code" : 200,
        'Message_Sent' : json.dumps(message)
        }
