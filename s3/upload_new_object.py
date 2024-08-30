import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket='jsmith-boto3-08262024',
              Key='folder/folderA/folder1/test_text_str.txt',
              Body='Hey this is a string',
              ContentType='text/plain')