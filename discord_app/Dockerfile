FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
ENV HOME=/app
WORKDIR $HOME

RUN apt update && apt upgrade -y

ADD requirements.txt $HOME
RUN pip install -r requirements.txt