**Phishing Website Detector (Mini Project)**

=========================================



This project is a phishing website detector built using Machine Learning and Streamlit. It detects phishing URLs based on three core features.







**Features Used**

**-------------**

• Presence of an IP address in the URL

• Presence of the '@' symbol

• Length of the URL

• Check whether the URL starts with "https" or "http"

• Count the number of subdomains in the URL

• Count the number of hyphens ("-") in the domain name

• Identify suspicious keywords in the URL such as "login", "secure", "verify", etc.



These improvements can make the model more robust and the app more user-friendly.





**Technologies Used**

**-----------------**

• Python

• Pandas

• scikit-learn

• Streamlit



---



**Project Files**

**-------------**

• phishing\_dataset.csv – Sample dataset with 3 features

• train\_model.py – Python script to train the ML model

• phishing\_model.pkl – Trained model saved using pickle

• phishing\_app.py – Streamlit GUI to interact with the model

• README.md – Project documentation



---



**How to Run**

**----------**

1\. Install required libraries (if not already installed):

&nbsp;  

&nbsp;  • pip install pandas scikit-learn streamlit



2\. Train the model (optional if phishing\_model.pkl is already present):



&nbsp;  • python train\_model.py



3\. Run the Streamlit application:



&nbsp;  • streamlit run phishing\_app.py



4.Example Test URLs



Use the following example URLs to test the application:



• http://203.0.113.0 → Expected: Phishing



• http://login@bank.com → Expected: Phishing



• https://www.google.com → Expected: Legitimate





**Project Purpose**

**---------------**



This is a mini project developed for academic use (BSc IT - Machine Learning subject) to demonstrate phishing website detection using basic ML techniques and a simple GUI.







