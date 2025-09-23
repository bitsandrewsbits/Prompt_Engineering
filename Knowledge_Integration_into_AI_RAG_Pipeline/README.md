## Instruction for project execution:

# === Build, pull Docker images ===
1) # Build Docker image for Jupyter Notebook container:
sudo docker build -f Jupyter_Notebook.Dockerfile -t jupyter_notebook:latest .

2) # Pull Qdrant image:
sudo docker pull qdrant/qdrant

# === Run Docker containers via Docker Compose ===
