import streamlit as st

def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(c):
    return (c * 9.0 / 5.0) + 32

st.title("Temperature Converter")

st.sidebar.header("Choose Conversion Type")
conversion_type = st.sidebar.radio("Convert:", ("Fahrenheit to Celsius", "Celsius to Fahrenheit"))

if conversion_type == "Fahrenheit to Celsius":
    f_input = st.number_input("Enter temperature in Fahrenheit:", value=32.0)
    c_output = fahrenheit_to_celsius(f_input)
    st.write(f"{f_input} °F is {c_output:.2f} °C")

elif conversion_type == "Celsius to Fahrenheit":
    c_input = st.number_input("Enter temperature in Celsius:", value=0.0)
    f_output = celsius_to_fahrenheit(c_input)
    st.write(f"{c_input} °C is {f_output:.2f} °F")
