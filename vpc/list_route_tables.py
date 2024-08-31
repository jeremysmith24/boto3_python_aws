import boto3

# Initialize the EC2 client using boto3
ec2 = boto3.client('ec2')

def describe_route_tables():
    """
    Retrieves and prints information about route tables in your AWS account, including
    the VPC ID, Route Table ID, Route Table Association ID, Subnet ID (if applicable),
    and route details like Destination CIDR Block and Gateway ID.
    """
    # Describe all route tables in your AWS account
    response = ec2.describe_route_tables()

    # Iterate over each route table in the response
    for routeTable in response["RouteTables"]:
        # Print the VPC ID and Route Table ID of each route table
        print(routeTable["VpcId"], routeTable["RouteTableId"])

        # Iterate over each association in the route table
        for association in routeTable["Associations"]:
            # Print the Route Table Association ID
            print(association["RouteTableAssociationId"])
            
            # If the association is associated with a subnet, print the Subnet ID
            if "SubnetId" in association:
                print(association["SubnetId"])
        
        # Iterate over each route in the route table
        for route in routeTable["Routes"]:
            # Print the Destination CIDR Block and Gateway ID for each route
            print(route["DestinationCidrBlock"], route["GatewayId"])

# Call the function to describe and print route table information
describe_route_tables()
