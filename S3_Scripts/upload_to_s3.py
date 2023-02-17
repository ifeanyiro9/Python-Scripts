import boto3

s3_resource = boto3.resource('s3')

s3_resource.Bucket('boto3bucketluit11').upload_file('/home/ec2-user/environment/test.txt', 'test2.txt')