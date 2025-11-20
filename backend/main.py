import boto3, json

def fetch_ec2_info():
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    instances = ec2.describe_instances()
    data = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            data.append({
                'InstanceId': instance['InstanceId'],
                'State': instance['State']['Name'],
                'InstanceType': instance['InstanceType'],
                'LaunchTime': str(instance['LaunchTime']),
                'PublicIP': instance.get('PublicIpAddress', 'N/A')
            })
    return data

def fetch_s3_info():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = []
    for bucket in response['Buckets']:
        name = bucket['Name']
        location = s3.get_bucket_location(Bucket=name)['LocationConstraint']
        buckets.append({'BucketName': name, 'Region': location})
    return buckets

# Combine data
ec2_data = fetch_ec2_info()
s3_data = fetch_s3_info()

final_data = {
    'ec2': ec2_data,
    's3': s3_data
}

print(json.dumps(final_data, indent=4))

with open('data/aws_data.json', 'w') as f:
    json.dump(final_data, f, indent=4)
