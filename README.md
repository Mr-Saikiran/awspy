# awspy
Python Scripts for AWS boto3

#### delete_ebs.py

The script below can be used to iterate through the EBS volumes within an AWS account's region to identify EBS volumes that are not attached to EC2 instances. Once these unattached volumes are identified, the script below deletes the volume unless the volume has a tag of Name=DND.
This script can be run manually or as a lambda.

#### stop_ec2.py

lambda script to stop ec2 instance

#### start_ec2.py

manual script to start instance using instance id