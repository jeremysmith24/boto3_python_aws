import boto3
from typing import List, Dict, Any

def get_vpc_information(client: boto3.client, filter: List[Dict[str, Any]] = []) -> None:
    """
    Retrieves and prints basic information about VPCs in your AWS account.

    :param client: The EC2 client object.
    :param filter: A list of filters to apply when describing VPCs. Default is an empty list.
    """
    # Describe VPCs using the provided filters (if any)
    response = client.describe_vpcs(Filters=filter)
    
    # Iterate over each VPC in the response and print its ID, CIDR block, and default status
    for vpc in response["Vpcs"]:
        print(vpc["VpcId"], vpc["CidrBlock"], vpc["IsDefault"])

def get_vpc_name(client: boto3.client, filter: List[Dict[str, Any]] = []) -> None:
    """
    Retrieves and prints the 'Name' tag of VPCs in your AWS account, if it exists.

    :param client: The EC2 client object.
    :param filter: A list of filters to apply when describing VPCs. Default is an empty list.
    """
    # Describe VPCs using the provided filters (if any)
    response = client.describe_vpcs(Filters=filter)
    
    # Iterate over each VPC in the response
    for vpc in response["Vpcs"]:
        # Check if the VPC has any tags
        if "Tags" in vpc:
            # Iterate over each tag to find the 'Name' tag and print its value
            for tag in vpc["Tags"]:
                if tag["Key"] == "Name":
                    print(tag["Value"])

if __name__ == '__main__':
    # Initialize the EC2 client using boto3
    ec2 = boto3.client("ec2")

    # Define a filter to get only the default VPC
    Filters = [{'Name': 'isDefault', 'Values': ['true']}]

    # Call the functions to get VPC information and names
    get_vpc_information(ec2)
    get_vpc_information(ec2, Filters)
