import requests

city: str = input('Название города: ').capitalize()
url: str = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

weather_data = requests.get(url).json()

temperature: int = round(weather_data['main']['temp'])
temperature_feels: int = round(weather_data['main']['feels_like'])

if __name__ == "__main__":
    print(f'Сейчас в городе {city} {temperature}°C')
    print(f'Ощущается как {temperature_feels}°C')
