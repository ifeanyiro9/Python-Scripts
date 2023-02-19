import json
import boto3

sqs = boto3.resource('sqs', region_name='us-east-1')

def lambda_handler(event, content):
    
    
    return "success"
