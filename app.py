import streamlit as st
import requests
import pandas as pd

def get_weather(latitude, longitude):
    # Step 1: Define the API URL for OpenMeteo
    print(latitude, longitude)
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
   
    # Step 2: Send a GET request to the OpenMeteo API
    response = requests.get(api_url)

    # Step 3: Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Step 4: Parse the JSON response to get weather data
        weather_data = response.json()
        print(weather_data.keys())
        print(weather_data['hourly'])

        df = pd.DataFrame(weather_data['hourly']['temperature_2m'],weather_data['hourly']['time'])
        st.title("Weather Data")
        st.write("Sample weather data in a Pandas DataFrame:")
        st.line_chart(df)

        # Step 5: Display the weather information
        st.write(f"Weather information for Latidude:{latitude}, Longitude:{longitude}:")
        st.write(f"Time: {weather_data['hourly']['time']}")
        st.write(f"Temperature: {weather_data['hourly']['temperature_2m']}°C")
    else:
        st.write(f"Failed to fetch weather data for Latidude:{latitude}, Longitude:{longitude}. Please check the city name.")

#get_weather(3,4)

# Streamlit UI elements
st.title("OpenMeteo Weather App")
st.write("Enter the city for weather information:")

latitude = st.number_input("Latitude", value=36)
longitude = st.number_input("Longitude", value=135)

if st.button("Get Weather"):
    st.write(f"Fetching weather information for Latidude:{latitude}, Longitude:{longitude}...")
    get_weather(latitude, longitude)
