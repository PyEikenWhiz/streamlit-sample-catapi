import streamlit as st
import requests
import pandas as pd

def get_weather(city):
    # Step 1: Define the API URL for OpenMeteo
    api_url = f"https://api.open-meteo.com/v1/forecast?city={city}&daily=temperature_2m_min,daily_temperature_2m_max,precipitation_sum"
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"

    # Step 2: Send a GET request to the OpenMeteo API
    response = requests.get(api_url)

    # Step 3: Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Step 4: Parse the JSON response to get weather data
        weather_data = response.json()
        print(weather_data.keys())
        print(weather_data['hourly'])

        # Step 5: Display the weather information
        st.write(f"Weather information for {city}:")
        st.write(f"Time: {weather_data['hourly']['time']}")
        st.write(f"Temperature: {weather_data['hourly']['temperature_2m']}°C")
        df = pd.DataFrame(weather_data['hourly']['temperature_2m'],weather_data['hourly']['time'])
        st.title("Weather Data")
        st.write("Sample weather data in a Pandas DataFrame:")
        #print(df)
        st.line_chart(df)
    else:
        st.write(f"Failed to fetch weather data for {city}. Please check the city name.")

#get_weather(city)

# Streamlit UI elements
st.title("OpenMeteo Weather App")
st.write("Enter the city for weather information:")

city = st.text_input("City Name", "Berlin")  # Default city is Berlin

if st.button("Get Weather"):
    st.write(f"Fetching weather information for {city}...")
    get_weather(city)
