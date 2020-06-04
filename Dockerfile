##################################################
# Section 1: Build the application
FROM ubuntu:18.04 as builder
MAINTAINER Haider Ali ali.haider7111@gmail.com

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y

RUN apt-get install -y --no-install-recommends apt-utils python3 python3-pip && \
	pip3 install --upgrade setuptools && \
	pip3 install requests && \  
	apt-get install cec-utils -y


ADD . /opt/sources
WORKDIR /opt/sources

ENTRYPOINT [ "python3","/opt/sources/Athan.py" ]
