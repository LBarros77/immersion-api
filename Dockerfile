FROM python:3.8

RUN useradd -ms /bin/bash dev

USER dev

ENV PYTHONUNBUFFERED 1

WORKDIR /home/dev/immersion-api

ENV PATH $PATH:/home/dev/.local/bin

COPY requirements.txt /home/dev/immersion-api

RUN pip install -r requirements.txt

COPY . /home/dev/immersion-api
