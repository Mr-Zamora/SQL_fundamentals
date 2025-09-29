# 11. Working with Multiple Tables

Now that you've created tables with relationships, it's time to learn how to work with data across multiple tables. The most powerful feature for this is the JOIN operation.

## What is a JOIN?

A JOIN combines rows from two or more tables based on a related column between them. This allows you to query data from multiple tables as if they were a single table.

## Setting Up Example Data

Let's first insert some sample data into our related tables:

```sql
-- Insert teachers
INSERT INTO teachers (id, name, subject, email) VALUES
    (1, 'Mr. Anderson', 'Mathematics', 'anderson@school.edu'),
    (2, 'Ms. Davis', 'English', 'davis@school.edu'),
    (3, 'Mrs. Wilson', 'Computer Science', 'wilson@school.edu');

-- Insert courses
INSERT INTO courses (id, name, room, teacher_id) VALUES
    (1, 'Algebra', '101', 1),
    (2, 'Calculus', '102', 1),
    (3, 'English Literature', '203', 2),
    (4, 'Creative Writing', '204', 2),
    (5, 'Programming', 'Lab 3', 3);

-- Insert students
INSERT INTO students (id, name, age, grade) VALUES
    (1, 'John Smith', 17, 12),
    (2, 'Sarah Johnson', 18, 12),
    (3, 'Michael Wong', 17, 12),
    (4, 'Emma Brown', 16, 11),
    (5, 'David Lee', 16, 11);

-- Insert enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES
    (1, 1, '2023-09-01'),  -- John in Algebra
    (1, 5, '2023-09-01'),  -- John in Programming
    (2, 2, '2023-09-01'),  -- Sarah in Calculus
    (2, 3, '2023-09-01'),  -- Sarah in English Literature
    (3, 2, '2023-09-01'),  -- Michael in Calculus
    (3, 5, '2023-09-01'),  -- Michael in Programming
    (4, 1, '2023-09-01'),  -- Emma in Algebra
    (4, 3, '2023-09-01'),  -- Emma in English Literature
    (5, 4, '2023-09-01'),  -- David in Creative Writing
    (5, 5, '2023-09-01');  -- David in Programming
```

## Types of JOINs

SQLite supports several types of JOINs:

### INNER JOIN

An INNER JOIN returns only the rows that have matching values in both tables:

```sql
SELECT 
    courses.name AS course_name,
    teachers.name AS teacher_name
FROM 
    courses
INNER JOIN 
    teachers ON courses.teacher_id = teachers.id;
```

This returns all courses with their corresponding teachers.

### LEFT JOIN (or LEFT OUTER JOIN)

A LEFT JOIN returns all rows from the left table and the matched rows from the right table. If there's no match, NULL values are returned for the right table's columns:

```sql
SELECT 
    teachers.name AS teacher_name,
    courses.name AS course_name
FROM 
    teachers
LEFT JOIN 
    courses ON teachers.id = courses.teacher_id;
```

This returns all teachers, even those who don't teach any courses (though in our example data, all teachers have courses).

### Cross JOIN

A CROSS JOIN returns the Cartesian product of both tables (every row from the first table combined with every row from the second table):

```sql
SELECT 
    students.name AS student_name,
    courses.name AS course_name
FROM 
    students
CROSS JOIN 
    courses;
```

This returns all possible combinations of students and courses, regardless of enrollment.

## Joining Multiple Tables

You can join more than two tables in a single query:

```sql
SELECT 
    students.name AS student_name,
    courses.name AS course_name,
    teachers.name AS teacher_name
FROM 
    students
INNER JOIN 
    enrollments ON students.id = enrollments.student_id
INNER JOIN 
    courses ON enrollments.course_id = courses.id
INNER JOIN 
    teachers ON courses.teacher_id = teachers.id;
```

This query returns a list of students with the courses they're enrolled in and the teachers who teach those courses.

## Using Aliases for Table Names

For complex queries with multiple tables, you can use aliases to make the query more readable:

```sql
SELECT 
    s.name AS student_name,
    c.name AS course_name,
    t.name AS teacher_name
FROM 
    students s
INNER JOIN 
    enrollments e ON s.id = e.student_id
INNER JOIN 
    courses c ON e.course_id = c.id
INNER JOIN 
    teachers t ON c.teacher_id = t.id;
```

## Filtering Joined Data

You can use WHERE clauses with JOINs to filter the results:

```sql
SELECT 
    s.name AS student_name,
    c.name AS course_name
FROM 
    students s
INNER JOIN 
    enrollments e ON s.id = e.student_id
INNER JOIN 
    courses c ON e.course_id = c.id
WHERE 
    s.grade = 12 AND c.name LIKE '%Programming%';
```

This returns grade 12 students enrolled in programming courses.

## Aggregating Joined Data

You can use aggregate functions with JOINs:

```sql
SELECT 
    c.name AS course_name,
    COUNT(e.student_id) AS student_count
FROM 
    courses c
LEFT JOIN 
    enrollments e ON c.id = e.course_id
GROUP BY 
    c.name;
```

This returns the number of students enrolled in each course.

## Self-Joins

You can join a table to itself (useful for hierarchical data):

```sql
SELECT 
    e1.name AS employee,
    e2.name AS manager
FROM 
    employees e1
LEFT JOIN 
    employees e2 ON e1.manager_id = e2.id;
```

This returns each employee with their manager's name.

## Common JOIN Problems

1. **Missing JOIN condition**: Without a JOIN condition, you get a cross join (Cartesian product)
2. **Incorrect JOIN condition**: Joining on the wrong columns gives incorrect results
3. **Ambiguous column names**: When tables have columns with the same name, you must qualify them with table names
4. **NULL values**: INNER JOINs exclude rows with NULL values in the join columns

## Practice Exercise: Working with Multiple Tables

1. List all students with the courses they're enrolled in
2. Find which teacher has the most students
3. List all courses with their teacher and the number of enrolled students
4. Find students who are taking both Mathematics and Computer Science courses
5. Find courses that have no students enrolled

## Next Steps

Now that you've learned how to work with related tables, in the next section we'll explore advanced SQL topics and next steps for your SQL journey.
