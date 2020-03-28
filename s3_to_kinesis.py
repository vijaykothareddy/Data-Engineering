import boto3
import json
#from urllib.parse import unquote_plus
import time
import csv

s3 = boto3.client('s3')
kinesis = boto3.client('kinesis')

def lambda_handler(event, context):
    if event:
       # Read bucketname, filename from event record
       file_obj = event["Records"][0]
       bucketname = file_obj['s3']['bucket']['name']
       filename = file_obj['s3']['object']['key']
       
       # Get referenc to file on s3 bucket
       fileObj = s3.get_object(Bucket=bucketname, Key=filename)
       
       # Convert the data in file
       file_content = fileObj["Body"].read().decode('utf-8')
      
       # put the record to kinesis
       
       kinesis.put_record(Data=bytes(file_content, 'utf-8'), StreamName='my_fake_stream',PartitionKey='vjfirst')
       

    return "thanks"