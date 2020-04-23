* [Tools Used](#Tools-Used)
  - [AWS](#AWS-products-used)
  - [Docker](#Docker)
  - [Apache Airflow](#Apache-Airflow)
  - [Power BI](#Power-BI)
  - [Coding](#Coding)
  - [IDE](#IDE)
* [How they work](#How-they-work)
  - Lambda and S3
  - Kinesis and Dynamodb
  - EC2, RDS
* [Tools set up method](#Tools-set-up-method)
# Tools Used

My technical stack decision was made based on the results of researching the job postings.  AWS skills were on demand on most of the job description and it is used widely around the world.
### AWS products used
* Amazon S3
* Amazon Kinesis Data Streams
* AWS Lambda
* Dynamo DB
* Amazon RDS
* Amazon EC2

### Docker
Docker is becoming more popular for its easy to use image concept.  Literally you can get any kind of operating environment by, just pulling a container image on to your host OS.

### Apache Airflow
To Orchestrate work flow of task for you pipeline, Apache Airflow offers to build your Dynamic Acyclic Graphs(DAG) of your tasks and its dependencies.

### Power BI
Microsoft Power BI is the visualization tool, has integrated with wide variety of datasources and you can get the free desktop version to play and devolop visualization.
Its great tool with in-memory technology for transforming power queries and applying to dataset.

### Coding
Python BOTO3 package is integrated with all the AWS resources additionally you can package any class with you AWS lambda processing environment.


I use python for data manipulation and to develop custom classes.
SQL used to interact with relational databases.

* Python
* SQL
### IDE

There are many Integrated Development environments, I use VS code for python developments and you can also download AWS toolkit.
AWS toolkit helps to connect to cloud and interact with Lamda functions.
* VS Code
* Jupiter Note Book

# How they work

Lambda function invocation based on file creation event in S3,
* [head on to the blog post, to know how these are implemented](https://www.teamdatascience.com/post/how-to-process-simple-data-stream-and-consume-with-lambda)

Kinesis acts as a buffer for streaming data
* [click the link to see how steam data is stored to a NoSQL store](https://www.teamdatascience.com/post/how-to-write-kinesis-data-stream-to-dynamodb)

Amazon EC2 is used to spin up a virtual machine with preferred operating system, either you can host you application or run multiple applications by pulling docker images.

Amazon RDS is a SAAS service where you can run relation database management systems like SQL Server, Oracle and MySQL

# Tools set up methods

AWS stack are configured using management console.
One should create a AWS account, which is a root user.
Best practice is to create an IAM user and assign required privileges, prefer to use IAM user for interacting with AWS resources.  

* python code to connect
```python
import boto3
s3 = boto3.resource(
                     's3',
                      region_name='ap-southeast-2',
                      aws_access_key_id=<>,
                      aws_secret_access_key=<>
                      )
```
<dl>
<dt> you should mask AWS access key's before uploading scripts to internet ( blogs, git and other), once exposed any one can access your cloud account </dt>
</dl>

