import requests

city = input("Enter a city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=Bd5e378503939ddaee76f12ad7a97608&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"The temperature in {city} is {temp:.1f}°C with {desc}.")
else:
    print(f"Error fetching weather data for {city}.")
