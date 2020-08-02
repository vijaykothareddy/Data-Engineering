# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
# Datetime and other 
from datetime import datetime
import boto3, json

# Default arguments and can be overwritten at operator initialization
default_args = {
        'owner': 'Vijay',
        'depends_on_past': False,
        'start_date': datetime(2020,4,17),
        'email': ['@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
}

# DAG initialization
dag = DAG(
        'invocation_lambda',
        default_args=default_args,
        description='invoke a lambda in dev aws instance'
)

# Function

def lambda1(ds,**kwargs):
        lambda_client = boto3.client('lambda', 
                                 region_name='',
                                 aws_access_key_id='',
                                 aws_secret_access_key='')
        response_1 = lambda_client.invoke(FunctionName='myAirflowTest',InvocationType='RequestResponse')
        print ('Response--->' , response_1)

# Task

start = DummyOperator(task_id='Begin_execution',  dag=dag)

t1 = PythonOperator(
        task_id="lambda1",
        python_callable=lambda1,
        provide_context=True,
        dag=dag
)

end = DummyOperator(task_id='stop_execution',  dag=dag)

start >> t1 >> end