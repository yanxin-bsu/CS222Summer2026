import requests

url = "https://api.weather.gov/points/40.1934,-85.3864"

response = requests.get(url)
data = response.json()

forecast_url = data["properties"]["forecast"]

forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

periods = forecast_data["properties"]["periods"]

for period in periods:
    print("Name:", period["name"])
    print("Temperature:", period["temperature"])
    print("Detailed Forecast:", period["detailedForecast"])
    print()