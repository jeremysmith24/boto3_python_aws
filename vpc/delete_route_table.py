import boto3

route_table_id = 'rtb-0d477894f685ca7b4'

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)

