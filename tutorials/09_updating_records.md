# 9. Updating Records

After adding data to your database, you'll often need to modify it. The UPDATE statement allows you to change existing records in a table.

## Basic UPDATE Syntax

The basic syntax for updating records is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

Where:
- `table_name` is the table containing the records you want to update
- The SET clause specifies which columns to modify and their new values
- The WHERE clause determines which rows will be updated

## IMPORTANT: Always Use WHERE with UPDATE

If you omit the WHERE clause, the UPDATE will modify ALL rows in the table! This is rarely what you want and can lead to data loss.

```sql
-- DON'T DO THIS unless you really want to update all records
UPDATE students SET grade = 12;
```

## Simple UPDATE Example

To update a single student's grade:

```sql
UPDATE students
SET grade = 12
WHERE id = 5;
```

This changes the grade to 12 for the student with id = 5.

### Running this in SQLite CLI:

```
sqlite> UPDATE students SET grade = 12 WHERE id = 5;
sqlite> SELECT * FROM students WHERE id = 5;
id  name       age   grade
--  ---------  ----  -----
5   David Lee  NULL  12
```

### Running this in Python:

```python
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("UPDATE students SET grade = 12 WHERE id = 5")

# Always commit changes for UPDATE, DELETE, and INSERT
conn.commit()

# Verify the change
cursor.execute("SELECT * FROM students WHERE id = 5")
print(cursor.fetchone())

conn.close()
```

## Updating Multiple Columns

You can update multiple columns in a single statement:

```sql
UPDATE students
SET age = 17, grade = 12
WHERE name = 'David Lee';
```

## Updating Based on Calculations

You can update a column based on its current value:

```sql
-- Increment all grade 11 students to grade 12
UPDATE students
SET grade = grade + 1
WHERE grade = 11;

-- Give a 10% increase to all course fees
UPDATE courses
SET fee = fee * 1.1;
```

## Updating with Subqueries

You can use subqueries in your UPDATE statements:

```sql
-- Update the room for all Mathematics courses to match the Computer Science room
UPDATE courses
SET room = (SELECT room FROM courses WHERE name = 'Computer Science')
WHERE name = 'Mathematics';
```

## Safe UPDATE Practices

### 1. Always test your WHERE clause first

Before running an UPDATE, test your WHERE clause with a SELECT to make sure it targets the right rows:

```sql
-- First, check which rows will be affected
SELECT * FROM students WHERE grade = 11;

-- If the results look correct, then run the update
UPDATE students SET grade = 12 WHERE grade = 11;
```

### 2. Use transactions for safety

Transactions let you roll back changes if something goes wrong:

```sql
BEGIN TRANSACTION;

UPDATE students SET grade = grade + 1 WHERE grade < 12;

-- Check if the update looks correct
SELECT * FROM students;

-- If everything looks good
COMMIT;

-- If something went wrong
-- ROLLBACK;
```

### 3. Limit the scope of your updates

Be as specific as possible with your WHERE clause:

```sql
-- Good: very specific
UPDATE students SET age = 18 WHERE id = 3;

-- Less good: might affect more rows than intended
UPDATE students SET age = 18 WHERE name LIKE 'M%';
```

## Common UPDATE Scenarios

### Updating NULL values

```sql
-- Set missing ages to the average age
UPDATE students
SET age = (SELECT AVG(age) FROM students WHERE age IS NOT NULL)
WHERE age IS NULL;
```

### Updating based on joins

```sql
-- Update grades for all students enrolled in Computer Science
UPDATE students
SET grade = 12
WHERE id IN (
    SELECT student_id 
    FROM enrollments 
    JOIN courses ON enrollments.course_id = courses.id
    WHERE courses.name = 'Computer Science'
);
```

## Practice Exercises

1. Update the room for the English Literature course to 'Room 205'
2. Increase all students' ages by 1 (to simulate a new school year)
3. Update the teacher for all courses in Room 101 to 'Ms. Thompson'
4. Set all NULL ages to 16
5. Update the enrollment date for all Mathematics enrollments to '2023-09-05'

## Next Steps

Now that you know how to update existing records, in the next section we'll learn how to delete records from the database.
