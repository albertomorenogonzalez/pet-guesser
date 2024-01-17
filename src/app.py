import streamlit as st
import pandas as pd
import joblib
clf = joblib.load("model/pet_model.pkl")

st.title('Guess your pet!')

height = st.number_input('Height:')
weight = st.number_input('Weight:')
eye_color = st.selectbox(
    'Select Eye Colour',
    ('Brown', 'Blue')
)

if st.button('Submit'):
    X = pd.DataFrame([[height, weight, eye_color]], columns=["Height", "Weight", "Eye"])
    X = X.replace(["Brown", "Blue"], [1, 0])
    prediction = clf.predict(X)[0]
    st.text(f"This pet is a {prediction}")