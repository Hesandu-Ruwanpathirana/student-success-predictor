import pandas as pd

def main():
    df = pd.read_csv("data/students.csv")
    print("First 5 rows:")
    print(df.head())
    print("\nSummary:")
    print(df.describe(include="all"))

if __name__ == "__main__":
    main()