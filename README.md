# 🌦️ Weather App using WeatherAPI

This is a simple command-line weather application built with Python. The script fetches and displays real-time weather data for any city using the **[WeatherAPI](https://www.weatherapi.com/)**.

---

## 🧰 Features

- Fetches real-time weather data.
- Displays:
  - City and country name
  - Temperature in °C
  - Weather condition
  - Humidity
  - Wind speed
- Easy input and graceful exit

---

## 📦 Requirements

- Python 3.x
- `requests` library

Install the required package by running:

bash
pip install requests
`

---

## 🔑 Setup Your WeatherAPI Key

1. Visit [WeatherAPI.com](https://www.weatherapi.com/).
2. Sign up and generate your free API key.
3. Replace the placeholders in your script:

python
API_KEY = "write your API key here"
BASE_URL = "write your Base URL here"


Example Base URL:
`http://api.weatherapi.com/v1/current.json`

---

## 🚀 How to Use

1. Save the script as `weather_app.py`.
2. Run the script:

bash
python weather_app.py


3. Enter any city name when prompted.
4. Type `exit` to quit the app.

---

## 💡 Example Output


Enter city name (or type 'exit' to quit): Lahore

Weather Report for Lahore, Pakistan
Temperature: 32°C
Condition: Partly cloudy
Humidity: 47%
Wind Speed: 18 km/h


---

## 🧠 Concepts Practiced

* Working with APIs
* Handling JSON responses
* Using Python’s `requests` module
* Error handling and input validation

---

## 🛠️ Tech Stack

* Python
* WeatherAPI (external service)
* `requests` package for HTTP requests

---

## 👤 Author

**Ahmad**
GitHub: [Ahmad2627](https://github.com/Ahmad2627)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 📝 Notes

Make sure to replace the placeholder strings with your actual API key and the Base URL before running the app.

API_KEY = "write your API key here"
BASE_URL = "write your Base URL here"
