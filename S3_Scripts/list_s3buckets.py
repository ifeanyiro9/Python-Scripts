import boto3

s3_resource = boto3.resource("s3")
buckets = s3_resource.buckets.all() #get all buckets

num = 1

for bucket in buckets: #loop through buckets
    print("Bucket", num, "=", bucket.name) #print bucket names
    num += 1
    
    
    
    