import json
from datetime import datetime, timedelta

from airflow.models import Variable
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.mongo.hooks.mongo import MongoHook


def fetch_historical_to_s3():
    print("fetch_historical_to_s3")


def process_data():
    print("process_data")


def store_data():
    print("store_data")


def cleanup():
    print("cleanup")
