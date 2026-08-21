import requests
import os
from dotenv import load_dotenv
import streamlit as st

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def get_city_image(city):
    """
    Fetch Image of the City, the user has inputed.
    """
    url = "https://api.unsplash.com/photos/random"

    params = {
        "query": city,
        "client_id": UNSPLASH_ACCESS_KEY,
        "orientation": "landscape"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["urls"]["regular"], data["user"]["name"]
    return None, None




def get_weather(city):
    """
    Fetch weather for the given city and print it nicely.
    """
    # 1. Create the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # 2. Set query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }
    
    # 3. Make the request
    response = requests.get(url, params=params)
    
    # 4. Parse JSON
    data = response.json()

    if response.status_code != 200:
        print(f"Sorry Can't find the weather for {city}, please check the name of the City and try again")
        return 



    city_name = data["name"]
    temp_celsius = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    
    # 6. Print
    st.write(f"In {city_name}, it is {temp_celsius}°C and a humidity of {humidity} with {description}.")

# Try it



# 1. Title and description
st.title("Weather In Any City!")
cityName = st.text_input("Enter any City and We'll fetch you the weather!")

if cityName:
    get_weather(cityName)
    image_url, photographer = get_city_image(cityName)
    if image_url:
        st.image(image_url, caption=f"{cityName} — Photo by {photographer} on Unsplash")


