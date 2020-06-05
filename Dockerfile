##################################################
# Section 1: Build the application
FROM python:latest as builder
MAINTAINER Haider Ali ali.haider7111@gmail.com

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y

RUN apt-get install -y --no-install-recommends apt-utils python3 python3-pip 
RUN pip3 install --upgrade setuptools
RUN apt-get install -y git python3-dev python3-numpy libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev
RUN apt-get install cec-utils -y
RUN pip3 install requests 
RUN pip3 install pygame

ADD . /opt/sources
WORKDIR /opt/sources

ENTRYPOINT [ "python3","/opt/sources/Athan.py" ]
