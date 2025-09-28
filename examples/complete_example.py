"""
Complete SQL Example - School Database

This script demonstrates all the SQL concepts covered in the tutorial
by creating and working with a school database.
"""

import sqlite3
import os

# Delete the database if it already exists (for demonstration purposes)
if os.path.exists('school.db'):
    os.remove('school.db')

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON")

print("1. Creating tables...")
# Create tables
cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade INTEGER,
    email TEXT UNIQUE
)
''')

cursor.execute('''
CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher TEXT,
    room TEXT,
    max_students INTEGER
)
''')

cursor.execute('''
CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    grade TEXT,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id)
)
''')

print("2. Inserting data...")
# Insert students
cursor.execute('''
INSERT INTO students (name, age, grade, email)
VALUES 
    ('John Smith', 17, 12, 'john.smith@school.edu'),
    ('Sarah Johnson', 18, 12, 'sarah.j@school.edu'),
    ('Michael Wong', 17, 12, 'michael.w@school.edu'),
    ('Emma Brown', 16, 11, 'emma.b@school.edu'),
    ('David Lee', 16, 11, 'david.lee@school.edu'),
    ('Lisa Chen', 17, 11, 'lisa.c@school.edu'),
    ('James Wilson', 18, 12, 'james.w@school.edu'),
    ('Olivia Martinez', 16, 11, 'olivia.m@school.edu')
''')

# Insert courses
cursor.execute('''
INSERT INTO courses (name, teacher, room, max_students)
VALUES 
    ('Mathematics', 'Mr. Anderson', 'Room 101', 30),
    ('English Literature', 'Ms. Davis', 'Room 203', 25),
    ('Computer Science', 'Mrs. Wilson', 'Lab 3', 20),
    ('Physics', 'Dr. Brown', 'Lab 1', 24),
    ('History', 'Mr. Thompson', 'Room 105', 30)
''')

# Insert enrollments
cursor.execute('''
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES 
    (1, 1, '2023-09-01', 'A'),
    (1, 3, '2023-09-01', 'A-'),
    (2, 1, '2023-09-01', 'B+'),
    (2, 2, '2023-09-01', 'A'),
    (3, 1, '2023-09-01', 'B'),
    (3, 3, '2023-09-01', 'A'),
    (3, 4, '2023-09-01', 'B+'),
    (4, 2, '2023-09-01', 'A-'),
    (4, 5, '2023-09-01', 'B'),
    (5, 4, '2023-09-01', 'A'),
    (5, 5, '2023-09-01', 'B+'),
    (6, 1, '2023-09-01', 'A-'),
    (6, 2, '2023-09-01', 'B'),
    (7, 3, '2023-09-01', 'A'),
    (7, 4, '2023-09-01', 'A-'),
    (8, 2, '2023-09-01', 'B+'),
    (8, 5, '2023-09-01', 'A')
''')

print("\n3. Basic SELECT examples:")
# Select all students
cursor.execute("SELECT * FROM students")
print("\nAll students:")
for row in cursor.fetchall():
    print(row)

# Select specific columns
cursor.execute("SELECT name, grade FROM students")
print("\nStudent names and grades:")
for row in cursor.fetchall():
    print(row)

print("\n4. Filtering data examples:")
# Filter with WHERE
cursor.execute("SELECT * FROM students WHERE grade = 12")
print("\nGrade 12 students:")
for row in cursor.fetchall():
    print(row)

# Using LIKE
cursor.execute("SELECT * FROM students WHERE name LIKE 'J%'")
print("\nStudents whose names start with J:")
for row in cursor.fetchall():
    print(row)

# Combining conditions
cursor.execute("SELECT * FROM students WHERE grade = 12 AND age >= 18")
print("\nGrade 12 students who are 18 or older:")
for row in cursor.fetchall():
    print(row)

print("\n5. Ordering results examples:")
# Basic ORDER BY
cursor.execute("SELECT * FROM students ORDER BY name")
print("\nStudents ordered by name:")
for row in cursor.fetchall():
    print(row)

# Multiple columns
cursor.execute("SELECT * FROM students ORDER BY grade DESC, name ASC")
print("\nStudents ordered by grade (descending) and then by name:")
for row in cursor.fetchall():
    print(row)

print("\n6. Limiting results examples:")
# Basic LIMIT
cursor.execute("SELECT * FROM students LIMIT 3")
print("\nFirst 3 students:")
for row in cursor.fetchall():
    print(row)

# LIMIT with OFFSET
cursor.execute("SELECT * FROM students LIMIT 3 OFFSET 3")
print("\nStudents 4-6:")
for row in cursor.fetchall():
    print(row)

print("\n7. Updating records example:")
# Update a record
cursor.execute("UPDATE students SET age = 17 WHERE id = 5")
cursor.execute("SELECT * FROM students WHERE id = 5")
print("\nUpdated student (id=5):")
print(cursor.fetchone())

print("\n8. Join examples:")
# Inner join
cursor.execute('''
SELECT students.name, courses.name as course_name, enrollments.grade
FROM students
INNER JOIN enrollments ON students.id = enrollments.student_id
INNER JOIN courses ON enrollments.course_id = courses.id
ORDER BY students.name, courses.name
''')
print("\nStudents and their courses:")
for row in cursor.fetchall():
    print(row)

print("\n9. Aggregate function examples:")
# COUNT
cursor.execute("SELECT COUNT(*) FROM students")
print("\nTotal number of students:", cursor.fetchone()[0])

# AVG
cursor.execute("SELECT AVG(age) FROM students")
print("Average student age:", cursor.fetchone()[0])

# GROUP BY
cursor.execute('''
SELECT grade, COUNT(*) as student_count
FROM students
GROUP BY grade
''')
print("\nNumber of students in each grade:")
for row in cursor.fetchall():
    print(f"Grade {row[0]}: {row[1]} students")

# More complex query
cursor.execute('''
SELECT courses.name, COUNT(enrollments.id) as enrollment_count
FROM courses
LEFT JOIN enrollments ON courses.id = enrollments.course_id
GROUP BY courses.id
ORDER BY enrollment_count DESC
''')
print("\nCourses by popularity:")
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]} students")

print("\n10. Demonstrating transactions:")
# Start a transaction
cursor.execute("BEGIN TRANSACTION")

try:
    # Delete a student
    cursor.execute("DELETE FROM enrollments WHERE student_id = 8")
    cursor.execute("DELETE FROM students WHERE id = 8")
    
    # Verify deletion
    cursor.execute("SELECT * FROM students WHERE id = 8")
    result = cursor.fetchone()
    print("\nAfter deletion, student 8 exists:", result is not None)
    
    # Commit the transaction
    cursor.execute("COMMIT")
    print("Transaction committed successfully")
except Exception as e:
    # Rollback in case of error
    cursor.execute("ROLLBACK")
    print(f"Transaction rolled back due to error: {e}")

print("\nDatabase operations completed successfully!")

# Close the connection
conn.close()
