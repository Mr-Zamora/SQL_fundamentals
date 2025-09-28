# SQL Exercise Solutions

Below are the solutions to the exercises in the `exercises.md` file.

## Basic Exercises

### Exercise 1: SELECT Statements

1. Select all students in grade 11:
```sql
SELECT * FROM students WHERE grade = 11;
```

2. Select the names and teachers of all courses:
```sql
SELECT name, teacher FROM courses;
```

3. Find the oldest student:
```sql
SELECT * FROM students ORDER BY age DESC LIMIT 1;
```

### Exercise 2: Filtering

1. Find all students whose names contain the letter 'a':
```sql
SELECT * FROM students WHERE name LIKE '%a%';
```

2. Find all courses taught in rooms that contain 'Lab' in their name:
```sql
SELECT * FROM courses WHERE room LIKE '%Lab%';
```

3. Find all students who are either 16 years old or in grade 11:
```sql
SELECT * FROM students WHERE age = 16 OR grade = 11;
```

### Exercise 3: Ordering

1. List all students ordered by age (youngest to oldest):
```sql
SELECT * FROM students ORDER BY age ASC;
```

2. List all courses ordered by name alphabetically:
```sql
SELECT * FROM courses ORDER BY name ASC;
```

3. List all students ordered by grade (highest first) and then by name (alphabetically):
```sql
SELECT * FROM students ORDER BY grade DESC, name ASC;
```

### Exercise 4: Limiting Results

1. Get the 3 youngest students:
```sql
SELECT * FROM students WHERE age IS NOT NULL ORDER BY age ASC LIMIT 3;
```

2. Get courses 3-5 when ordered alphabetically:
```sql
SELECT * FROM courses ORDER BY name ASC LIMIT 3 OFFSET 2;
```

### Exercise 5: Updating Records

1. Update the room for the Mathematics course to 'Room 102':
```sql
UPDATE courses SET room = 'Room 102' WHERE name = 'Mathematics';
```

2. Increase all students' ages by 1:
```sql
UPDATE students SET age = age + 1 WHERE age IS NOT NULL;
```

3. Change the grade of student with id=3 in the Computer Science course:
```sql
UPDATE enrollments 
SET grade = 'A+' 
WHERE student_id = 3 
AND course_id = (SELECT id FROM courses WHERE name = 'Computer Science');
```

## Intermediate Exercises

### Exercise 6: Joins

1. List all students and the courses they're enrolled in:
```sql
SELECT students.name, courses.name as course_name
FROM students
JOIN enrollments ON students.id = enrollments.student_id
JOIN courses ON enrollments.course_id = courses.id
ORDER BY students.name, courses.name;
```

2. Find all students who are enrolled in the Mathematics course:
```sql
SELECT students.*
FROM students
JOIN enrollments ON students.id = enrollments.student_id
JOIN courses ON enrollments.course_id = courses.id
WHERE courses.name = 'Mathematics';
```

3. Find all courses that have no students enrolled:
```sql
SELECT courses.*
FROM courses
LEFT JOIN enrollments ON courses.id = enrollments.course_id
WHERE enrollments.id IS NULL;
```

### Exercise 7: Aggregate Functions

1. Count how many students are in each grade:
```sql
SELECT grade, COUNT(*) as student_count
FROM students
GROUP BY grade
ORDER BY grade DESC;
```

2. Find the average age of students in grade 12:
```sql
SELECT AVG(age) as average_age
FROM students
WHERE grade = 12;
```

3. Find the course with the most students enrolled:
```sql
SELECT courses.name, COUNT(enrollments.id) as enrollment_count
FROM courses
JOIN enrollments ON courses.id = enrollments.course_id
GROUP BY courses.id
ORDER BY enrollment_count DESC
LIMIT 1;
```

### Exercise 8: Inserting Data

1. Add a new student:
```sql
INSERT INTO students (name, age, grade, email)
VALUES ('Robert Johnson', 17, 11, 'robert.j@school.edu');
```

2. Add a new course:
```sql
INSERT INTO courses (name, teacher, room, max_students)
VALUES ('Biology', 'Ms. Green', 'Lab 2', 28);
```

