# Data Engineering with AWS
Data Pipe Lines with AWS

# Introduction & Goals
The project is about building data pipeline on cloud serverless platform.  It takes the general [blueprint](https://github.com/andkret/Cookbook/blob/master/sections/01-Introduction.md#my-data-science-platform-blueprint) as a reference for selecting data sources, processing and buffer framework, storage and visualization tools.

This Project has mainly classified into three phases,

  - Initial phase : Dataset selection, based on the industry research.
  - Second Phase : Designing and developing the pipeline with tools and data source.
  - Third Phase : Documentation for the project and grouping the code used in various phases of development

  #### About my data set

  I researched as mentioned in the [blog post](https://www.teamdatascience.com/post/dba-focus-to-work-as-data-engineer) results of it helped to narrow down my option to the banking industry.


  I selected credit card complaints data and selection process has been explained in my [blog](https://www.teamdatascience.com/post/data-sets)
  
  #### Tools that I used 

  Quick snapshot of tools used in this project are captured in below picture,


  ![](https://github.com/vijaykothareddy/Data-Engineering/blob/master/Images/tools_used.jpg)

*Amazon Web Services, Docker for Amazon Machine Images, Airflow on Ubuntu, Python IDE and BI tools*
  #### What i did

  I choose managed services provided by Amazon, which are server less environments and offer greater capability at scale,

  Data pipelines in this project uses, **Lambda** as a processing environment.  To handle streaming data **Kinesis** will come to rescue and they acts as a buffer too.  
  
  Eventually data is stored in warehouses, NoSql or file system storage solution.

  Visualization tools or analytics products are connected to these datasources and used for data analytics.

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
- [About my dataset](Contents/Dataset.MD)
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
- How did this project turn out
- What major things have you learned
- What were the biggest challenges

# Follow Me On

Linkedin  [linkedin.com/in/kvbr]

# Appendix

[Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
