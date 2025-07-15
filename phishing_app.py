# phishing_app.py

import streamlit as st
import pickle
import numpy as np
import re
import validators

# check URL validity
def is_valid_url(url):
    return validators.url(url)

# Load the trained model
with open("phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("🔐 Phishing Website Detector")
st.markdown("Enter a website URL and find out if it's **Phishing** or **Legitimate** 🕵️‍♂️")

# User input
url = st.text_input("🌐 Enter Website URL")

# Feature extraction from URL
def extract_features(url):
    has_ip = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    has_at = 1 if '@' in url else 0
    url_length = len(url)
    return np.array([has_ip, has_at, url_length]).reshape(1, -1)

# Check button
if st.button("🔎 Check Now"):
    if url:
        features = extract_features(url)
        prediction = model.predict(features)[0]
        if prediction == 1:
            st.error("🚨 This is a Phishing Website!")
        else:
            st.success("✅ This is a Legitimate Website.")
    else:
        st.warning("⚠️ Please enter a valid URL.")

     
