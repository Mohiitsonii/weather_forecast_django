import requests
from django.conf import settings


def get_weather_forecast(lat, lon, detailing_type):
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = "https://api.openweathermap.org/data/2.5/onecall"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "exclude": "minutely,alerts",
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    data = response.json()

    # Check if the response contains the 'hourly' key
    if 'hourly' not in data:
        raise ValueError(
            "Invalid weather data format. Hourly forecast data not found.")

    # Get the forecast data based on the detailing type
    if detailing_type == 'minute':
        forecast_data = data['minutely']
    elif detailing_type == 'hourly':
        forecast_data = data['hourly']
    elif detailing_type == 'daily':
        forecast_data = data['daily']
    else:
        raise ValueError(
            "Invalid detailing type. Allowed values are 'minute', 'hourly', and 'daily'.")

    return forecast_data
