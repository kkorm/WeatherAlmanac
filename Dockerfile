FROM python:3

ENV TZ="America/Chicago"
RUN date

RUN apt-get update && apt-get install -y cron

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install requests_oauthlib
RUN pip install python-dotenv

RUN mkdir -p /home/weatheralmanac
COPY . /home/weatheralmanac

RUN /usr/bin/crontab /home/weatheralmanac/crontab

WORKDIR /home/weatheralmanac

CMD ["cron", "-f"]