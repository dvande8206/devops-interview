import requests
from datetime import datetime, timezone, timedelta

def fetch_data_from_url(latitude, longitude, time_format=0):
    url = f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted={time_format}'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()

            if 'results' in json_data:
                sunrise_str = json_data['results']['sunrise']
                sunset_str = json_data['results']['sunset']

                # Convert sunrise and sunset strings to datetime objects
                sunrise = datetime.strptime(sunrise_str, "%Y-%m-%dT%H:%M:%S%z")
                sunset = datetime.strptime(sunset_str, "%Y-%m-%dT%H:%M:%S%z")
                
                # Creates cet timezone object representing a time zone offset of 1 hour ahead of Coordinated Universal Time (UTC)
                cet_timezone = timezone(timedelta(hours=1))

                # Convert Sunrise/Sunset UTC times to CET
                sunrise_cet = sunrise.astimezone(cet_timezone)
                sunset_cet = sunset.astimezone(cet_timezone)

                # Used for debugging
                #print(f"Sunrise: {sunrise_cet.strftime('%Y-%m-%d %H:%M:%S %Z')}")
                #print(f"Sunset: {sunset_cet.strftime('%Y-%m-%d %H:%M:%S %Z')}")

                # Get current CET time
                cet_time_now = datetime.now(cet_timezone)
                
                # Used for debugging
                #print(f"Current CET Time: {cet_time_now.strftime('%Y-%m-%d %H:%M:%S %Z')}")

                # Check if current cet time is between sunrise and sunset
                if sunrise_cet <= cet_time_now <= sunset_cet:
                    print("OFF")
                else:
                    print("ON")

            else:
                print("Error: 'results' key not found in the API response.")

        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

fetch_data_from_url(latitude=50.930581, longitude=5.780691)