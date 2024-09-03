import boto3

# Initialize the EC2 client using boto3
ec2 = boto3.client('ec2')

# Describe all internet gateways in your AWS account
response = ec2.describe_internet_gateways()

# Iterate over each internet gateway in the response
for ig in response["InternetGateways"]:
    # Print the Internet Gateway ID
    print(ig["InternetGatewayId"])
    
    # Iterate over each attachment associated with the internet gateway
    for attachment in ig["Attachments"]:
        # Print the VPC ID and the state of the attachment (e.g., attached or detached)
        print(attachment["VpcId"], attachment["State"])
