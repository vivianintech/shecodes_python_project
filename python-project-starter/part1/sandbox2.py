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

def convert_date(date):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    farenheit = float(temp_in_farenheit)
    celsius = round((farenheit - 32) * (5/9),1)
    return celsius

def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = (total/num_items)
    return(mean)

def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """

    num_items = 0
    totalMin = 0

    dates = []
    minimum_temps = []
    maximum_temps = []
    summary = ""

    with open(forecast_file) as json_file:
        forecast_5days_a = json.load(json_file)

    for data in forecast_5days_a["DailyForecasts"]:
        date = convert_date(data["Date"])
        dates.append(date)

        minTemp = convert_f_to_c(data["Temperature"]["Minimum"]["Value"])
        minTempFormat = format_temperature(minTemp)
        minimum_temps.append(minTemp)

        maxTemp = convert_f_to_c(data["Temperature"]["Maximum"]["Value"])
        maxTempFormat = format_temperature(maxTemp)
        maximum_temps.append(maxTemp)

        daytime = data["Day"]["LongPhrase"]
        RainProbDay = data["Day"]["RainProbability"]

        nighttime = data["Night"]["LongPhrase"]
        RainProbNight = data["Night"]["RainProbability"]  

        a = ""
        num_items += 1

        summary1 = f"--------{date}--------"
        summary2 = f"Miniumum Temperature: {minTempFormat}"
        summary3 = f"Maximum Temperature: {maxTempFormat}"
        summary4 = f"Daytime: {daytime}"
        summary5 = f"{a:>2}Chance of Rain: {RainProbDay}%"
        summary6 = f"Nighttime: {nighttime}"
        summary7 = f"{a:>2}Chance of Rain: {RainProbNight}%"
        summary8 = "\n"

        summary += summary1 + "\n" + summary2 + "\n" + summary3 + "\n" + summary4 + "\n" + summary5 + "\n" + summary6 + "\n" + summary7 + "\n" + summary8

    lowest_temp = min(minimum_temps)
    lowest_tempFormat = format_temperature(lowest_temp)
    highest_temp = max(maximum_temps)
    highest_tempFormat = format_temperature(highest_temp)
    index_min = minimum_temps.index(lowest_temp)
    index_min_date = dates[index_min]
    index_max = maximum_temps.index(highest_temp)
    index_max_date = dates[index_max]

    totalMin = sum(minimum_temps)
    averageMin = calculate_mean(totalMin, num_items)
    averageMinFormat = format_temperature(averageMin)
    totalMax = sum(maximum_temps)
    averageMax = calculate_mean(totalMax, num_items)
    averageMaxFormat = format_temperature(averageMax)

    a = ""
    overview1 = f"5 Day Overview"
    overview2 = f"{a:>3}The lowest temperature will be {lowest_tempFormat}, and will occur on {index_min_date}."
    overview3 = f"{a:>3}The highest temperature will be {highest_tempFormat}, and will occur on {index_max_date}."
    overview4 = f"{a:>3}The average low this week is {averageMinFormat}."
    overview5 = f"{a:>3}The average high this week is {averageMaxFormat}."
    overview6 = "\n"

    overview = overview1 + "\n" + overview2 + "\n" + overview3 + "\n" + overview4 + "\n" + overview5 + "\n" + overview6
    output = overview + summary
    return output


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))





