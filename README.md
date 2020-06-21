# Data Engineering with AWS
Data Pipe Lines with AWS

# Introduction & Goals

I have been using on-premise IT infrastructure platform for storing and processing the Data.

To address real time analytics business problem,  I utilized AWS serverless architecture to design and develop data pipeline.


This project took the general [blueprint](https://github.com/andkret/Cookbook/blob/master/sections/01-Introduction.md#my-data-science-platform-blueprint) as a reference to

identify the tools required at regular intervale of pipeline based on kind of data Volume, Velocity and Variation.

This Project has mainly classified into three phases,

  - Initial phase : Data Set selection, based on the industry research.
  - Second Phase : Designing and developing the pipeline with tools.
  - Third Phase : Documentation for the project and grouping the code used in various phases of development

  #### About my data set

  I researched as mentioned in the [blog post](https://www.teamdatascience.com/post/dba-focus-to-work-as-data-engineer) results of it helped to narrow down my option to the banking industry.


  I selected credit card complaints data and selection process has been explained in my [blog](https://www.teamdatascience.com/post/data-sets)
  
  #### Tools that I used 

  Quick snapshot of tools used in this project are captured in below picture,


  ![](https://github.com/vijaykothareddy/Data-Engineering/blob/master/Images/tools_used.jpg)

*Amazon Web Services, Docker for Amazon Machine Images, Airflow on Ubuntu, Python IDE and BI tools*
  #### What i did

  I utilized managed services provided by Amazon Web Services, which offer greater capability at scale,

  Data pipelines in this project uses, **Lambda** as a processing environment.  To handle streaming data **Kinesis** will come to rescue and they acts as a buffer too.  
  
  Eventually data is stored in warehouse, NoSql database or file system type of storage solutions.

  Visualization tools or analytics products are connected to these data sources and used for data analytics.

  #### Conclusion

  Basically this projects has been designed by assuming the huge data size, so that the cloud resources are economically scaled.


# Contents

- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
- [Pipelines](#pipelines)
- [Demo](#demo)
- [Conclusion](#conclusion)
- [Follow Me On](#follow-me-on)
- [Appendix](#appendix)


# The Data Set
- [About my Data Set](Contents/Dataset.MD)
- [Why did I choose it?](Contents/Dataset.MD)
- [What do you like about it?](Contents/Dataset.MD)
- [What is problematic?](Contents/Dataset.MD)
- [What do you want to do with it?](Contents/Dataset.MD)

# Used Tools
- [Tools I used](Contents/Tools.MD)
- [How do they work]((Contents/Tools.MD))
- [Why I choose them](Contents/Tools.MD)
- [Tools Setup](Contents/Tools.MD)

# Pipelines
- [Stream Processing](Contents/Pipelines.MD)
  - [Storing Data Stream](Contents/Pipelines.MD)
  - [Processing Data Stream](Contents/Pipelines.MD)
- [Batch Processing](Contents/Pipelines.MD)
- [Visualizations](Contents/Pipelines.MD)

# Demo
- You could add a demo video here
- Or link to your presentation video of the project

# Conclusion
Write a comprehensive conclusion.
- I created end-to-end data pipeline to deliver real time analytics with data available to BI system in minutes of latency.


#### Things I learned 
I learnt about 
  - Different AWS Services like Lambda, Redshift, DynamoDB and other
  - User roles and policies
  - How to encode and decode the data while dealing with multiple AWS services.
  - How to integrate services with Python using BOTO3.
#### Challenges that I Faces

  - NoSQL
  I picked DynamoDB as one of my storage option. Data modelling is quite opposite to traditional RDBMS models, Amazon re invent videos and blogs helped me to understand about DynamoDB.
  - Python Package
  To use any Python package other than BOTO3 need to packaged with Lambda function.  

# Follow Me On


[my Linkedin profile](https://www.linkedin.com/in/kvbr/)

# Appendix

[Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
