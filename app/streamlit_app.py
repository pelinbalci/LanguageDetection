import streamlit as st
import json
import requests

st.title("Language Detection Model")
st.write("")
title = st.text_input('Input text', 'Please enter the text here')
st.write('The current text is', title)

inputs = {"text": title}

if st.button("Detect Language"):
    res = requests.post(url = "http://0.0.0.0:80/predict", data=json.dumps(inputs))

    st.subheader(f"response from API = {res.text}")