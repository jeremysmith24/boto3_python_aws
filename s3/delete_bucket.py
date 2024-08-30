import boto3

def empty_bucket(client, bucket):
    """
    Empties the specified S3 bucket by deleting all objects within it.

    :param client: The S3 client object.
    :param bucket: The name of the S3 bucket to empty.
    """
    # List objects in the bucket, using version 2 of the list_objects API
    response = client.list_objects_v2(Bucket=bucket)

    # Check if the bucket contains any objects
    if "Contents" in response:
        # Prepare a list of dictionaries, each containing the 'Key' for objects to delete
        objects = [{'Key': content["Key"]} for content in response["Contents"]]
        
        # Delete the listed objects from the bucket
        response = client.delete_objects(
            Bucket=bucket,
            Delete={
                'Objects': objects
            }
        )

        # Continue deleting objects if the response indicates more objects are present
        while response.get("NextContinuationToken"):
            # List the next batch of objects using the continuation token
            response = client.list_objects_v2(Bucket=bucket, 
                                              ContinuationToken=response["NextContinuationToken"])
            
            # Prepare the next batch of objects to delete
            objects = [{'Key': content["Key"]} for content in response["Contents"]]

            # Delete the next batch of objects
            response = client.delete_objects(
                Bucket=bucket,
                Delete={
                    'Objects': objects
                }
            )

# Initialize the S3 client using boto3
s3 = boto3.client('s3')

# Define the S3 bucket name
bucket = 'jsmith-boto3-08262024'

# Call the function to empty the bucket
empty_bucket(s3, bucket)

# Delete the now-empty bucket
response = s3.delete_bucket(
    Bucket=bucket
)
