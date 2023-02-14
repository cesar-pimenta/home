FROM ubuntu:22.04

EXPOSE 8000

RUN apt-get -qq -y update && \
    apt-get -qq -y install \
    wget \
    curl \
    git \
    make \
    python3 \ 
    python3-pip \
    python3-venv
