# Pull base image
FROM ubuntu:latest

# Labels
LABEL MAINTAINER="Øyvind Nilsen <oyvind.nilsen@gmail.com>"

# Setup external package-sources
RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    python-setuptools \
    python-pip \
    python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* 

# RUN pip install setuptools
RUN pip install pytz influxdb

# Environment vars
ENV PYTHONIOENCODING=utf-8

# Copy files
ADD lnetatmo.py /
ADD netatmo2influxdb.py /
ADD get.sh /

# Run
CMD ["/bin/bash","/get.sh"]
