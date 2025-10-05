# syntax=docker/dockerfile:1

FROM ghcr.io/mlflow/mlflow

RUN mkdir /mlflow

CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]