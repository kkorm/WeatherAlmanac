# WeatherAlmanac
Application that pulls weather data from NOAA and posts to a Corteza instance. Note that it is assumed that Corteza is already installed and configured.

## Purpose
This project was initiated largely as a learning exercise to use a combination of Python and Docker.

## To setup:
- Populate the `.env` file with the appropriate values, using `.env.template` as a starting point.
- Run `make docker_startup`
- Add the contents of `crontab` to the host's cron via the command `crontab -e`.

## Find NOAA Weather Station IDs
https://www.ncdc.noaa.gov/cdo-web/datatools/findstation