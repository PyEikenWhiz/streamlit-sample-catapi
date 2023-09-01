import streamlit as st

# Step 1: Import necessary libraries
import requests  # Library for making HTTP requests
#from IPython.display import Image, display  # Library for displaying images

# Step 2: Define the API URL for a random cat image
api_url = "https://api.thecatapi.com/v1/images/search"

# Step 3: Send a GET request to the API and get the response
response = requests.get(api_url)

# Step 4: Check if the request was successful (status code 200)
if response.status_code == 200:
    # Step 5: Parse the JSON response to get the image URL
    cat_data = response.json()
    cat_image_url = cat_data[0]["url"]

    # Step 6: Display the cat image inline in Colab
    st.image(cat_image_url)
#    display(Image(url=cat_image_url))
else:
    print("Failed to fetch cat data from the API.")