FROM ubuntu:18.04

LABEL MAINTANER Your Name "youremail@domain.tld"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app /app
COPY ./run.py .

ENTRYPOINT [ "python" ]

CMD [ "flask", "run" ]