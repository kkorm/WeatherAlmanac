from flask import Flask
from flask import render_template
from . import app
from web_interface.almanac_table import almanac_table

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/<office>/<station>/<year>/<month>")
def almanac(office = None, station = None, year = None, month = None):
    table = almanac_table(office, station, year, month)
    return render_template(
        "almanac.html",
        station = station,
        year = year,
        month = month,
        print_table = table.get_html_string
    )
