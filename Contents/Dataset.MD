# About My Dataset
I used credit card complaints data set for my project. It has 18 columns and 80k rows. Columns are of Date, Text and Number types.  The dataset is a CSV file. 
You can find the dataset here, [Credit Card Complaints]( https://data.world/dataquest/bank-and-credit-card-complaints)

have a look at quick view of dataset,
![](https://github.com/vijaykothareddy/Data-Engineering/blob/master/Contents/data_view.PNG)
# Why i choose it?
When I started to peruse Data Engineering, I did a research on industry based on jobs available on job portal.  Banking and Telecommunication are the top two sectors posting jobs locally.  It should be relevant to do hands on project relating to these industries and that made made me to narrow down the data set.
# What i like in the dataset?
Its a good candidate to draw some insights and calculate statistics like average, total complaints group by location and time series analysis.
# What is Problematic?
One of the column 'Sub-Issue' doesn't have any values, we need to manually impute values.  Imputation can be based on context of dataset usage.
Eg: In my case I collected the Sub-Issue types and populated the column randomly.
# What i want to achieve?
I will use this data as a source for my data pipelines to address some of the problem statements
1. Analytics with Steaming data 
