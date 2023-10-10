import schedule
import time


def send_weather_update():
    #Hardcoded latitude and longitude for New York City
    latitude = 40.7128
    longitude = -74.0060

    weather_data = get_weather(latitude, longitude)

def main():
    schedule.every().day.at("08:00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()