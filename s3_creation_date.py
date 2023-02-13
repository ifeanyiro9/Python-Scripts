import boto3

s3_resource = boto3.client("s3")

for bucket in s3_resource.list_buckets()["Buckets"]:
    print("Bucket name is", bucket["Name"], "and it's creation date was", bucket["CreationDate"])
