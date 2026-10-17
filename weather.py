import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_curent_weather(city="Nagpur"):

    request_city_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={os.getenv("API_KEY")}'

    response_city = requests.get(request_city_url).json()

    request_weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={response_city[0]["lat"]}&lon={response_city[0]["lon"]}&appid={os.getenv("API_KEY")}&units=metric'
    
    response_weather = requests.get(request_weather_url).json()

    return response_weather

if __name__ == "__main__":
    print("\n*** Get Current Weather ***\n")

    city = input("\nEnter city name: ")

    weather_data = get_curent_weather(city)

    print("\n")
    print(f"\nCurrent Weather Data for {city}:\n")
    pprint(weather_data)