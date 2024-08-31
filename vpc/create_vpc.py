import boto3

# Initialize the EC2 client using boto3
ec2 = boto3.client('ec2')

# Create a VPC with the specified CIDR block
vpc = ec2.create_vpc(CidrBlock='12.0.0.0/16')

# Print the VPC ID of the newly created VPC
print(vpc["Vpc"]["VpcId"])
