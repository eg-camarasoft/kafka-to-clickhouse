FROM python:3.7.12-slim-bullseye
RUN apt-get update && apt-get install -y python3-pip build-essential librdkafka-dev

RUN mkdir -p /app
COPY app/requirements.txt /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#CMD ["python", "producer.py"]
CMD ["tail", "-f", "/dev/null"]