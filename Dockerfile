FROM apache/airflow:2.9.3-python3.12

USER root
RUN apt-get update && apt-get install -y git
USER airflow
RUN pip install --no-cache-dir pytest
