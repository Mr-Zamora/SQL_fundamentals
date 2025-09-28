# 5. Reading Data (SELECT)

The SELECT statement is used to retrieve data from a database. It's the most commonly used SQL command and has many variations.

## Basic SELECT Syntax

The basic syntax for retrieving data is:

```sql
SELECT column1, column2, ...
FROM table_name;
```

Where:
- The columns you list after SELECT are the ones you want to retrieve
- `table_name` is the table you want to get data from

## Retrieving All Columns

To retrieve all columns from a table, use the asterisk (*) wildcard:

```sql
SELECT * FROM students;
```

This will return all rows and all columns from the students table.

### Running this in SQLite CLI:

```
sqlite> SELECT * FROM students;
id  name           age  grade
--  -------------  ---  -----
1   John Smith     17   12
2   Sarah Johnson  18   12
3   Michael Wong   17   12
4   Emma Brown     16   11
5   David Lee      NULL 11
```

### Running this in Python:

```python
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

# Fetch all rows
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
```

## Selecting Specific Columns

To retrieve only specific columns:

```sql
SELECT name, grade FROM students;
```

This returns only the name and grade columns for all students.

## Filtering Data with WHERE

The WHERE clause lets you filter which rows are returned:

```sql
SELECT * FROM students WHERE grade = 12;
```

This returns all columns, but only for students in grade 12.

## Using Expressions in SELECT

You can use expressions in your SELECT statements:

```sql
SELECT name, age, age + 1 AS next_year_age FROM students;
```

This calculates each student's age next year and returns it as a column named "next_year_age".

## Column Aliases

You can rename columns in the result using AS:

```sql
SELECT 
    name AS student_name,
    grade AS current_grade
FROM students;
```

This makes the result columns appear with the names "student_name" and "current_grade".

## Distinct Values

To retrieve only unique values, use DISTINCT:

```sql
SELECT DISTINCT grade FROM students;
```

This returns each grade level that appears in the table, but only once each.

## Counting Results

To count the number of rows:

```sql
SELECT COUNT(*) FROM students;
```

To count rows that match a condition:

```sql
SELECT COUNT(*) FROM students WHERE grade = 12;
```

## Combining WHERE Conditions

You can combine multiple conditions using AND and OR:

```sql
SELECT * FROM students WHERE grade = 12 AND age >= 18;
```

This returns students who are both in grade 12 AND at least 18 years old.

```sql
SELECT * FROM students WHERE grade = 12 OR grade = 11;
```

This returns students who are in either grade 11 OR grade 12.

## Retrieving Data from Multiple Tables

We'll cover joins in detail later, but here's a simple example:

```sql
SELECT 
    students.name AS student_name,
    courses.name AS course_name
FROM 
    students, 
    courses, 
    enrollments
WHERE 
    enrollments.student_id = students.id 
    AND enrollments.course_id = courses.id;
```

This returns a list of students and the courses they're enrolled in.

## Practice Exercises

1. Retrieve all students in grade 11
2. Count how many students are in each grade
3. Find the average age of students in grade 12
4. List all courses with their teachers
5. Find all students enrolled in Mathematics

## Next Steps

Now that you know how to retrieve data, in the next section we'll explore more advanced filtering techniques.
