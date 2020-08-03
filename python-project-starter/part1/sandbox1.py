import json
from datetime import datetime
DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    temp_in_celsius = (temp_in_farenheit-32) * 5/9
    multiply_part = (temp_in_farenheit-32) * 5
    if multiply_part % 9 == 0:
        return temp_in_celsius
    else:
        return round(temp_in_celsius,1)


def calculate_mean(total, num_items):
    mean_number = total/num_items
    if total % num_items == 0:
        return mean_number
    else:
        return round(mean_number,1)


def process_weather(forecast_file):
    # load JSON file into Python object
    with open(forecast_file) as json_file:
        dataSet = json.load(json_file)
    
    minTemp = dataSet["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]
    minDate = dataSet["DailyForecasts"][0]["Date"]
    maxTemp = dataSet["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
    maxDate = dataSet["DailyForecasts"][0]["Date"]
    totalMinTemp = 0
    totalMaxTemp = 0

    # retrieve data for the first paragraph
    for dataSubSet in dataSet["DailyForecasts"]:
        # retrieve lowest temperature and date throughout 8 days forecast
        minTempValues = dataSubSet["Temperature"]["Minimum"]["Value"]
        minDateValues = dataSubSet["Date"]
        totalMinTemp += minTempValues
        if minTempValues < minTemp:
            minTemp = minTempValues
            minDate = minDateValues
        else:
            None
        # retrieve highest temperature and date through out 8 days forecast
        maxTempValues = dataSubSet["Temperature"]["Maximum"]["Value"]
        maxDateValues = dataSubSet["Date"]
        totalMaxTemp += maxTempValues
        if maxTempValues > maxTemp:
            maxTemp = maxTempValues
            maxDate = maxDateValues
    
    minTempCelsius = format_temperature(convert_f_to_c(minTemp))
    maxTempCelsius = format_temperature(convert_f_to_c(maxTemp))
    dateTimeMinFormat = convert_date(minDate)
    dateTimeMaxFormat = convert_date(maxDate)
    lenDataSet = len(dataSet["DailyForecasts"])
    meanMinTemp = format_temperature(convert_f_to_c(calculate_mean(totalMinTemp, lenDataSet)))
    meanMaxTemp = format_temperature(convert_f_to_c(calculate_mean(totalMaxTemp, lenDataSet)))
    print(f"{lenDataSet} Day Overview")
    print(f"    The lowest temperature will be {minTempCelsius}, and will occur on {dateTimeMinFormat}.")
    print(f"    The highest temperature will be {maxTempCelsius}, and will occur on {dateTimeMaxFormat}.")
    print(f"    The average low this week is {meanMinTemp}.")
    print(f"    The average high this week is {meanMaxTemp}.")

    # retrieve data for the remaining paragraphs
    for dataSubSet in dataSet["DailyForecasts"]:
        
        # Day
        dateData = convert_date(dataSubSet["Date"])
        print(f"\n--------{dateData}--------")

        # Temperature
        minTempValues = format_temperature(convert_f_to_c(dataSubSet["Temperature"]["Minimum"]["Value"]))
        maxTempValues = format_temperature(convert_f_to_c(dataSubSet["Temperature"]["Maximum"]["Value"]))
        print(f"Minimum Temperature: {minTempValues}")
        print(f"Maximum Temperature: {maxTempValues}")
        
        # Daytime
        dayTimeData = dataSubSet["Day"]["LongPhrase"]
        print(f"Daytime: {dayTimeData}")

        # Chance of rain
        rainDayProbability = dataSubSet["Day"]["RainProbability"]
        print(f"    Chance of rain:  {rainDayProbability}%")

        # Night time
        nightTimeData = dataSubSet["Night"]["LongPhrase"]
        print(f"Nighttime: {nightTimeData}")

        # Chance of rain
        rainNightProbability = dataSubSet["Night"]["RainProbability"]
        print(f"    Chance of rain:  {rainNightProbability}%")

# if __name__ == "__main__":
#     print(process_weather("data/forecast_5days_a.json"))
process_weather("data/forecast_5days_a.json")