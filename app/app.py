import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/student_success_model.pkl")

st.title("Student Success Predictor")
st.write("Enter student details below to predict pass or fail.")

study_hours = st.number_input("Study Hours", min_value=0, max_value=12, value=4)
attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=80)
assignments_completed = st.number_input("Assignments Completed", min_value=0, max_value=10, value=6)
quiz_score = st.number_input("Quiz Score", min_value=0, max_value=100, value=70)
sleep_hours = st.number_input("Sleep Hours", min_value=0, max_value=12, value=7)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "assignments_completed": assignments_completed,
        "quiz_score": quiz_score,
        "sleep_hours": sleep_hours
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Prediction: Pass")
    else:
        st.error("Prediction: Fail")