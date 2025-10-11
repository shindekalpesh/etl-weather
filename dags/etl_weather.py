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

# DAG (Directed Acyclic Graph)
with DAG(
    dag_id='weather_etl_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dags:
    
    @task()
    def extract_weather_data():
        """Extraction of data from the Open-Meteo API using Airflow Connection"""

        # Use HttpHook to connection details from Airflow Connection
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method='GET')
        print("http_hook", type(http_hook), http_hook)
        
        # Build the API Endpoint
        api_endpoint = f"/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&&current_weather=true"
        #"https://api.open-meteo.com/v1/forecast?latitude=46.8182&longitude=8.2275&&current_weather=true"
        print("api_endpoint", type(api_endpoint), api_endpoint)
        
        # Make Response Request from via http_hook
        response = http_hook.run(api_endpoint)
        print("response", type(response), response)
        
        print("response.status_code", type(response.status_code), response.status_code)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch the weather data: {response.status_code}. ")
        