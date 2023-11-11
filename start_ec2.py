import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_id = 'i-xxxxxxx'  # Replace with your EC2 instance ID
    
    response = ec2.start_instances(
        InstanceIds=[instance_id],
        DryRun=False
    )

    print(response)
