# import json

# min_temp_list = []
# max_temp_list = []
# # declare function for pulling data from json file
# def process_weather(forecast_file):
#     # load JSON file into Python object
#     with open(forecast_file) as json_file:
#         dataSet = json.load(json_file)
    
#     # pulling data from DailyForecasts dictionary
#     for dailyForecasts in dataSet['DailyForecasts']:
        
#         # pulling list of minimum value of Farenheit temperature
#         list_min_temp = dailyForecasts['Temperature']['Minimum']['Value']
#         # append all minimum temps into min_temp_list
#         min_temp_list.append(list_min_temp)

#         # pulling list of maximum value of Farenheit temperature
#         list_max_temp = dailyForecasts['Temperature']['Maximum']['Value']
#         # append all maximum temps into max_temp_list
#         max_temp_list.append(list_max_temp)
   
#     # getting the minimum of the list of minimum value of Farenheit temperature
#     print(min_temp_list)
#     min_temp = min(min_temp_list)
#     print(min_temp)
#     # getting index of minimum temperature in the list
#     idex_min_temp = min_temp_list.index(min_temp)
#     print(idex_min_temp)

#     # getting the maximum of the list of maximum value of Farenheit temperature
#     print(max_temp_list)
#     max_temp = max(max_temp_list)
#     print(max_temp)
#     # getting index of minimum temperature in the list
#     idex_max_temp = max_temp_list.index(max_temp)
#     print(idex_max_temp)

#     # pulling date of lowest temperature
#     date_min_temp = dataSet['DailyForecasts'][idex_min_temp]['Date']
#     print(date_min_temp)

#     # pulling date of highest temperature
#     date_max_temp = dataSet['DailyForecasts'][idex_max_temp]['Date']
#     print(date_max_temp)


# print(process_weather("data/forecast_8days.json"))

        




# # dailyForecasts: dictionary
from datetime import datetime

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")

print(convert_date("2020-06-19T07:00:00+08:00"))