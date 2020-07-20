FROM python:3.8.3-slim-buster
LABEL maintainer="Rup Gautam <hello@rupgautam.me>"

WORKDIR /usr/src/app
COPY app app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=run.py

CMD flask run --host=0.0.0.0