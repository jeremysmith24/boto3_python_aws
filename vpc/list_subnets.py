import boto3

# Initialize the EC2 client using boto3
ec2 = boto3.client('ec2')

# Describe all subnets in your AWS account
response = ec2.describe_subnets()

# Iterate over each subnet in the response
for subnet in response["Subnets"]:
    # Print the CIDR block, Subnet ID, and VPC ID of each subnet
    print(subnet['CidrBlock'], subnet['SubnetId'], subnet['VpcId'])
