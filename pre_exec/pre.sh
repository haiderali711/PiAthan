#!/usr/bin/env bash

apt-get update -y && \
apt-get upgrade -y && \
apt-get dist-upgrade -y

apt-get install -y --no-install-recommends apt-utils python3 python3-pip 
pip3 install --upgrade setuptools
#apt-get install -y git python3-dev python3-numpy libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev
apt-get install cec-utils -y
pip3 install requests 
pip3 install pygame