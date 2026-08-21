# Weather Report App

A Streamlit app that fetches the current weather and a photo for any city, using the OpenWeatherMap and Unsplash APIs.

## Setup

1. Install dependencies:
```bash
   pip install -r requirements.txt
```

2. Get a free API key at [openweathermap.org](https://openweathermap.org/) (API keys section of your account).

3. Get a free API key at [unsplash.com/oauth/applications](https://unsplash.com/oauth/applications) (create a new application, then copy the Access Key).

4. Create a `.env` file in the project folder with:
```
   OPENWEATHER_API_KEY=your_openweather_key_here
   UNSPLASH_ACCESS_KEY=your_unsplash_key_here
```

## Run

```bash
streamlit run get_weather.py
```

This opens the app in your browser. Enter a city name, and it'll display the temperature (°C), humidity, weather description, and a photo of the city. If the city isn't found, it'll let you know instead of crashing.