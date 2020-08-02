# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
# Datetime and other 
from datetime import datetime
import boto3, json
# Importing airflow hook
from airflow.contrib.hooks.aws_lambda_hook import AwsLambdaHook

# Default arguments and can be overwritten at operator initialization
default_args = {
        'owner': 'Vijay',
        'depends_on_past': False,
        'start_date': datetime(2020,5,1),
        'email': ['@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
}



# Function

def lambda1(ds,**kwargs):
        
        hook = AwsLambdaHook('myAirflowTest', region_name='', log_type='None',qualifier='$LATEST',invocation_type='RequestResponse',config=None,aws_conn_id='my_lambda')
        response_1 = hook.invoke_lambda(payload='null')
        print ('Response--->' , response_1)

# Task

# Using the context manager alllows you not to duplicate the dag parameter in each operator
with DAG('invocation_hook_lambda', default_args=default_args, description='invoke a lambda in dev aws instance') as dag:

    start = DummyOperator(task_id='Begin_execution')

    t1 = PythonOperator(
        task_id="lambda1",
        python_callable=lambda1,
        provide_context=True
)

    t2 = BashOperator(
        task_id="run_with_lambda",
        bash_command="echo 1"
)

    t3 = BashOperator(
        task_id="run_with_lambda2",
        bash_command="echo 1"
)
    end = DummyOperator(task_id='stop_execution')



start >>  [t1, t2] >>  t3 >>end
