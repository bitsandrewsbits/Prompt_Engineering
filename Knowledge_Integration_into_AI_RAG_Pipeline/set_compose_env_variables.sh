#!/bin/bash
SUBNET="173.18.0.0/24"
GATEWAY="173.18.0.1"

JupyterLab="173.18.0.2"
QdrantDB="173.18.0.3"
LlamaCppServer="173.18.0.4"

# write to .env file
echo "PROJECT_DIR=$(pwd)" > .env
echo "SUBNET=$SUBNET" >> .env
echo "GATEWAY=$GATEWAY" >> .env
echo "JUPYTER_LAB_IP=$JupyterLab" >> .env
echo "QDRANT_DB_IP=$QdrantDB" >> .env
echo "LLAMACPP_Server_IP=$LlamaCppServer" >> .env
