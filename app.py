import streamlit as st

st.set_page_config(page_title="🔄 Unit Converter", page_icon="🔢", layout="centered")

st.markdown("""
    <style>
        .big-font {font-size:30px !important; text-align: center; font-weight: bold;}
        .stTextInput > div > div > input {border-radius: 10px; padding: 10px;}
        .stButton > button {border-radius: 10px; background: linear-gradient(90deg, #ff7300, #ff5733); color: white; font-weight: bold; border: none; padding: 10px 20px;}
        .footer {text-align: center; font-size: 14px; color: grey;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='big-font'>🔄 Unit Converter</h1>", unsafe_allow_html=True)

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

category = st.selectbox("📌 Choose Category:", list(categories.keys()), index=0)
from_unit = st.selectbox("🟢 Convert From:", categories[category])
to_unit = st.selectbox("🔵 Convert To:", categories[category])
value = st.number_input("🔢 Enter Value:", min_value=0.0, value=1.0)

def convert(value, from_unit, to_unit):
    conversion_factors = {
    # Length
    "Millimeters": {"Centimeters": 0.1, "Meters": 0.001, "Kilometers": 1e-6, "Inches": 0.0393701, "Feet": 0.00328084, "Yards": 0.00109361, "Miles": 6.2137e-7},
    "Centimeters": {"Millimeters": 10, "Meters": 0.01, "Kilometers": 1e-5, "Inches": 0.393701, "Feet": 0.0328084, "Yards": 0.0109361, "Miles": 6.2137e-6},
    "Meters": {"Millimeters": 1000, "Centimeters": 100, "Kilometers": 0.001, "Inches": 39.3701, "Feet": 3.28084, "Yards": 1.09361, "Miles": 0.000621371},
    "Kilometers": {"Millimeters": 1e6, "Centimeters": 100000, "Meters": 1000, "Inches": 39370.1, "Feet": 3280.84, "Yards": 1093.61, "Miles": 0.621371},
    "Inches": {"Millimeters": 25.4, "Centimeters": 2.54, "Meters": 0.0254, "Kilometers": 2.54e-5, "Feet": 0.0833333, "Yards": 0.0277778, "Miles": 1.5783e-5},
    "Feet": {"Millimeters": 304.8, "Centimeters": 30.48, "Meters": 0.3048, "Kilometers": 0.0003048, "Inches": 12, "Yards": 0.333333, "Miles": 0.000189394},
    "Yards": {"Millimeters": 914.4, "Centimeters": 91.44, "Meters": 0.9144, "Kilometers": 0.0009144, "Inches": 36, "Feet": 3, "Miles": 0.000568182},
    "Miles": {"Millimeters": 1.609e6, "Centimeters": 160900, "Meters": 1609.34, "Kilometers": 1.60934, "Inches": 63360, "Feet": 5280, "Yards": 1760},
    
    # Mass/Weight
    "Kilograms": {"Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274, "Tonnes": 0.001},
    "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
    "Pounds": {"Kilograms": 0.453592, "Grams": 453.592, "Ounces": 16},
    "Ounces": {"Kilograms": 0.0283495, "Grams": 28.3495, "Pounds": 0.0625},
    "Tonnes": {"Kilograms": 1000, "Grams": 1e6, "Pounds": 2204.62},

    # Temperature
    "Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
    "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9, "Kelvin": lambda f: (f - 32) * 5/9 + 273.15},
    "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32},

    # Speed
    "km/h": {"m/s": 0.277778, "mph": 0.621371, "Knots": 0.539957},
    "m/s": {"km/h": 3.6, "mph": 2.23694, "Knots": 1.94384},
    "mph": {"km/h": 1.60934, "m/s": 0.44704, "Knots": 0.868976},
    "Knots": {"km/h": 1.852, "m/s": 0.514444, "mph": 1.15078},

    # Time
    "Seconds": {"Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400, "Weeks": 1/604800, "Years": 1/31536000},
    "Minutes": {"Seconds": 60, "Hours": 1/60, "Days": 1/1440, "Weeks": 1/10080, "Years": 1/525600},
    "Hours": {"Seconds": 3600, "Minutes": 60, "Days": 1/24, "Weeks": 1/168, "Years": 1/8760},
    "Days": {"Seconds": 86400, "Minutes": 1440, "Hours": 24, "Weeks": 1/7, "Years": 1/365},
    "Weeks": {"Seconds": 604800, "Minutes": 10080, "Hours": 168, "Days": 7, "Years": 1/52.1429},
    "Years": {"Seconds": 31536000, "Minutes": 525600, "Hours": 8760, "Days": 365, "Weeks": 52.1429},

    # Area
    "Square Meter": {"Hectare": 0.0001, "Acre": 0.000247105, "Square Foot": 10.7639},
    "Hectare": {"Square Meter": 10000, "Acre": 2.47105, "Square Foot": 107639},
    "Acre": {"Square Meter": 4046.86, "Hectare": 0.404686, "Square Foot": 43560},
    "Square Foot": {"Square Meter": 0.092903, "Hectare": 9.2903e-6, "Acre": 2.2957e-5},

    # Volume
    "Liter": {"Milliliter": 1000, "Cubic Meter": 0.001, "Gallon (US)": 0.264172, "Gallon (UK)": 0.219969, "Pint": 2.11338, "Fluid Ounce": 33.814},
    "Milliliter": {"Liter": 0.001, "Cubic Meter": 1e-6},
    "Cubic Meter": {"Liter": 1000, "Milliliter": 1e6},
    "Gallon (US)": {"Liter": 3.78541, "Milliliter": 3785.41},
    "Gallon (UK)": {"Liter": 4.54609, "Milliliter": 4546.09},

    # Power
    "Watt": {"Kilowatt": 0.001, "Horsepower": 0.00134102, "Megawatt": 1e-6},
    "Kilowatt": {"Watt": 1000, "Horsepower": 1.34102, "Megawatt": 0.001},
    "Horsepower": {"Watt": 745.7, "Kilowatt": 0.7457, "Megawatt": 0.0007457},
    "Megawatt": {"Watt": 1e6, "Kilowatt": 1000, "Horsepower": 1341.02},

    # Energy
    "Joule": {"Calorie": 0.239006, "Kilowatt-hour": 2.7778e-7, "Electronvolt": 6.242e18, "BTU": 0.000947817},
    "Calorie": {"Joule": 4.184},
    "Kilowatt-hour": {"Joule": 3.6e6},
      # Power
    "Watt": {"Kilowatt": 1/1000, "Horsepower": 1/745.7, "Megawatt": 1/1000000},
    "Kilowatt": {"Watt": 1000, "Horsepower": 1.34102, "Megawatt": 1/1000},
    "Horsepower": {"Watt": 745.7, "Kilowatt": 1/1.34102, "Megawatt": 1/1341.02},
    "Megawatt": {"Watt": 1000000, "Kilowatt": 1000, "Horsepower": 1341.02},

    # Force
    "Newton": {"Dyne": 1e5, "Pound-force": 0.224809, "Kilopond": 0.101972},
    "Dyne": {"Newton": 1e-5, "Pound-force": 2.24809e-6, "Kilopond": 1.01972e-6},
    "Pound-force": {"Newton": 4.44822, "Dyne": 4.44822e5, "Kilopond": 0.453592},
    "Kilopond": {"Newton": 9.80665, "Dyne": 9.80665e5, "Pound-force": 2.20462},

    # Data Storage
    "Byte": {"KB": 1/1024, "MB": 1/1048576, "GB": 1/1073741824, "TB": 1/1099511627776, "PB": 1/1125899906842624, "Bit": 8},
    "KB": {"Byte": 1024, "MB": 1/1024, "GB": 1/1048576, "TB": 1/1073741824, "PB": 1/1099511627776},
    "MB": {"Byte": 1048576, "KB": 1024, "GB": 1/1024, "TB": 1/1048576, "PB": 1/1073741824},
    "GB": {"Byte": 1073741824, "KB": 1048576, "MB": 1024, "TB": 1/1024, "PB": 1/1048576},
    "TB": {"Byte": 1099511627776, "KB": 1073741824, "MB": 1048576, "GB": 1024, "PB": 1/1024},
    "PB": {"Byte": 1125899906842624, "KB": 1099511627776, "MB": 1073741824, "GB": 1048576, "TB": 1024},

    # Fuel Efficiency
    "km/l": {"L/100km": 100, "mpg (US)": 2.35215, "mpg (UK)": 2.82481},
    "L/100km": {"km/l": 1/100, "mpg (US)": 235.215, "mpg (UK)": 282.481},
    "mpg (US)": {"km/l": 0.425144, "L/100km": 1/2.35215, "mpg (UK)": 1.20095},
    "mpg (UK)": {"km/l": 0.354006, "L/100km": 1/2.82481, "mpg (US)": 0.832674},

    # Angle
    "Degrees": {"Radians": 3.14159/180, "Gradians": 10/9},
    "Radians": {"Degrees": 180/3.14159, "Gradians": 200/3.14159},
    "Gradians": {"Degrees": 9/10, "Radians": 3.14159/200},

    # Frequency
    "Hertz": {"Kilohertz": 1/1000, "Megahertz": 1/1000000, "Gigahertz": 1/1000000000},
    "Kilohertz": {"Hertz": 1000, "Megahertz": 1/1000, "Gigahertz": 1/1000000},
    "Megahertz": {"Hertz": 1000000, "Kilohertz": 1000, "Gigahertz": 1/1000},
    "Gigahertz": {"Hertz": 1000000000, "Kilohertz": 1000000, "Megahertz": 1000},

    # Luminous Intensity
    "Candela": {"Lumen": 1, "Lux": 1},
    "Lumen": {"Candela": 1, "Lux": 1},
    "Lux": {"Candela": 1, "Lumen": 1},

    # Radioactivity
    "Becquerel": {"Curie": 1/3.7e10, "Sievert": 1},
    "Curie": {"Becquerel": 3.7e10, "Sievert": 1},
    "Sievert": {"Becquerel": 1, "Curie": 1},

    # Torque
    "Newton Meter": {"Pound-foot": 1/1.35582, "Dyne-centimeter": 1e7},
    "Pound-foot": {"Newton Meter": 1.35582, "Dyne-centimeter": 1.35582e7},
    "Dyne-centimeter": {"Newton Meter": 1e-7, "Pound-foot": 1/1.35582e7},

    # Electrical Conductance
    "Siemens": {"Mho": 1},
    "Mho": {"Siemens": 1},

    # Electrical Resistance
    "Ohm": {"Milliohm": 1000, "Kiloohm": 1/1000, "Megaohm": 1/1000000},
    "Milliohm": {"Ohm": 1/1000, "Kiloohm": 1/1000000, "Megaohm": 1/1000000000},
    "Kiloohm": {"Ohm": 1000, "Milliohm": 1000000, "Megaohm": 1/1000},
    "Megaohm": {"Ohm": 1000000, "Milliohm": 1e9, "Kiloohm": 1000},

    # Magnetic Flux
    "Weber": {"Maxwell": 1e8, "Tesla": 1, "Gauss": 1e4},
    "Maxwell": {"Weber": 1e-8, "Tesla": 1e-8, "Gauss": 0.1},
    "Tesla": {"Weber": 1, "Maxwell": 1e8, "Gauss": 10000},
    "Gauss": {"Weber": 1e-4, "Maxwell": 10, "Tesla": 1/10000},
}


    if from_unit == to_unit:
        return value 
    
    try:
        conversion = conversion_factors.get(from_unit, {}).get(to_unit)
        return conversion(value) if callable(conversion) else value * conversion if conversion else "Conversion Not Available"
    except (TypeError, KeyError):
        return "Conversion Not Available"

result = convert(value, from_unit, to_unit)
st.success(f"✅ {value} {from_unit} = {result} {to_unit}")

st.markdown("<p class='footer'>Developed by Seerat Fatima ❤️ | Powered by Streamlit 🚀</p>", unsafe_allow_html=True)
