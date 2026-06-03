import streamlit as st
import pickle
import pandas as pd

# Load Model
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page Configuration
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💰"
)

st.title("💰 Salary Prediction App")
st.write("Predict salary using Experience, Interview Score, and Age")

# Inputs
experience = st.slider("Experience (Years)", 0, 12, 6)
marks = st.slider("Interview Score", 0, 10, 5)
age = st.slider("Age", 23, 56, 32)

# Predict Button
if st.button("Predict Salary"):

    input_df = pd.DataFrame({
        "experience": [experience],
        "age": [age],
        "interview_score": [marks]
    })

    # st.write("Expected:", model.feature_names_in_)
    # st.write("Provided:", input_df.columns.tolist())

    prediction = model.predict(input_df)

    st.success(f"Predicted Salary: ₹{prediction[0]:,.2f}")