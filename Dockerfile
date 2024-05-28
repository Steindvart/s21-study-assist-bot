FROM python:3

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src
COPY .env_docker src/.env
COPY content/ content

WORKDIR /app/src
CMD ["python", "main.py"]
