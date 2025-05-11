# Weather App using WeatherAPI
# This script fetches the current weather for a given city using the WeatherAPI.
import requests

# Your API key
API_KEY = "Enter_Your_API_Key_Here"
# Base URL for the WeatherAPI
BASE_URL = "Enter _WeatherAPI_URL_Here"
# Example: "http://api.weatherapi.com/v1/current.json"

while True:
    city = input("Enter city name (or type 'exit' to quit): ")

    if city.lower() == 'exit':
        print("Goodbye!")
        break

    # Create full URL
    url = f"{BASE_URL}?key={API_KEY}&q={city}"

    # Make a request
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        country = data['location']['country']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        wind_kph = data['current']['wind_kph']

        print(f"\nWeather Report for {location}, {country}")
        print(f"Temperature: {temp_c}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_kph} km/h\n")

    else:
        print("City not found. Please try again.")
