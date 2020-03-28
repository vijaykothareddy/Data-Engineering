import boto3
import base64

# Accessing the resource for writing stream data
s3 = boto3.resource(
                     's3',
                      region_name='ap-southeast-2',
                      aws_access_key_id=<>,
                      aws_secret_access_key=<>
                      )
ev_lst = []
def lambda_handler(event, context):
    
    for record in event['Records']:
       
       #Kinesis data is base64 encoded so decode here
       payload=base64.b64decode(record["kinesis"]["data"])
       ev_lst.append(payload)

# writing data to S3   
    s3.Object('kotharv-target', 'test.txt').put(Body=str(ev_lst))
