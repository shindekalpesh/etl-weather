from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook                         # Fetch data from API

from airflow.providers.postgres.hooks.postgres import PostgresHook              # Push data into Postgres
from airflow.decorators import task
from airflow.utils.dates import days_ago


# Latitude and Longitude for the desired location. (Using Switzerland in this case.)

LATITUDE = '46.8182'
LONGITUDE = '8.2275'
POSTGRES_CONN_ID = 'postgres_default'
API_CONN_ID = 'open_meteo_api'

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    
}

print("default_args", type(default_args), default_args)
