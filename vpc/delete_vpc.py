import boto3

vpc_id = 'vpc-0793c0541201e03a6'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)

