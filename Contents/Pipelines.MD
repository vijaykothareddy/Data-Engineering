* [Pipelines](#Pipelines)
  - [Stream Processing](#stream-processing)
  - [Batch Processing](#Batch-processing)
  - [Visualization]
# Pipelines

Data Analytics is derived form various data sources and intermediate transformations.  Pipeline is created with *connect, storage, process, buffer and visualization* elements used to achieve organizational data goal.
## Stream Processing

Steam Processing is analyzing the data in real time.  Log from application server, click stream from websites, mobile apps and IOT learn about application, products and customers with the help of streaming data solutions.

I created a pipe line to visualize credit cards complaints stream.

![](https://github.com/vijaykothareddy/Data-Engineering/blob/master/Contents/Stream_Processing.jpg)

Let me take you through the solution,

### Connect

I manually crated a python script to upload JSON file to AWS S3 bucket, which acts as my connect stream data source.

### Process

AWS lambda function is invoked for S3 bucket object cerated event.  File content will be transferred as record to Kinesis stream.

### Buffer

Kinesis Data Stream acts as a buffer for real time data and Kinesis firehouse is my consumer, which acts as  data transformation service and delivers data to Amazon Redshift.

### Storage

Data is eventually stored in a Redshift, which is connected to analytics tools.

### Visualization

Power BI desktop has been configured to AWS redshift data source to answer some of the analytical queries for business.

## Batch Processing
