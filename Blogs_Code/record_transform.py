import base64
import json
from datetime import datetime

# Incoming Event
def lambda_handler(event, context):
    output = []
    output_record = {}
    
    # Loop through records in incoming Event
    for record in event['records']:

        # Extract message
        
        message = base64.b64decode(record['data']).decode("UTF-8")

        # Construct output and add to the list
   
        rec = json.loads(message)
        rec['l3'] = 19
        
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(bytes(json.dumps(rec), 'utf-8'))}
        output.append(output_record)

    return {'records': output}
   