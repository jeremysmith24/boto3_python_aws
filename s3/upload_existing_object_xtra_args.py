import boto3

s3 = boto3.client("s3")

#with open("test_text.txt", "rb") as f:
#    s3.put_object(Bucket="jsmith-boto3-08262024", Key="test_text.txt", Body=f, ContentType="text/plain")

s3.upload_file('test_text.txt', 'jsmith-boto3-08262024', 'test_text_upload.txt', ExtraArgs={'ContentType':'text/plain'})