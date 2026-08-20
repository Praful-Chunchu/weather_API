# Weather Report App

A command-line app that fetches the current weather for a US city using the OpenWeatherMap API.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Get a free API key at [openweathermap.org](https://openweathermap.org/) (API keys section of your account).

3. Create a `.env` file in the project folder with:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Run

```bash
python get_weather.py
```

You'll be prompted to enter a city name, and the app will print the temperature (°C), humidity, and weather description. If the city isn't found, it'll let you know instead of crashing.