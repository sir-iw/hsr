import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from supporting_code import transform


app = Flask(__name__)

# read data
warps = pd.read_csv("Data/warps.csv", delimiter=";")

# transform data
warps = transform.transform(warps)

@app.route("/calendar", methods=["GET", "POST"])
def calendar():

    # read all year-month combinations
    year_month = list(warps['year month'].unique())
    # sort from recent to oldest
    year_month = year_month[::-1]
    # selected year-month
    if request.method == "POST":
        date = request.form['button']
        return redirect(url_for('month', date=date))

    return render_template('calendar.html', year_month=year_month)


@app.route("/calendar-<date>", methods=["GET", "POST"])
def month(date):
    warps_month = warps.loc[warps['year month'] == date]
    warps_month_js = warps_month.to_json()
    return render_template('calendar_month.html', date=date, warps_month=warps_month, warps_month_js=warps_month_js)