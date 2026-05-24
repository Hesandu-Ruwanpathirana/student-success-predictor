import sqlite3
import pandas as pd

df = pd.read_csv("data/students.csv")

conn = sqlite3.connect("students.db")

df.to_sql("students", conn, if_exists="replace", index=False)

print("Database created and CSV loaded into students table.")

conn.close()