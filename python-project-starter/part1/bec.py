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
​
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

    minimum_temps = []
    dates = []
    maximum_temps = []

    with open(forecast_file) as json_file:
        forecast_5days_a = json.load(json_file)

    for data in forecast_5days_a["DailyForecasts"]:
        # appending dates into date list 
        date = data["Date"]
        dateFormat = convert_date(date)
        dates.append(date)
       
        minTemp = convert_f_to_c(data["Temperature"]["Minimum"]["Value"]) 
        minimum_temps.append(minTemp)
        
        maxTemp = convert_f_to_c(data["Temperature"]["Maximum"]["Value"])
        maximum_temps.append(maxTemp)
        
        daytime = data["Day"]["LongPhrase"]
        RainProbDay = data["Day"]["RainProbability"]
        
        nighttime = data["Night"]["LongPhrase"]
        RainProbNight = data["Night"]["RainProbability"]  
        
        a = ""
        num_items += 1
    
    # moved lowest temp from inside the loop to outside the loop
    lowest_temp = min(minimum_temps)
    highest_temp = max(maximum_temps)

    index_min = minimum_temps.index(lowest_temp)
    index_max = maximum_temps.index(highest_temp)

    totalMin = sum(minimum_temps)
    totalMax = sum(maximum_temps)
    
    averageMin = calculate_mean(totalMin, num_items)
    averageMax = calculate_mean(totalMax, num_items)
    
    

    # totalMax = sum(maximum_temps)

    # averageMin = calculate_mean(totalMin, num_items)
    # averageMax = calculate_mean(totalMax, num_items)

        # print(f"--------{dateFormat}--------")
        # print(f"Miniumum Temperature: {minTemp}")
        # print(f"Miniumum Temperature: {minTempFormat}")
        # print(f"Maximum Temperature: {maxTemp}")
        # print(f"Daytime: {daytime}")
        # print(f"{a:>2}Chance of Rain: {RainProbDay}%")
        # print(f"Nighttime: {nighttime}")
        # print(f"{a:>2}Chance of Rain: {RainProbNight}%")
        # print()
        # print(min(minimum_temps))
        # print(lowest_temp)
        # print(index_min)
        # # print(dates)
        # print(dates[index_min])
        # print(num_items)
        # print(minimum_temps)
        # print(totalMin)
        # print(averageMin)
        # print(max(maximum_temps))
        # print(highest_temp)
        # print(index_max)
        # print(dates[index_max])
        # print(maximum_temps)
        # print(averageMax)

# a = ""
# print(f"5 Day Overview")
# print(f"{a:>3}The lowest temperature will be lowest_temp, and will occur on index_min.")
# print(f"{a:>3}The highest temperature will be highest_temp, and will occur on index_date.")
# print(f"{a:>3}The average low this week is averageMin.")
# print(f"{a:>3}The average high this week is averageMax.")
# print()

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))