import json
from datetime import datetime
import plotly.express as px
import pandas as pd

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def convert_f_to_c(temp_in_farenheit):
    temp_in_celsius = (temp_in_farenheit-32) * 5/9
    multiply_part = (temp_in_farenheit-32) * 5
    if multiply_part % 9 == 0:
        return temp_in_celsius
    else:
        return round(temp_in_celsius,1)

def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")

filePaths = ["data/forecast_5days_a.json", "data/forecast_5days_b.json", "data/forecast_8days.json"]

for filePath in filePaths:
    with open(filePath) as jsonFile:
        dataSet = json.load(jsonFile)

    dateList = []
    minTempList = []
    maxTempList = []
    numDays = 0
    minRealFeels = []
    minRealShades = []

    for dailyForecasts in dataSet["DailyForecasts"]:
        date = convert_date(dailyForecasts["Date"])
        minTemp = convert_f_to_c(dailyForecasts["Temperature"]["Minimum"]["Value"])
        maxTemp = convert_f_to_c(dailyForecasts["Temperature"]["Maximum"]["Value"])
        dateList.append(date)
        minTempList.append(minTemp)
        maxTempList.append(maxTemp)
        numDays += 1
        minRealFeel = convert_f_to_c(dailyForecasts["RealFeelTemperature"]["Minimum"]["Value"])
        minRealFeels.append(minRealFeel)
        minRealShade = convert_f_to_c(dailyForecasts["RealFeelTemperatureShade"]["Minimum"]["Value"])
        minRealShades.append(minRealShade)

    print(minRealFeels)
    print(minRealShades)

    df = {
        "Minimum Temperature": minTempList,
        "Maximum Temperature": maxTempList,
        "Date": dateList
    }

    fig = px.line(
        df,
        x = "Date",
        y = ["Minimum Temperature", "Maximum Temperature"],
        title= f"Daily Forecast for {numDays} days from {dateList[0]} to {dateList[-1]}"
    )

    fig.update_layout(
        yaxis_title="Temperature (°C)"
    )
    fig.show()

    df1 = {
        "Minimum Temperature": minTempList,
        "Minimum Real Feel Temperature": minRealFeels,
        "Minimum Real Feel Temperature Shade": minRealShades,
        "Date": dateList
    }
    fig1 = px.line(
        df1,
        x = "Date",
        y = ["Minimum Temperature", "Minimum Real Feel Temperature", "Minimum Real Feel Temperature Shade"],
        title=f"Daily Forecast for {numDays} days from {dateList[0]} to {dateList[-1]}"
    )

    fig1.update_layout(
        yaxis_title="Temperature (°C)"
    )
    fig1.show()
    