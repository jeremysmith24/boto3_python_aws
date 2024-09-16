import boto3

route_table_id = 'rtb-01b69a83900331c14'
gateway_id = 'igw-0137e438d7bd619f7'

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=gateway_id,
    RouteTableId=route_table_id,
)

