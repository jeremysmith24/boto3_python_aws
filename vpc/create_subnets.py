import boto3  # Import the Boto3 library to interact with AWS services

# Define the CIDR block for the new subnet
cidr_block = '12.0.1.0/24'

# Define the ID of the VPC where the subnet will be created
vpc_id = 'vpc-0793c0541201e03a6'

# Create an EC2 client to interact with the EC2 service
ec2 = boto3.client('ec2')

# Call the create_subnet method to create a new subnet with the specified CIDR block and VPC ID
subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc_id)

# Print the ID of the created subnet from the response
print(subnet["Subnet"]["SubnetId"])
