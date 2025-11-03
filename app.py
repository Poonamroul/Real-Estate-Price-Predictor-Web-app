# Import necessary libraries
import streamlit as st
import joblib
import numpy as np

# ------------------ CSS Styling ------------------
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Teko:wght@300&display=swap');

.stApp {
    background-image: url('https://images.unsplash.com/photo-1588557132645-ff567110cafd?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 100vh;
    font-family: 'Times New Roman', Times, serif !important;
}

html, body, [class*="css"] {
    font-family: 'Times New Roman', Times, serif !important;
}

.stNumberInput input {
    background-color: #fff !important;
    color: #888 !important;
}

.stNumberInput label, .stNumberInput span {
    color: #fff !important;
}

.stNumberInput button {
    background-color: #fff !important;
    color: #888 !important;
    border: 1px solid #ccc !important;
}

.stButton > button {
    background-color: #00FF00 !important;
    color: #fff !important;
    border: none !important;
    transition: box-shadow 0.3s;
}

.stButton > button:hover {
    box-shadow: 0 0 20px 5px #00FF00;
}

.custom-title {
    font-family: 'Teko', 'Times New Roman', Times, serif !important;
    font-size: 3rem;
    color: #fff;
    font-weight: 300;
    text-shadow: 3px 3px 12px #888888, 0 0 10px #000;
    margin-bottom: 0.5em;
    margin-top: 0.5em;
    text-align: center;
    letter-spacing: 2px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ------------------ Load Model ------------------
model = joblib.load("model.pkl")

# ------------------ Title ------------------
st.markdown("<h1 class='custom-title'>PREDICT HOUSE PRICE OF INDIA</h1>", unsafe_allow_html=True)
st.divider()

# ------------------ Description ------------------
st.markdown(
    "<div style='font-family: Times New Roman, Times, serif; font-size: 1.2rem; color: #fff;'>"
    "This app uses machine learning for predicting house prices based on given features of the house. "
    "To use this app, enter the inputs in the user interface and then click the Predict button."
    "</div>",
    unsafe_allow_html=True
)
st.divider()

# ------------------ Input Fields ------------------
bedrooms = st.number_input("Number of bedrooms", min_value=0, value=0)
bathrooms = st.number_input("Number of bathrooms", min_value=0, value=0)
livingarea = st.number_input("Sq Ft Living area", min_value=0, value=2000)
Balcony = st.number_input("Number of Balcony", min_value=0, value=3)
schools = st.number_input("Number of schools nearby", min_value=0, value=0)

st.divider()

# ------------------ Prediction ------------------
X = [[bedrooms, bathrooms, livingarea, Balcony, schools]]
predictbutton = st.button("Predict!")

if predictbutton:
    st.snow()
    st.balloons()
    X_array = np.array(X)
    prediction = model.predict(X_array)
    st.markdown(
        f"<h2 style=\"color:#ffffff; font-size:2.5rem; font-weight:bold; "
        f"font-family: 'Times New Roman', Times, serif; "
        f"text-shadow: 2px 2px 8px #007700, 0 0 10px #00FF00;\">"
        f"Price prediction is ₹{prediction[0]:,.0f}</h2>",
        unsafe_allow_html=True
    )
else:
    st.write("Please use predict button after entering values.")
