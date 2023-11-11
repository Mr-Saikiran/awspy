import boto3
session = boto3.Session(profile_name='saml',  region_name='us-east-1')
ec2 = session.resource('ec2')
 
# Volume states:  (creating | available | in-use | deleting | deleted | error )
 
for vol in ec2.volumes.all():
    if  vol.state=='available':
        if vol.tags is None:
            vid=vol.id
            v=ec2.Volume(vol.id)
            v.delete()
            print "Deleted " +vid
            continue
        for tag in vol.tags:
            if tag['Key'] == 'Name':
                value=tag['Value']
                if value != 'DND' and vol.state=='available':
                    vid=vol.id
                    v=ec2.Volume(vol.id)
                    v.delete()
                    print "Deleted " +vid