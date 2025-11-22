import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Load ML Model
# -----------------------------
MODEL_PATH = "model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


st.set_page_config(page_title="EcoScan - Carbon Emission Predictor")

st.title("🌿 EcoScan")
st.subheader("Carbon Emission Prediction App")

st.write("Enter the vehicle details below to estimate CO₂ emissions.")


fuel_consumption = st.number_input("Fuel Consumption (L/100km)", min_value=0.0, format="%.2f")
distance = st.number_input("Distance Travelled (km)", min_value=0.0, format="%.2f")
engine_size = st.number_input("Engine Size (L)", min_value=0.0, format="%.2f")
cylinders = st.number_input("Number of Cylinders", min_value=1, step=1)


if st.button("Predict Emission"):
    try:
        input_data = np.array([[fuel_consumption, distance, engine_size, cylinders]])
        prediction = model.predict(input_data)[0]

        st.success(f"🌍 Estimated CO₂ Emission: **{round(prediction, 2)} g/km**")

    except Exception as e:
        st.error(f"Error: {e}")

st.caption("Built with ❤️ using Streamlit")
