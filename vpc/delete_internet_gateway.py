import boto3 

ec2 = boto3.client('ec2')

interenet_gateway_id = 'igw-0137e438d7bd619f7'

ec2.delete_internet_gateway(
    InternetGatewayId=interenet_gateway_id,
)

