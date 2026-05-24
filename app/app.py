import streamlit as st
import joblib
import pandas as pd
import sqlite3

model = joblib.load("models/student_success_model.pkl")

st.title("Student Success Predictor")
st.write("Enter student details below to predict pass or fail.")

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]

cursor.execute("SELECT AVG(quiz_score) FROM students")
average_quiz_score = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM students WHERE final_result = 'pass'")
total_pass = cursor.fetchone()[0]

conn.close()

col1, col2, col3 = st.columns(3)
col1.metric("Total Students", total_students)
col2.metric("Average Quiz Score", f"{average_quiz_score:.2f}")
col3.metric("Students Passed", total_pass)

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
    probabilities = model.predict_proba(input_data)[0]
    fail_probability = probabilities[0]
    pass_probability = probabilities[1]

    if prediction == 1:
        st.success("Prediction: Pass")
    else:
        st.error("Prediction: Fail")

    st.write(f"Pass probability: {pass_probability:.2%}")
    st.write(f"Fail probability: {fail_probability:.2%}")