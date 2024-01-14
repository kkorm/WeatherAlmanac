# WeatherAlmanac
Application that pulls weather data from NOAA and posts to a Corteza instance. Note that it is assumed that Corteza is already installed and configured.

## Purpose
This project was initiated largely as a learning exercise to use a combination of Python and Docker.

## Run With Docker and Without Datbase
Clone to desired directory `git clone https://github.com/kkorm/WeatherAlmanac`. Build docker image `docker build -t weatheralmanac:local`. Note that the tag is specified as `local` in this case. This can be changed, but the YAML file must match the same tag since a local build is being used. 

## Local Test Runs
For local test builds, install dependencies using `pipenv install`.

Create a `.env` file in the project's root directory with the structure as shown below. Modify variables appropriately.
`corteza_client_id = ''`
`corteza_client_secret = ''`
`corteza_base_url = ''`
`corteza_namespace_id = ''`
`corteza_noaa_module_id = ''`
`corteza_stations_module_id = ''`

Run `docker-compose up -d` to start the container. To teardown, run `docker-compose down`.