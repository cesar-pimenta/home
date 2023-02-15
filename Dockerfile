FROM ubuntu:22.04

EXPOSE 8000
WORKDIR /home

RUN apt-get -qq -y update && \
    apt-get -qq -y install \
    wget \
    curl \
    git \
    make \
    python3 \ 
    python3-pip \
    python3-venv

COPY . /home

RUN pip install -r requirements/base.txt

RUN python3 manage.py migrate

 CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]