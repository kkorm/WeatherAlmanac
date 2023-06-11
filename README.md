# WeatherAlmanac
Small website that scrapes data from the National Weather Service.

## Purpose
This project was initiated largely as a learning exercise to use a combination of Python (including Flask), HTML, CSS, and Docker. Basic structure was borrowed from https://code.visualstudio.com/docs/python/tutorial-flask. Data from this web application should be used for entertainment purposes only.

## Run Standalone and Without Database
Clone to desired directory `git clone https://github.com/kkorm/WeatherAlmanac`. Install dependencies using `pipenv install`. You may use the development server when running in debug mode in Visual Studio, or a production server can be spun up using Waitress. To use Waitress, use `pipenv run waitress-serve --listen=*:port web_interface.webapp:app`. Access the app at 127.0.0.1:port.

## Run With Docker and Without Datbase
Clone to desired directory `git clone https://github.com/kkorm/WeatherAlmanac`. Build docker image `docker build -t weatheralmanac:tag .`, replacing `tag` with desired qualifier. Create the container using `docker run -p 127.0.0.1:hostport:8081/tcp weatheralmanac:tag`, replacing `hostport` and `tag` as appropriate.

## Run With Docker and With Datbase
Clone to desired directory `git clone https://github.com/kkorm/WeatherAlmanac`. Build docker image `docker build -t weatheralmanac:local .`. Note that the tag is specified as `local` in this case. This can be changed, but the YAML file must match the same tag since a local build is being used. Copy the YAML file to a different directory and edit variables as required. Run `docker-compose -f Stack_SQL.yml up` to start the container. To teardown, run `docker-compose -f Stack_SQL.yml down`.

## Future Improvements
As this was used for educational purposes only, future improvements are unlikely. Obvious improvements could be made to the UI to make it more visually pleasing. More thorough vetting of upstream data from NWS could improve the user experience if inactive stations were removed.

## To DO
- Update documentation and code to use .env for db credentials
- Update code to write/read to/from database
