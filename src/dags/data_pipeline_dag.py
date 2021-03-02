import importlib
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

dags = importlib.import_module("git-dags")

default_args = {
    'owner': 'agranimo',
    'depends_on_past': False,
    'start_date': datetime(2021, 3, 1, 13, 0, 0),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)}

dag = DAG(
    'data_pipeline_v2',
    default_args=default_args,
    schedule_interval='@hourly',
)

kick_off_dag = DummyOperator(
    task_id='kick_off_dag',
    dag=dag)

data_ingestion = PythonOperator(
    task_id='data_ingestion',
    python_callable=dags.plugins.tasks.fetch_historical_to_s3,
    dag=dag,
)

kick_off_dag >> data_ingestion
