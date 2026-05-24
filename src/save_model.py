import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def main():
    df = pd.read_csv("data/students.csv")

    df["final_result"] = df["final_result"].map({"fail": 0, "pass": 1})

    X = df[["study_hours", "attendance", "assignments_completed", "quiz_score", "sleep_hours"]]
    y = df["final_result"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, "models/student_success_model.pkl")
    print("Model saved to models/student_success_model.pkl")

if __name__ == "__main__":
    main()