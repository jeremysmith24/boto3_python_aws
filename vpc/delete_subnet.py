import boto3

subnet_id = 'subnet-01ec259bbe414bdd9'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)

