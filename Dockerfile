FROM PYTHON:3.8-SLIM-BUSTER

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
COPY . .
