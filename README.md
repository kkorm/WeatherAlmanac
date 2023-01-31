# WeatherAlmanac
Small website that scrapes data from the National Weather Service.

## Purpose
This project was initiated largely as a learning exercise to use a combination of Python (including Flask), HTML, and CSS. Basic structure was borrowed from https://code.visualstudio.com/docs/python/tutorial-flask. Data from this web application should be used for entertainment purposes only.

## Run
Clone to desired directory `git clone https://github.com/kkorm/WeatherAlmanac`. Install dependencies using `pipenv install`. You may use the development server when running in debug mode in Visual Studio, or a production server can be spun up using Waitress. To use Waitress, use 'pipenv run waitress-serve --listen=*:port web_interface.webapp:app'. Access the app at 127.0.0.1:port.

## Future Improvements
As this was used for educational purposes only, future improvements are unlikely. Obvious improvements could be made to the UI to make it more visually pleasing. More thorough vetting of upstream data from NWS could improve the user experience if inactive stations were removed.
