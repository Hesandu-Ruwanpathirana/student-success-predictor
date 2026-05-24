import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    df = pd.read_csv("data/students.csv")

    df["final_result"] = df["final_result"].map({"fail": 0, "pass": 1})

    X = df[["study_hours", "attendance", "assignments_completed", "quiz_score", "sleep_hours"]]
    y = df["final_result"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)

    print("\nFirst 5 rows of X_train:")
    print(X_train.head())

    print("\nFirst 5 values of y_train:")
    print(y_train.head())

if __name__ == "__main__":
    main()