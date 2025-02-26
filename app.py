import streamlit as st

# Page Config
st.set_page_config(page_title="🔄 Unit Converter", page_icon="🔢", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        .big-font {font-size:30px !important; text-align: center; font-weight: bold;}
        .stTextInput > div > div > input {border-radius: 10px; padding: 10px;}
        .stButton > button {border-radius: 10px; background: linear-gradient(to right, #ff7300, #ff5733); color: white; font-weight: bold;}
        .footer {text-align: center; font-size: 14px; color: grey;}
    </style>
""", unsafe_allow_html=True)

# Heading
st.markdown("<h1 class='big-font'>🔄Unit Converter</h1>", unsafe_allow_html=True)

# Categories of Conversion
categories = {
    "Length": ["Millimeters", "Centimeters", "Meters", "Kilometers", "Inches", "Feet", "Yards", "Miles", "Nautical Miles"],
    "Mass/Weight": ["Kilograms", "Grams", "Pounds", "Ounces", "Tonnes"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Speed": ["km/h", "m/s", "mph", "Knots"],
    "Time": ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Years"],
    "Pressure": ["Pascal", "Bar", "PSI", "Atmosphere", "Torr"],
    "Area": ["Square Meter", "Hectare", "Acre", "Square Foot"],
    "Volume": ["Liter", "Milliliter", "Cubic Meter", "Gallon (US)", "Gallon (UK)", "Pint", "Fluid Ounce"],
    "Energy": ["Joule", "Calorie", "Kilowatt-hour", "Electronvolt", "BTU"],
    "Power": ["Watt", "Kilowatt", "Horsepower", "Megawatt"],
    "Force": ["Newton", "Dyne", "Pound-force", "Kilopond"],
    "Data Storage": ["Byte", "KB", "MB", "GB", "TB", "PB", "Bit"],
    "Fuel Efficiency": ["km/l", "L/100km", "mpg (US)", "mpg (UK)"],
    "Angle": ["Degrees", "Radians", "Gradians"],
    "Frequency": ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"],
    "Luminous Intensity": ["Candela", "Lumen", "Lux"],
    "Radioactivity": ["Becquerel", "Curie", "Sievert"],
    "Torque": ["Newton Meter", "Pound-foot", "Dyne-centimeter"],
    "Electrical Conductance": ["Siemens", "Mho"],
    "Electrical Resistance": ["Ohm", "Milliohm", "Kiloohm", "Megaohm"],
    "Magnetic Flux": ["Weber", "Maxwell", "Tesla", "Gauss"],
}

# User Input
category = st.selectbox("📌 Choose Category:", list(categories.keys()))
from_unit = st.selectbox("🟢 Convert From:", categories[category])
to_unit = st.selectbox("🔵 Convert To:", categories[category])
value = st.number_input("🔢 Enter Value:", min_value=0.0, value=1.0)

# Conversion Logic (Dummy, Real Factors Needed)
def convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value  # No conversion needed
    factor = 1.0  # Placeholder factor, real conversion factors should be added
    return value * factor

# Live Conversion Output
result = convert(value, from_unit, to_unit)
st.success(f"✅ {value} {from_unit} = {result:.5f} {to_unit}")

# Footer
st.markdown("<p class='footer'>Developed by seeratfatima ❤️ | Powered by Streamlit 🚀</p>", unsafe_allow_html=True)
