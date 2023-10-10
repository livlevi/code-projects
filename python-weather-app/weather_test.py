#IMPORTING LIBRARY
import requests
import json
import pandas as pd

#GET CURRENT WEATHER DATA
url_data="https://api.open-meteo.com/v1/forecast?latitude=40.7143&longitude=-74.006&hourly=temperature_2m&current_weather=true&timezone=GMT&start_date=2023-08-29&end_date=2023-08-30"
response=requests.get(url_data).json() #get data response in json
weather_df=pd.DataFrame(response)
current_weather=weather_df['current_weather']
print(current_weather)