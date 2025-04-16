import streamlit as st

# Page config
st.set_page_config(page_title="Unit Converter", layout="centered")

# App title
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🔄 Unit Converter App</h1>",
    unsafe_allow_html=True,
)

# Supported units by category
unit_categories = {
    "Length": {
        "Millimeter (mm)": 0.001,
        "Centimeter (cm)": 0.01,
        "Meter (m)": 1.0,
        "Kilometer (km)": 1000.0,
        "Inch (in)": 0.0254,
        "Foot (ft)": 0.3048,
        "Yard (yd)": 0.9144,
        "Mile (mi)": 1609.34,
    },
    "Mass": {
        "Milligram (mg)": 0.000001,
        "Gram (g)": 0.001,
        "Kilogram (kg)": 1.0,
        "Metric Ton (t)": 1000.0,
        "Ounce (oz)": 0.0283495,
        "Pound (lb)": 0.453592,
    },
    "Time": {
        "Second (s)": 1.0,
        "Minute (min)": 60.0,
        "Hour (hr)": 3600.0,
        "Day (d)": 86400.0,
    },
    "Temperature": {
        "Celsius (°C)": "celsius",
        "Fahrenheit (°F)": "fahrenheit",
        "Kelvin (K)": "kelvin",
    },
}

# Category selection
category = st.selectbox("📂 Select Category", list(unit_categories.keys()))

# Input value
value = st.number_input("🔢 Enter Value to Convert", step=1.0, format="%.4f")

# Unit selection
units = list(unit_categories[category].keys())
from_unit = st.selectbox("🔽 From Unit", units)
to_unit = st.selectbox("🔼 To Unit", units)

def convert_units(category, value, from_unit, to_unit):
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    else:
        base_value = value * unit_categories[category][from_unit]
        converted_value = base_value / unit_categories[category][to_unit]
        return converted_value

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    # Convert from source to Celsius
    if from_unit == "Fahrenheit (°F)":
        value = (value - 32) * 5/9
    elif from_unit == "Kelvin (K)":
        value = value - 273.15
    # Convert from Celsius to target
    if to_unit == "Fahrenheit (°F)":
        return (value * 9/5) + 32
    elif to_unit == "Kelvin (K)":
        return value + 273.15
    else:
        return value

# Convert button
if st.button("Convert"):
    result = convert_units(category, value, from_unit, to_unit)
    st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.8em;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True,
)
