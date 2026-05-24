# student-success-predictor

An end-to-end machine learning project that predicts student pass/fail outcomes using Python, scikit-learn, and Streamlit.

## Features
- Loads and analyzes student data
- Trains a Logistic Regression model
- Predicts student success from input features
- Shows pass/fail probability in a Streamlit app

## Tech Stack
- Python
- pandas
- scikit-learn
- Streamlit
- joblib

## Project Structure
- `data/` - dataset
- `src/` - training and preprocessing scripts
- `models/` - saved model files
- `app/` - Streamlit application

### How to Run
```bash
pip3 install pandas scikit-learn streamlit joblib
python3 src/train_model.py
python3 src/save_model.py
streamlit run app/app.py
```
