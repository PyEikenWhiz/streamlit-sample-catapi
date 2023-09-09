import streamlit as st
import requests
import pandas as pd
import numpy as np

def get_weather(latitude, longitude):
    # Step 1: Define the API URL for OpenMeteo
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"

    # Step 2: Send a GET request to the OpenMeteo API
    response = requests.get(api_url)

    # Step 3: Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Step 4: Parse the JSON response to get weather data
        weather_data = response.json()

        df = pd.DataFrame(weather_data['hourly']['temperature_2m'],weather_data['hourly']['time'])
        expander = st.expander("Weather Data Expander")
        expander.write("Weather Data")
        expander.write("Sample weather data in a Pandas DataFrame:")
        expander.line_chart(df)

        #st.title("Weather Data")
        #st.write("Sample weather data in a Pandas DataFrame:")
        #st.line_chart(df)

        # Step 5: Display the map
        st.write(f"Weather information for Latidude: {latitude}, Longitude: {longitude}:")
        df = pd.DataFrame(
          np.random.randn(1000, 2) / [50, 50] + [latitude, longitude],
          columns=['lat', 'lon'])
        st.map(df)

    else:
        st.write(f"Failed to fetch weather data for Latidude:{latitude}, Longitude:{longitude}. Please check the city name.")

#get_weather(38.0 ,127.1)

# Streamlit UI elements
st.title("OpenMeteo Weather App")
st.write("Enter the city for weather information:")

latitude = st.number_input("Latitude", value=35.0, step=0.1)
longitude = st.number_input("Longitude", value=135.7, step=0.1)

if st.button("Get Weather"):
    st.write(f"Fetching weather information for Latidude:{latitude}, Longitude:{longitude}...")
    get_weather(latitude, longitude)
