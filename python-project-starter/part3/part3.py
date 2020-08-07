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

def convert_hour(iso_string):
    h = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return h.strftime("%H:%M")

# START RETRIEVING DATA AND MAKE GRAPHS
filePaths = ["data/historical_6hours.json", "data/historical_24hours_a.json", "data/historical_24hours_b.json"]



for filePath in filePaths:
    tempList = []
    realTempList = []
    hourList = []
    weatherText = []
    weatherCounting = []

    with open(filePath) as jsonFile:
        dataSet = json.load(jsonFile)
    
    # setup initial vars 
    minTemp = dataSet[0]["Temperature"]["Metric"]["Value"]
    maxTemp = dataSet[0]["Temperature"]["Metric"]["Value"]
    minDateTemp = dataSet[0]["LocalObservationDateTime"]
    minDateTemp = dataSet[0]["LocalObservationDateTime"]
    sumPrecip = 0
    dayTimeCount = 0
    maxUV = dataSet[0]["UVIndex"]
    hourMaxUV = dataSet[0]["LocalObservationDateTime"]
    outcomes = ""
    
    for data in dataSet:

        temps = data["Temperature"]["Metric"]["Value"]
        tempList.append(temps)
        realTemp = data["RealFeelTemperature"]["Metric"]["Value"]
        realTempList.append(realTemp)
        dateHour = convert_hour(data["LocalObservationDateTime"])
        hourList.append(dateHour)


        # getting min temp, min temp date
        if temps < minTemp:
            minTemp = temps
            minDateTemp = data["LocalObservationDateTime"]

        # getting max temp, max temp date
        if temps > maxTemp:
            maxTemp = temps
            maxDateTemp = data["LocalObservationDateTime"]
        
        # getting precipitation
        precips = data["PrecipitationSummary"]["Precipitation"]["Metric"]["Value"]
        sumPrecip += precips

        # day time count
        dayTime = data["IsDayTime"]
        if dayTime == True:
            dayTimeCount += 1

        # UV index
        uvIdx = data["UVIndex"]
        if uvIdx > maxUV:
            maxUV = uvIdx
            hourMaxUV = data["LocalObservationDateTime"]
        
        #weatherText
        weatherTxt = data["WeatherText"]
        weatherText.append(weatherTxt)
    
    # formatting outputs
    fmMinTemp = format_temperature(minTemp)
    fmMaxTemp = format_temperature(maxTemp)
    fmMinHourTemp = convert_hour(minDateTemp)
    fmMaxHourTemp = convert_hour(maxDateTemp)
    fmMinDateTemp = convert_date(minDateTemp)
    fmMaxDateTemp = convert_date(maxDateTemp)
    fmHourMaxUV = convert_hour(hourMaxUV)

    # printing outputs
    outcomes += f"-------- Data from {filePath} --------\n"
    outcomes += f"Minimum temperature occurred is {fmMinTemp} at {fmMinHourTemp}\n"
    outcomes += f"Minimum temperature occurred is {fmMaxTemp} at {fmMaxHourTemp}\n"
    outcomes += f"Amount of precipitation that fell is {sumPrecip}mm\n"
    outcomes += f"The number of daylight hours in the past 24 hours is {dayTimeCount} hours\n"
    outcomes += f"The maximum UV index is {maxUV}, and was occurred at {fmHourMaxUV}\n\n"

    print(outcomes)

    #Graphs 
    df = {
        "Temperature": tempList, 
        "Real Temperature": realTempList
    }

    fig = px.box(
        df,
        y = ["Temperature", "Real Temperature"],
        points = "all"
    )
    fig.update_layout(
        yaxis_title="Temperature (°C)",
        xaxis_title="Different temperatures"
    )

    fig.show()
        

    df1 = {
        "Weather Text": weatherText
    }

    fig1 = px.bar(
        df1,
        x="Weather Text"
    )
    fig1.show()