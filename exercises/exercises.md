# SQL Exercises

These exercises will help you practice the SQL concepts covered in the tutorial. Try to solve them on your own before looking at the solutions.

## Setup

First, make sure you have created the school database with the following tables:

- students (id, name, age, grade, email)
- courses (id, name, teacher, room, max_students)
- enrollments (id, student_id, course_id, enrollment_date, grade)

You can use the `complete_example.py` script to set up the database.

## Basic Exercises

### Exercise 1: SELECT Statements
1. Write a query to select all students in grade 11.
2. Write a query to select the names and teachers of all courses.
3. Write a query to find the oldest student.

### Exercise 2: Filtering
1. Find all students whose names contain the letter 'a'.
2. Find all courses taught in rooms that contain 'Lab' in their name.
3. Find all students who are either 16 years old or in grade 11.

### Exercise 3: Ordering
1. List all students ordered by age (youngest to oldest).
2. List all courses ordered by name alphabetically.
3. List all students ordered by grade (highest first) and then by name (alphabetically).

### Exercise 4: Limiting Results
1. Get the 3 youngest students.
2. Get courses 3-5 when ordered alphabetically.

### Exercise 5: Updating Records
1. Update the room for the Mathematics course to 'Room 102'.
2. Increase all students' ages by 1 (to simulate a new school year).
3. Change the grade of student with id=3 to 'A+' in the Computer Science course.

## Intermediate Exercises

### Exercise 6: Joins
1. List all students and the courses they're enrolled in.
2. Find all students who are enrolled in the Mathematics course.
3. Find all courses that have no students enrolled.

### Exercise 7: Aggregate Functions
1. Count how many students are in each grade.
2. Find the average age of students in grade 12.
3. Find the course with the most students enrolled.

### Exercise 8: Inserting Data
1. Add a new student named "Robert Johnson" who is 17 years old, in grade 11.
2. Add a new course called "Biology" taught by "Ms. Green" in "Lab 2".
3. Enroll Robert in Biology and Mathematics.

### Exercise 9: Deleting Records
1. Delete all enrollments for the student with id=1.
2. Delete the English Literature course (make sure to delete related enrollments first).

## Advanced Exercises

### Exercise 10: Complex Queries
1. Find students who are enrolled in both Mathematics and Computer Science.
2. Find the teacher who teaches the most students (based on course enrollments).
3. For each student, list their name and the number of courses they're enrolled in.

### Exercise 11: Database Design
1. Design a new table to track assignments for each course.
2. Design a table to store student attendance records.
3. Modify the courses table to include a department.

### Exercise 12: Transactions
1. Write a transaction that moves all students from grade 11 to grade 12.
2. Write a transaction that assigns a new teacher to all courses currently taught by "Mr. Anderson".

## Solutions

Solutions to these exercises are provided in the `exercise_solutions.md` file. Try to solve the exercises yourself before looking at the solutions!
