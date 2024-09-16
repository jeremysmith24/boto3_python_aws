import boto3

rout_table_id = 'rtb-01b69a83900331c14'

ec2 = boto3.client('ec2')

ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=rout_table_id,
)

