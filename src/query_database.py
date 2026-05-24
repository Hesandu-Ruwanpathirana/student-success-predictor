import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]

cursor.execute("SELECT AVG(quiz_score) FROM students")
average_quiz_score = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM students WHERE final_result = 'pass'")
total_pass = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM students WHERE final_result = 'fail'")
total_fail = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM students WHERE attendance < 75")
low_attendance = cursor.fetchone()[0]

print("Total students:", total_students)
print("Average quiz score:", round(average_quiz_score, 2))
print("Students who passed:", total_pass)
print("Students who failed:", total_fail)
print("Students with attendance below 75:", low_attendance)

conn.close()