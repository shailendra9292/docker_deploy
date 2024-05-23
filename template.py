# template.py
import streamlit as st
import pandas as pd
import numpy as np
import requests

def main():
    st.title("Wine Quality Prediction")

    # Input fields for each feature
    fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, step=0.1)
    volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, step=0.01)
    citric_acid = st.number_input("Citric Acid", min_value=0.0, step=0.01)
    residual_sugar = st.number_input("Residual Sugar", min_value=0.0, step=0.1)
    chlorides = st.number_input("Chlorides", min_value=0.0, step=0.001)
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, step=1)
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, step=1)
    density = st.number_input("Density", min_value=0.0, step=0.001)
    pH = st.number_input("pH", min_value=0.0, step=0.01)
    sulphates = st.number_input("Sulphates", min_value=0.0, step=0.01)
    alcohol = st.number_input("Alcohol", min_value=0.0, step=0.1)

    # Submit button to send data for prediction
    if st.button("Predict"):
        # Prepare input data
        input_data = {
            'fixed acidity': fixed_acidity,
            'volatile acidity': volatile_acidity,
            'citric acid': citric_acid,
            'residual sugar': residual_sugar,
            'chlorides': chlorides,
            'free sulfur dioxide': free_sulfur_dioxide,
            'total sulfur dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol
        }

        # Send input data to FastAPI for prediction
        prediction = predict(input_data)

        # Display prediction result
        st.success(f"Predicted Wine Quality: **{prediction}**")

def predict(data):
    # FastAPI endpoint URL
    endpoint = "http://localhost:8000/predict"

    # Send POST request to FastAPI endpoint with input data
    response = requests.post(endpoint, json=data)

    # Parse prediction result from response
    if response.status_code == 200:
        prediction = response.json()['quality']
        return prediction
    else:
        st.error("Error occurred during prediction.")
        return None

if __name__ == "__main__":
    main()
