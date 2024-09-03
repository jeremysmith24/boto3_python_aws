import boto3  # Import the Boto3 library to interact with AWS services

# Define the ID of the route table to associate
route_table_id = 'rtb-0d477894f685ca7b4'

# Define the ID of the subnet to associate with the route table
subnet_id = 'subnet-01ec259bbe414bdd9'

# Create an EC2 client to interact with the EC2 service
ec2 = boto3.client('ec2')

# Call the associate_route_table method to associate the specified route table with the subnet
association = ec2.associate_route_table(
    RouteTableId=route_table_id,  # ID of the route table
    SubnetId=subnet_id  # ID of the subnet
)

# Print the ID of the association from the response
print(association["AssociationId"])
