# Student Success Predictor

An end-to-end machine learning project that predicts whether a student is likely to pass or fail based on study habits and academic performance data.

## Features

- Loads student data from a CSV file
- Prepares data for machine learning
- Trains a Logistic Regression model
- Saves the trained model with joblib
- Uses a Streamlit app for interactive predictions
- Displays pass/fail probability

## Tech Stack

- Python
- pandas
- scikit-learn
- Streamlit
- joblib

## Project Structure

```text
student-success-predictor/
│
├── app/
│   └── app.py
├── data/
│   └── students.csv
├── models/
│   └── student_success_model.pkl
├── src/
│   ├── load_data.py
│   ├── prepare_data.py
│   ├── train_model.py
│   └── save_model.py
└── README.md
```

## How to Run

1. Install dependencies:

```bash
pip3 install pandas scikit-learn streamlit joblib
```

2. Train the model:

```bash
python3 src/train_model.py
```

3. Save the model:

```bash
python3 src/save_model.py
```

4. Run the Streamlit app:

```bash
streamlit run app/app.py
```

## Example Input

- Study Hours: 3
- Attendance: 70
- Assignments Completed: 7
- Quiz Score: 82
- Sleep Hours: 10

## Future Improvements

- Add SQL database integration
- Expand the dataset
- Improve the UI
- Add more model evaluation metrics

## Author

Hesandu Ruwanpathirana

## Live App - https://student-success-predictor-n423v9vzpr2mbb2bvwijbv.streamlit.app
