# Student Success Predictor

An end-to-end machine learning project that predicts whether a student is likely to pass or fail based on study habits and academic performance data. The project uses Python, SQLite, scikit-learn, and Streamlit to cover the full workflow from data handling to live prediction.

## Live Demo

[Open the deployed app here](PASTE_YOUR_STREAMLIT_LINK_HERE)

## Project Overview

This project was built to demonstrate a complete beginner-friendly machine learning pipeline. It stores student data in a SQLite database, trains a classification model, and provides a Streamlit web app where users can enter student details and receive a pass/fail prediction with probabilities.

## Features

- Loads and prepares student performance data for machine learning.
- Trains a machine learning model to predict pass/fail outcomes.
- Saves the trained model using `joblib` for reuse in the web app.
- Uses SQLite to store and query student records.
- Displays database metrics such as total students, average quiz score, and students passed in the Streamlit app.
- Allows users to enter new student data and generate predictions in real time.
- Saves new prediction inputs back into the database through the app workflow.

## Tech Stack

- Python
- Pandas
- scikit-learn
- Joblib
- SQLite
- Streamlit

## Project Structure

```bash
student-success-predictor/
├── app/
│   └── app.py
├── data/
│   └── student_data.csv
├── models/
│   └── student_success_model.pkl
├── src/
│   ├── train_model.py
│   ├── insert_data.py
│   └── query_database.py
├── students.db
├── requirements.txt
└── README.md
```

## How It Works

1. Student data is collected and stored in SQLite.
2. The dataset is processed in Python for training.
3. A machine learning model predicts whether a student will pass or fail.
4. The Streamlit app lets users input student information and view prediction results instantly.
5. New prediction records can be inserted into the database from the app itself.

## Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/student-success-predictor.git
cd student-success-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app/app.py
```

## Requirements

The main dependencies used in this project are:

```txt
streamlit
pandas
scikit-learn
joblib
```

## Future Improvements

- Add charts for student performance trends.
- Show model accuracy and evaluation metrics inside the app.
- Add filters and search for stored student records.
- Improve the UI design and layout.
- Deploy updated versions with more realistic datasets.

## Why This Project Matters

This project shows practical skills in machine learning, Python programming, SQL databases, and simple model deployment. It is a strong beginner portfolio project because it demonstrates more than just model training; it shows the full flow from data storage to user interaction in a live app.

## Author

**Hesandu Ruwanpathirana**  
AI and Data Science student interested in machine learning, software development, and building real-world AI projects.
