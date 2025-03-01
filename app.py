import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("crop_recommendation_model.pkl")

# Streamlit UI
st.title("🌱 AI-Powered Crop Recommendation System")
st.write("Enter soil details and get the best crop to grow.")

# User inputs
N = st.number_input("Nitrogen (N)", min_value=0, max_value=100)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=100)
K = st.number_input("Potassium (K)", min_value=0, max_value=100)
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)")

# Predict
if st.button("Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    crop = model.predict(input_data)[0]
    st.success(f"✅ Recommended Crop: **{crop}**")
