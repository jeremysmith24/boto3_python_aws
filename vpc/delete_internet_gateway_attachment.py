import boto3

internet_gateway_id = 'igw-0137e438d7bd619f7'
vpc_id = 'vpc-0793c0541201e03a6'

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)

