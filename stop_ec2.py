import boto3

def stop_ec2_instance(instance_id):
    ec2 = boto3.client('ec2')

    try:
        response = ec2.stop_instances(
            InstanceIds=[instance_id],
            DryRun=False
        )
        print(f"Instance {instance_id} is stopping. Response: {response}")
    except Exception as e:
        print(f"Error stopping instance {instance_id}: {str(e)}")

if __name__ == "__main__":
    instance_id = 'i-xxxxxx'
    stop_ec2_instance(instance_id)