3. Enroll Robert in Biology and Mathematics:
```sql
-- First, get Robert's ID
-- Assuming Robert's ID is 9 (check after inserting)
-- And assuming Biology's ID is 6 and Mathematics' ID is 1 (check after inserting)

INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES 
    (9, 6, '2023-09-15', NULL),
    (9, 1, '2023-09-15', NULL);
```

### Exercise 9: Deleting Records

1. Delete all enrollments for the student with id=1:
```sql
DELETE FROM enrollments WHERE student_id = 1;
```

2. Delete the English Literature course:
```sql
-- First, delete related enrollments
DELETE FROM enrollments 
WHERE course_id = (SELECT id FROM courses WHERE name = 'English Literature');

-- Then, delete the course
DELETE FROM courses WHERE name = 'English Literature';
```

## Advanced Exercises

### Exercise 10: Complex Queries

1. Find students who are enrolled in both Mathematics and Computer Science:
```sql
SELECT s.name
FROM students s
JOIN enrollments e1 ON s.id = e1.student_id
JOIN enrollments e2 ON s.id = e2.student_id
JOIN courses c1 ON e1.course_id = c1.id
JOIN courses c2 ON e2.course_id = c2.id
WHERE c1.name = 'Mathematics' AND c2.name = 'Computer Science'
GROUP BY s.id;
```

2. Find the teacher who teaches the most students:
```sql
SELECT courses.teacher, COUNT(DISTINCT enrollments.student_id) as student_count
FROM courses
JOIN enrollments ON courses.id = enrollments.course_id
GROUP BY courses.teacher
ORDER BY student_count DESC
LIMIT 1;
```

3. For each student, list their name and the number of courses they're enrolled in:
```sql
SELECT students.name, COUNT(enrollments.id) as course_count
FROM students
LEFT JOIN enrollments ON students.id = enrollments.student_id
GROUP BY students.id
ORDER BY course_count DESC, students.name;
```

### Exercise 11: Database Design

1. Design a table to track assignments for each course:
```sql
CREATE TABLE assignments (
    id INTEGER PRIMARY KEY,
    course_id INTEGER,
    title TEXT NOT NULL,
    description TEXT,
    due_date TEXT,
    max_points INTEGER,
    FOREIGN KEY (course_id) REFERENCES courses (id)
);
```

2. Design a table to store student attendance records:
```sql
CREATE TABLE attendance (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    date TEXT,
    status TEXT CHECK(status IN ('present', 'absent', 'late', 'excused')),
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id)
);
```

3. Modify the courses table to include a department:
```sql
-- Add a department column to the courses table
ALTER TABLE courses ADD COLUMN department TEXT;

-- Update existing courses with departments
UPDATE courses SET department = 'Mathematics' WHERE name = 'Mathematics';
UPDATE courses SET department = 'English' WHERE name = 'English Literature';
UPDATE courses SET department = 'Computer Science' WHERE name = 'Computer Science';
UPDATE courses SET department = 'Science' WHERE name = 'Physics';
UPDATE courses SET department = 'Social Studies' WHERE name = 'History';
UPDATE courses SET department = 'Science' WHERE name = 'Biology';
```

### Exercise 12: Transactions

1. Transaction to move all students from grade 11 to grade 12:
```sql
BEGIN TRANSACTION;

-- Check how many students will be affected
SELECT COUNT(*) FROM students WHERE grade = 11;

-- Update the grade
UPDATE students SET grade = 12 WHERE grade = 11;

-- Verify the update
SELECT COUNT(*) FROM students WHERE grade = 11;
SELECT COUNT(*) FROM students WHERE grade = 12;

-- If everything looks good
COMMIT;

-- If something went wrong
-- ROLLBACK;
```

2. Transaction to assign a new teacher to all courses taught by "Mr. Anderson":
```sql
BEGIN TRANSACTION;

-- Check which courses will be affected
SELECT * FROM courses WHERE teacher = 'Mr. Anderson';

-- Update the teacher
UPDATE courses SET teacher = 'Ms. Thompson' WHERE teacher = 'Mr. Anderson';

-- Verify the update
SELECT * FROM courses WHERE teacher = 'Ms. Thompson';
SELECT * FROM courses WHERE teacher = 'Mr. Anderson';

-- If everything looks good
COMMIT;

-- If something went wrong
-- ROLLBACK;
```
