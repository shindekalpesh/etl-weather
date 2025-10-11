from airflow import DAG
from airflow.providers.https.hooks.http import HttpHook                         # Fetch data from API
from airflow.providers.postgres.hooks.postgres import PostgresHook              # Push data into Postgres
from airflow.decorators import task
from airflow.utils.dates import days_ago

