from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook                              # Fetch data from API
from airflow.providers.postgres.hooks.postgres import PostgresHook                  # Push data into Postgres
from airflow.sdk import task
from datetime import datetime, timedelta        # airflow.utils.dates.days_ago is deprecated.

# Latitude and Longitude for the desired location. (Using Switzerland in this case.)

LATITUDE = '46.8182'
LONGITUDE = '8.2275'
POSTGRES_CONN_ID = 'postgres_default'
API_CONN_ID = 'open_meteo_api'

default_args = {
    'owner': 'airflow',
    'start_date': datetime.now() - timedelta(days=1),
    
}

print("task", type(task), task)
print("default_args", type(default_args), default_args)
