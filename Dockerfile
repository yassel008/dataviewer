
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ /app/app
WORKDIR /app/app
CMD ["python", "main.py"]
