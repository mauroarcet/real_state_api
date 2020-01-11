FROM ubuntu:latest

LABEL maintainer="mauroarcet"

RUN apt-get update
RUN apt-get install -y python3-pip

WORKDIR /true-home

COPY . /true-home

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "/true-home/app.py"]