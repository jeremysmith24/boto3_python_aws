import boto3  # Import the Boto3 library to interact with AWS services

# Define the ID of the VPC where the route table will be created
vpc_id = 'vpc-0793c0541201e03a6'

# Create an EC2 client to interact with the EC2 service
ec2 = boto3.client('ec2')

# Call the create_route_table method to create a new route table for the specified VPC
routeTable = ec2.create_route_table(VpcId=vpc_id)

# Print the ID of the created route table from the response
print(routeTable['RouteTable']['RouteTableId'])
