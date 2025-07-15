# phishing_app.py

import streamlit as st
import pickle
import numpy as np
import re
import validators

# ✅ Check if it's a valid URL
def is_valid_url(url):
    return validators.url(url)

# ✅ Feature extraction from URL
def extract_features(url):
    has_ip = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0  # Checks for IP address
    has_at = 1 if '@' in url else 0                             # Checks for '@'
    url_length = len(url)                                       # Length of URL
    count_dots = url.count('.')                                 # Number of dots
    has_https = 1 if url.startswith("https") else 0             # Checks if it uses HTTPS

    return np.array([has_ip, has_at, url_length, count_dots, has_https]).reshape(1, -1)

# ✅ Load the trained model
with open("phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

# ✅ Streamlit UI
st.title("🔐 Phishing Website Detector")
st.markdown("Enter a website URL and find out if it's **Phishing** or **Legitimate** 🕵️‍♂️")

# ✅ User input
url = st.text_input("🌐 Enter Website URL")

# ✅ When button is clicked
if st.button("🔍 Check Now"):
    if not is_valid_url(url):
        st.error("🚫 Invalid URL format. Please enter a valid website URL (e.g., https://example.com)")
    else:
        features = extract_features(url)
        prediction = model.predict(features)[0]

        if prediction == 1:
            st.error("⚠️ This is a Phishing Website!")
        else:
            st.success("✅ This is a Legitimate Website.")
