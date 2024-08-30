import boto3
from list_objects import list_object_keys

# Define the S3 bucket and key prefix
bucket = 'jsmith-boto3-08262024'
key = '/folder1'

# Initialize the S3 client using boto3
s3 = boto3.client('s3')

def delete_object(client, bucket, key):
    """
    Deletes a single object from an S3 bucket.

    :param client: The S3 client object.
    :param bucket: The name of the S3 bucket.
    :param key: The key (path) of the object to delete.
    :return: The response from the S3 delete_object API call.
    """
    # Call the delete_object API to remove the specified object
    response = client.delete_object(
        Bucket=bucket,
        Key=key
    )

    # Return the response from the API call
    return response

def delete_objects(client, bucket, keys):
    """
    Deletes multiple objects from an S3 bucket.

    :param client: The S3 client object.
    :param bucket: The name of the S3 bucket.
    :param keys: A list of keys (paths) of the objects to delete.
    :return: The response from the S3 delete_objects API call.
    """
    # Create a list of dictionaries, each containing a 'Key' for the objects to delete
    objects = [{'Key': key} for key in keys]

    # Call the delete_objects API to remove the specified objects
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )

    # Return the response from the API call
    return response

def delete_objects_non_recursive(client, bucket, keys, prefix):
    """
    Deletes multiple objects from an S3 bucket, but only those directly under the specified prefix (non-recursive).

    :param client: The S3 client object.
    :param bucket: The name of the S3 bucket.
    :param keys: A list of keys (paths) of the objects to delete.
    :param prefix: The prefix (path) under which to delete objects.
    :return: The response from the S3 delete_objects API call.
    """
    # Filter keys to include only those directly under the specified prefix (non-recursive)
    keys = [key for key in keys if '/' not in key[len(prefix):]]

    # Create a list of dictionaries, each containing a 'Key' for the objects to delete
    objects = [{'Key': key} for key in keys]

    # Call the delete_objects API to remove the filtered objects
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )

    # Return the response from the API call
    return response

if __name__ == '__main__':
    # Define the S3 bucket name and key prefix for deletion
    bucket = 'jsmith-boto3-08262024'
    prefix = 'folder/folderA/'

    # Initialize the S3 client
    s3 = boto3.client("s3")

    # List all objects under the specified prefix
    keys = list_object_keys(s3, bucket, prefix=prefix)

    # Call the delete_objects_non_recursive function to delete objects directly under the prefix
    delete_objects_non_recursive(s3, bucket, keys, prefix) 
