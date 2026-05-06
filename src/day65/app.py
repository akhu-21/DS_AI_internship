import streamlit as st
import joblib
import numpy as np

st.title("Student Performance Predictor")

import os

# Construct absolute path to the model file
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model.pkl")

try:
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"Model file not found! Looked at: {model_path}\nError: {e}")
    st.stop()

input1 = st.number_input("Enter Study Hours")
input2 = st.number_input("Enter Attendance")

if st.button("Predict"):
    prediction = model.predict([[input1, input2]])
    st.success(f"Predicted Score: {prediction[0]}")