from python:3.11

RUN useradd -ms /bin/bash dev

USER dev

ENV PYTHONUNBUFFERED 1

WORKDIR /home/immersion/api

ENV PATH $PATH:/home/immersion/.local/bin

COPY requirements.txt /home/immersion/api

RUN pip install -r requirements.txt

COPY . /home/immersion/api