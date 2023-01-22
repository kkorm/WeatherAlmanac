from flask import Flask
from flask import render_template, request
from . import app
from web_interface.almanac_table import almanac_table
from weather_api.offices import offices
from weather_api.stations import stations
import datetime

@app.route("/", methods=['GET'])
def home():
    offices_list = offices().list()
    return render_template("home.html", offices = offices_list)

@app.route("/", methods=['POST'])
def pick_site():
    office = request.form['office']
    stations_list = stations().list(office)

    date = datetime.datetime.now()
    year_cur = date.year
    year_past = year_cur - 3
    years_list = [x for x in range(year_past, year_cur + 1)]

    months_list = [x for x in range(1, 13)]

    return render_template("pick_site.html", stations=stations_list, years=years_list, months=months_list, office=office)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/almanac", methods=['POST'])
def almanac():
    office = request.form['office']
    station = request.form['station']
    year = request.form['year']
    month = request.form['month']

    try:
        table = almanac_table(office, station, year, month)
        date = datetime.date(int(year), int(month), 1)
    except:
        return render_template(
            "almanac_error.html",
        )
    else:
        return render_template(
            "almanac.html",
            station = station,
            year = year,
            month = date.strftime("%B"),
            print_table = table.get_html_string
        )
