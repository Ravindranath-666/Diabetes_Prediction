import streamlit as st
import pickle 
import pandas as pd
# load model & scaler data
with open("model/model.pkl","rb") as f:
    model = pickle.load(f)
with open("model/scaler.pkl","rb") as f:
    scaler =pickle.load(f)
# streamlit user interface 
st.title("Diabetes Prediction")
# set images 
st.set_page_config(
    page_title = "Diabetes Prediction",
    page_icon = "Pictures/logo.png",
)
st.image("Pictures/baner.png", width = 300)
st.write("Enter Your Health deatils below")
# input fields
Pregnancies = st.number_input("Pregnancies", 0, 20, 1)
Glucose = st.number_input("Glucose", 0, 300, 120)
BloodPressure = st.number_input("BloodPressure", 0, 200, 70)
SkinThickness = st.number_input("SkinThickness", 0, 100, 20)
Insulin = st.number_input("Insulin", 0, 1000, 80)
BMI = st.number_input("BMI", 0.0, 100.0, 25.0)
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction", 0.0, 3.0, 0.5)
Age = st.number_input("Age", 0, 120, 30)
# input fields into data frame 
input_data = pd.DataFrame({
    "Pregnancies": [Pregnancies],
    "Glucose": [Glucose],
    "BloodPressure": [BloodPressure],
    "SkinThickness": [SkinThickness],
    "Insulin": [Insulin],
    "BMI": [BMI],
    "DiabetesPedigreeFunction": [DiabetesPedigreeFunction],
    "Age": [Age]
})
# scaler input 
input_scaler = scaler.transform(input_data)
# predict button
if st.button("Predict"):
    y_prob = model.predict_proba(input_scaler)[:,1]
    y_pred = (y_prob >= 0.4).astype(int)
    if y_pred[0] == 1:
        st.error("Diabtes : YES")
    else:
        st.success("Diabetes : NO")