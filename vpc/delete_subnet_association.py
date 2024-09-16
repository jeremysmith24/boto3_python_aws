import boto3

# Define the ID of the route table to work with.
route_table_id: str = 'rtb-01b69a83900331c14'

# Create an EC2 client using Boto3 to interact with the AWS EC2 service.
ec2 = boto3.client('ec2')

# Describe the specified route table by its ID.
response: dict = ec2.describe_route_tables(
    RouteTableIds=[
        route_table_id,  # The route table ID to fetch details for.
    ],
)

# Iterate through the associations within the first route table returned.
for association in response["RouteTables"][0]["Associations"]:
    # Check if the association is not the main route table.
    if not association["Main"]:
        # Get the association ID for non-main route tables.
        association_id: str = association["RouteTableAssociationId"]
        print(association_id)  # Print the association ID.

        # Disassociate the non-main route table from the subnet.
        ec2.disassociate_route_table(
            AssociationId=association_id,  # The association ID to disassociate.
        )

