## Instruction for project execution:

#### Build, pull Docker images
1) ##### Build Docker image for Jupyter Notebook container:
sudo docker build -f dockerfiles/Jupyter_Notebook.Dockerfile -t jupyter_notebook:latest .

2) ##### Build Docker image for MLFlow-Server container:
sudo docker build -f dockerfiles/MLFlow_Server.Dockerfile -t mlflow-server:latest .

3) ##### Pull Qdrant image:
sudo docker pull qdrant/qdrant

4) ##### Pull LlamaCpp-Server image:
sudo docker pull ghcr.io/ggml-org/llama.cpp:server

5) ##### Pull PostgreSQL DB image:
sudo docker pull postgres:latest

#### Run Docker containers via Docker Compose
1) ##### Run in terminal, in project dir, in order to write ENV variables in .env file:
	a) chmod u+x set_compose_env_variables.sh
	b) ./set_compose_env_variables.sh

2) ##### Run Docker Compose file:
sudo docker compose up

#### Run Project:
1) During docker compose up, find in terminal a log line from JupyterLab container:
http://localhost:8888/?token=<token>

2) Copy link from 1) and open in brouser.
3) Find on left side file - rag_pipeline.ipynb. Open it.
4) Now, you can start project. Choose Run -> Run all cells to see project demo.
5) After you recieve a LLM answer, you can see experiment results as Runs in MLFlow:
	a) Open link - http://localhost:5000
	b) Open created experiment by name and find Runs tab.
	c) Also you can see in Traces tab, final trace - input(prompt)-output(answer) from LLM server.
5) To see created RAG artifacts files for every Parent Run: Open Run tab -> Artefacts -> open files list.

##### Note: for my laptop, it takes around 10 minutes in order to all containers will have healthy status.
##### Llama Sever downloads model, and starts it. It takes time.
##### So, check periodically containers status - sudo docker ps.
##### Also in terminal, check, if LlamaCpp-Server container sends 200 - you can start project notebook.
