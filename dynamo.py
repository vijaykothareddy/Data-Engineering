
import boto3
import json
import base64

# Accessing the resource for writing stream data
s3 = boto3.resource(
                     's3',
                      region_name='<>',
                      aws_access_key_id='<>',
                      aws_secret_access_key='<>'
                      )
dynamodb = boto3.resource('dynamodb',
                            region_name='<>',
                      aws_access_key_id='<>',
                      aws_secret_access_key='<>')
                      
table = dynamodb.Table('cc_complaint')
ev_lst = []
payload = b'low'

def lambda_handler(event, context):
    #print(event)
    for record in event['Records']:
       
       # Kinesis data is base64 encoded so decode here
       
       payload=base64.b64decode(record["kinesis"]["data"])
       
       
    # Writing data to Dynamo   
    
    main_lst = payload.decode().split('\r\n')
    
    # Assign first index value as keys
    keys = main_lst[0].split(',')
    #print(len(main_lst))
    #print(main_lst)
    # Loop through the records in uploaded CSV file from index 1
    for j in range(1, len(main_lst)-1):
        
        # Split each list
        val = main_lst[j].split(',')
        arr ={}
        print("lenth of values:",len(val))
        print("length ok keys:",len(keys))
        # Loop through keys to create item
        for i in range(len(val)):
            key = keys[i]
            value = val[i]
            if value is None:
                value = "5"
            if key == 'Complain_ID':
                print('yes complaint id')
                arr[key] = int(value)
            else:
                arr[key] = value
        print(arr)
        table.put_item(Item = arr)    
    #s3.Object('kotharv-target', 'test.txt').put(Body=payload)
    
       
    
   