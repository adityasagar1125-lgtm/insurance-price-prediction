import streamlit as st
import joblib
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Insurance Price Prediction",
    page_icon="💰",
    layout="centered"
)

# Title
st.title("💰 Insurance Price Prediction")
st.write("Enter your details below to estimate your insurance charges.")

# Load model and scaler
model = joblib.load("models/linear_regression_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Input section
col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=25
    )

    sex = st.selectbox(
        "Sex",
        ["female", "male"]
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=100.0,
        value=25.0
    )

with col2:
    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=10,
        value=0
    )

    smoker = st.selectbox(
        "Smoker",
        ["no", "yes"]
    )

    region = st.selectbox(
        "Region",
        ["northeast", "northwest", "southeast", "southwest"]
    )

# Encode categorical variables
sex_encoded = 1 if sex == "female" else 0
smoker_encoded = 1 if smoker == "yes" else 0

# Encode region
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# Create input DataFrame
input_data = pd.DataFrame({
    "age": [age],
    "sex": [sex_encoded],
    "bmi": [bmi],
    "children": [children],
    "smoker": [smoker_encoded],
    "region_northwest": [region_northwest],
    "region_southeast": [region_southeast],
    "region_southwest": [region_southwest]
})

# Scale numerical features
input_data[["age", "bmi", "children"]] = scaler.transform(
    input_data[["age", "bmi", "children"]]
)

# Prediction
if st.button("Predict Insurance Price"):
    prediction = model.predict(input_data)

    st.success(
        f"💰 Estimated Insurance Price: ₹{prediction[0]:,.2f}"
    )