FROM python:3-alpine

# RUN pip install pipenv
# RUN pipenv install

RUN pip install --upgrade pip
RUN pip install waitress
RUN pip install flask
RUN pip install requests
RUN pip mysql-connector-python

RUN mkdir -p /home/app/weatheralmanac
COPY . /home/weatheralmanac

EXPOSE 8081

WORKDIR /home/weatheralmanac

CMD ["waitress-serve", "--listen=*:8081", "web_interface.webapp:app"]