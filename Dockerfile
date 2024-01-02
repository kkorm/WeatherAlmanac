FROM python:3-alpine

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install requests_oauthlib
RUN pip install python-dotenv

RUN mkdir -p /home/weatheralmanac
COPY . /home/weatheralmanac

RUN crontab crontab

WORKDIR /home/weatheralmanac