import streamlit as st
import pandas as pd
import numpy as np 

st.title("hello streamlit world")
st.write("this is a simple text")
color = st.color_picker("pick a color for background", "#6E9DBB")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

st.write("here is the dataframe:")
st.dataframe(df)

char_data = pd.DataFrame(
   50 + 15*np.random.randn(20, 3), columns=['a', 'b', 'c']
)
st.line_chart(char_data)

st.title("Streamlit Text input")

name = st.text_input("Enter your name", placeholder = "Type here...")

if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age", 0, 100, 25)

st.write(f"your age is: {age}")

options = ["python", "java", "c++", "javascript"]
choice = st.selectbox("Select your favorite programming language", options)

st.write(f"your favorite programming language is: {choice}")

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df2 = pd.DataFrame(data)
st.write(df2)







# Define your custom CSS targetting the main view container
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-color: {color};
}}

.st-key-custom_picker [data-baseweb="input"] {{
    border: 3px dashed white !important;
    border-radius: 8px;
}}
</style>
""", unsafe_allow_html=True)