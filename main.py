import requests
from config import url, city

weather_data = requests.get(url).json()

temperature: int = round(weather_data['main']['temp'])
temperature_feels: int = round(weather_data['main']['feels_like'])

if __name__ == "__main__":
    print(f'Сейчас в городе {city} {temperature}°C')
    print(f'Ощущается как {temperature_feels}°C')