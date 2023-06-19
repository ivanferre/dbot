FROM python:3.12-rc-alpine3.18
COPY . /app
WORKDIR /app
CMD python3 firstbot.py
