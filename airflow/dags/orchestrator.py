import sys 
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta 
from docker.types import Mount

sys.path.append('/opt/airflow/api_requests')

def safe_main_callable():
    from insert_records import main 
    return main()

default_args = {
    'decription': 'Orchestrator for weather data processing',
    'start_date': datetime(2025, 7, 20),
    'catchup': False,
}

dag = DAG(
    dag_id = 'weather_data_orchestrator',
    default_args = default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id= 'ingest_data_task',
        python_callable=safe_main_callable
    )

    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(source='/home/namdoan/repo/weather-data-project/dbt/my_project',
                    target='/usr/app',
                    type='bind'),
            Mount(source='/home/namdoan/repo/weather-data-project/dbt/profiles.yml',
                    target='/root/.dbt/profiles.yml',
                    type='bind')
        ],
        network_mode='weather-data-project_default',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )

    task1 >> task2  