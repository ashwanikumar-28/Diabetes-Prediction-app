import streamlit as st
import joblib
import numpy as np

# Load model
model=joblib.load("diabetes1_model.pkl")

st.title("🩺 Diabetes Prediction App")

glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
age = st.number_input("Age", min_value=1, max_value=120, value=33)

if st.button("Predict"):
    input_data = np.array([[bmi, glucose, age]])   # order same as training
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ The model predicts **Diabetic**")
    else:
        st.success("✅ The model predicts **Not Diabetic**")
