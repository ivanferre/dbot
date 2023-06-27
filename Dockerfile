# syntax=docker/dockerfile:1

#FROM python:3.12-rc-alpine3.18
#FROM python3.11-alpine3.17
FROM python:3

COPY . /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app

CMD python3 firstbot.py
