import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# List of locations and their coordinates
locations = [
    {"latitude": 52.52, "longitude": 13.41, "name": "Berlin"},
    {"latitude": 52, "longitude": 13.42, "name": "Location2"},
    # Add more locations as needed
]

# List of time periods to query
time_periods = [
    {"start_date": "2020-06-01", "end_date": "2020-08-31"},
    {"start_date": "2010-06-01", "end_date": "2010-08-31"},
    {"start_date": "2020-06-01", "end_date": "2020-08-31"},
    {"start_date": "2010-06-01", "end_date": "2010-08-31"},
    {"start_date": "2020-06-01", "end_date": "2020-08-31"},
    {"start_date": "2010-06-01", "end_date": "2010-08-31"},
    {"start_date": "2020-06-01", "end_date": "2020-08-31"},
    {"start_date": "2010-06-01", "end_date": "2010-08-31"}
    # Add more time periods as needed
]

# Loop over locations and time periods to fetch data
all_hourly_data = []
all_daily_data = []

for location in locations:
    for period in time_periods:
        params = {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "start_date": period["start_date"],
            "end_date": period["end_date"],
            "daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean"],
            "models": "best_match"
        }

        # Fetch data from API
        responses = openmeteo.weather_api(url="https://archive-api.open-meteo.com/v1/archive", params=params)
        response = responses[0]  # Process first response (location and model)

        print(f"Processing data for {location['name']} from {period['start_date']} to {period['end_date']}")
        print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")


        # Process daily data
        daily = response.Daily()
        daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
        daily_temperature_2m_mean = daily.Variables(2).ValuesAsNumpy()

        daily_data = {
            "location": location["name"],
            "date": pd.date_range(
                start=pd.to_datetime(daily.Time(), unit="s", utc=True),
                end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=daily.Interval()),
                inclusive="left"
            ),
            "temperature_2m_max": daily_temperature_2m_max,
            "temperature_2m_min": daily_temperature_2m_min,
            "temperature_2m_mean": daily_temperature_2m_mean
        }

        daily_dataframe = pd.DataFrame(data=daily_data)
        all_daily_data.append(daily_dataframe)

# Concatenate all data into single DataFrames for easier analysis
all_daily_df = pd.concat(all_daily_data, ignore_index=True)


print("Daily data:")
print(all_daily_df.head())

# Save to CSV or other formats
all_daily_df.to_csv('daily_temperature_data.csv', index=False)
