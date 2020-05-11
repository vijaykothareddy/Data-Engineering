* [Connect](#Connect)
* Buffer
* Processing
* [Storage](#Storage)
* Visualization




## Connect
## Buffer
## Processing
## Storage

Storage solution depends on the purpose.  I stored my CSV data sets on AWS S3, inturn acts as data source for my pipeline.

Down the line I am writing the each row of CSV data to a NoSQL database called DynamoDB.

### Security

To use DynamoDB programatically you need *Access Keys*.


Access Key = Access Key ID + Secret Access Key

IAM user must have application-autoscaling permission which is provided by AWS managed policy DynamoDBFullAccess
## Visualization
