FROM python:3

ENV TZ="America/Chicago"
RUN date

# RUN python -m ensurepip --upgrade
# RUN pip install requests
# RUN pip install requests_oauthlib
# RUN pip install python-dotenv

# RUN mkdir -p /home/weatheralmanac
# COPY . /home/weatheralmanac

# WORKDIR /home/weatheralmanac

# CMD ["cron", "-f"]


RUN mkdir -p /var/lib/source
WORKDIR /var/lib/source
COPY ./source ./

RUN python -m ensurepip --upgrade
RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]