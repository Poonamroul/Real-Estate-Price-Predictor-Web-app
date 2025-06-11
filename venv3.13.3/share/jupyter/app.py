import streamlit as st
import joblib
import numpy as np

# Set full-page background image using CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1588557132645-ff567110cafd?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');        
        background-size: cover; 
        background-position: center; 
        background-repeat: no-repeat;
        height: 100vh;
    }
    /* Make input boxes white and user input text gray */
    .stNumberInput input {
        background-color: #fff !important;
        color: #888 !important; /* gray user input */
    }
    .stNumberInput label, .stNumberInput span {
        color: #fff !important;
    }
    /* Make increment/decrement buttons white with gray symbols */
    .stNumberInput button {
        background-color: #fff !important;
        color: #888 !important; /* gray symbols */
        border: 1px solid #ccc !important;
    }
    /* Make the Predict button green with white text */
    .stButton > button {
        background-color: #00FF00 !important; 
        color: #fff !important; 
        border: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

model = joblib.load("model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("This app uses machine learning for predicting house prices based on given features of the house. For using this app you can enter the inputs from this user interface ad then use predict button.")

st.divider()

bedrooms = st.number_input("Number of bedrooms", min_value = 0, value = 0)
bathrooms = st.number_input("Number of bathrooms", min_value = 0, value = 0)
livingarea = st.number_input("Living area", min_value = 0, value = 2000)
condition = st.number_input("Condition of the house", min_value = 0, value = 3)
schools = st.number_input("Number of schools nearby", min_value = 0, value = 0)

st.divider()

X = [[bedrooms, bathrooms, livingarea, condition, schools]]

predictbutton = st.button("Predict!")

if predictbutton:
    st.balloons()
    X_array = np.array(X)
    prediction = model.predict(X_array)
    st.write(f"Price prediction is {prediction}")
else:
    st.write("Please use predict button after entering values.")
    
#Order of X ['number of bedrooms', 'number of bathrooms', 'living area',
#'condition of the house', 'Number of schools nearby']