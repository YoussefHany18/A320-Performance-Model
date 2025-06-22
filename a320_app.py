import streamlit as st
import pandas as pd
import joblib

# Load trained models
model1 = joblib.load("takeoff_model.joblib")
model2 = joblib.load("fuel_model.joblib")
model3 = joblib.load("climb_model.joblib")

st.title("🛫 A320 Flight Performance Predictor")
st.markdown("Predict Takeoff Distance, Fuel Burn, or Climb Rate based on flight parameters.")

model_choice = st.selectbox("Choose Model:", [
    "Takeoff Distance",
    "Fuel Burn per 100 NM",
    "Climb Rate"
])

# Common input fields used by all models
oat = st.number_input("Outside Air Temperature (°C)", value=23)
slope = st.number_input("Runway Slope (%)", value=1.4)
wind = st.number_input("Headwind/Tailwind (kt)", value=5)
weight = st.number_input("Aircraft Weight (kg)", value=70000)

input_df = pd.DataFrame([[oat, slope, wind, weight]],
    columns=["OAT (C)", "Runway Slope (%)", "Headwind/Tailwind (kt)", "Aircraft Weight (kg)"])

if model_choice == "Takeoff Distance":
    st.subheader("✈️ Predict Takeoff Distance")
    if st.button("Predict"):
        prediction = model1.predict(input_df)
        st.success(f"Predicted Takeoff Distance: {prediction[0]:,.2f} meters")

elif model_choice == "Fuel Burn per 100 NM":
    st.subheader("⛽ Predict Fuel Burn")
    if st.button("Predict"):
        prediction = model2.predict(input_df)
        st.success(f"Predicted Fuel Burn per 100 NM: {prediction[0]:,.2f} kg")

else:
    st.subheader("📈 Predict Climb Rate")
    if st.button("Predict"):
        prediction = model3.predict(input_df)
        st.success(f"Predicted Climb Rate: {prediction[0]:,.2f} ft/min")
