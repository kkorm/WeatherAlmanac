FROM python:3-alphine

RUN pip install pipenv
RUN pipenv install

RUN mkdir -p /home/app/weatheralmanac

COPY . /home/app

CMD ["waitress-serve", "--call", "web_interface.webapp:app"]