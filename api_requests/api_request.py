import requests

# api_key = "186fab79d6ce9bb555c4c74c15c261b0"
# api_url = "http://api.weatherstack.com/current?access_key={api_key}&query=New York"
api_url= "http://api.weatherstack.com/current?access_key=186fab79d6ce9bb555c4c74c15c261b0&query=New York"


def fetch_data():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        print("Data fetched successfully:")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise
def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-07-17 05:38', 'localtime_epoch': 1752730680, 'utc_offset': '-4.0'}, 'current': {'observation_time': '09:38 AM', 'temperature': 26, 'weather_code': 122, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Overcast '], 'astro': {'sunrise': '05:40 AM', 'sunset': '08:24 PM', 'moonrise': 'No moonrise', 'moonset': '01:04 PM', 'moon_phase': 'Last Quarter', 'moon_illumination': 62}, 'air_quality': {'co': '395.9', 'no2': '35.89', 'o3': '84', 'so2': '11.47', 'pm2_5': '35.15', 'pm10': '35.15', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 13, 'wind_degree': 231, 'wind_dir': 'SW', 'pressure': 1013, 'precip': 0, 'humidity': 69, 'cloudcover': 0, 'feelslike': 29, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}

