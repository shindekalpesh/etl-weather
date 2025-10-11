## ETL Pipeline for Weather.

Fetch climatic information from a public weather API called Open-Meteo.

Fetching data for location: Switzerland.
api_endpoint = https://api.open-meteo.com/v1/forecast?latitude=46.8182&longitude=8.2275&&current_weather=true


json = {
  "latitude": 46.8,
  "longitude": 8.219999,
  "generationtime_ms": 0.0634193420410156,
  "utc_offset_seconds": 0,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "elevation": 1474,
  "current_weather_units": {
    "time": "iso8601",
    "interval": "seconds",
    "temperature": "°C",
    "windspeed": "km/h",
    "winddirection": "°",
    "is_day": "",
    "weathercode": "wmo code"
  },
  "current_weather": {
    "time": "2025-10-11T03:30",
    "interval": 900,
    "temperature": 4.2,
    "windspeed": 5.9,
    "winddirection": 76,
    "is_day": 0,
    "weathercode": 1
  }
}