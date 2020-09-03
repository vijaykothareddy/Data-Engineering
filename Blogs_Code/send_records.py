import boto3
import json
from urllib.parse import unquote_plus
import time
import csv
import base64

s3 = boto3.client('s3')
kinesis = boto3.client('kinesis')

def lambda_handler(event, context):
    my_records = []
    
    
    if event:
        # Read bucketname, filename from event record

        file_obj = event["Records"][0]
        bucketname = file_obj['s3']['bucket']['name']
        filename = file_obj['s3']['object']['key']

        # Get referenc to file on s3 bucket

        fileObj = s3.get_object(Bucket=bucketname, Key=filename)
       
        # Reading data with decoding bytes

        file_content = fileObj["Body"].read().decode('utf-8')

        # Split to extact each record to a list

        file_rows = file_content.split()

        # prepare the record and add to record list
        
        for row in range(len(file_rows)):
            pk = 'vjcool'+str(row)
            record = {
                'Data': bytes(file_rows[row], 'utf-8'),
                
                'PartitionKey': pk
            }
            my_records.append(record)
       
        
        # put the record to kinesis
       
        kinesis.put_records(Records= my_records, StreamName='my_cc_data')
        
        
       

    return "thanks"