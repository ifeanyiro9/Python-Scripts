import boto3

s3 = boto3.client('s3')

s3.delete_object(Bucket='boto3bucketluit11', Key='test2.txt')
