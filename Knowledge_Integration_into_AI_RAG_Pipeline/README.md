## Instruction for project execution:

#### Build, pull Docker images
1) ##### Build Docker image for Jupyter Notebook container:
sudo docker build -f Jupyter_Notebook.Dockerfile -t jupyter_notebook:latest .

2) ##### Pull Qdrant image:
sudo docker pull qdrant/qdrant

3) ##### Pull LlamaCpp-Server image:
sudo docker pull ghcr.io/ggml-org/llama.cpp:server

#### Run Docker containers via Docker Compose
1) ##### Run in terminal, in project dir, in order to write ENV variables in .env file:
chmod u+x set_compose_env_variables.sh
./set_compose_env_variables.sh

2) ##### Run Docker Compose file:
sudo docker compose up
