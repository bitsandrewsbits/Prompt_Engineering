#!/bin/bash
SUBNET="173.18.0.0/24"
GATEWAY="173.18.0.1"

JupyterLab="173.18.0.2"
Qdrant_DB_IP="173.18.0.3"
LlamaCpp_Server_IP="173.18.0.4"
MLFlow_Server_IP="173.18.0.5"
PostgreSQL_DB_IP="173.18.0.6"

PostgreSQL_DB_username=postgres
PostgreSQL_DB_password=postgres_password

# write to .env file
echo "PROJECT_DIR=$(pwd)" > .env
echo "SUBNET=$SUBNET" >> .env
echo "GATEWAY=$GATEWAY" >> .env
echo "JUPYTER_LAB_IP=$JupyterLab" >> .env
echo "QDRANT_DB_IP=$Qdrant_DB_IP" >> .env
echo "LLAMACPP_SERVER_IP=$LlamaCpp_Server_IP" >> .env
echo "MLFLOW_IP=$MLFlow_Server_IP" >> .env
echo "POSTGRESQL_DB_IP=$PostgreSQL_DB_IP" >> .env
echo "POSTGRESQL_DB_USERNAME=$PostgreSQL_DB_username" >> .env
echo "POSTGRESQL_DB_PASSWORD=$PostgreSQL_DB_password" >> .env
echo "MLFLOW_TRACKING_URI=postgresql+psycopg2://$PostgreSQL_DB_username:$PostgreSQL_DB_password@$PostgreSQL_DB_IP:5432/postgres" >> .env
