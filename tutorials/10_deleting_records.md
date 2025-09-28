# 10. Deleting Records

Sometimes you need to remove data from your database. The DELETE statement allows you to remove records from a table.

## Basic DELETE Syntax

The basic syntax for deleting records is:

```sql
DELETE FROM table_name
WHERE condition;
```

Where:
- `table_name` is the table containing the records you want to delete
- The WHERE clause determines which rows will be deleted

## IMPORTANT: Always Use WHERE with DELETE

If you omit the WHERE clause, the DELETE will remove ALL rows from the table! This is rarely what you want and can lead to significant data loss.

```sql
-- DON'T DO THIS unless you really want to delete all records
DELETE FROM students;
```

## Simple DELETE Example

To delete a single student:

```sql
DELETE FROM students
WHERE id = 5;
```

This removes the student with id = 5 from the table.

### Running this in SQLite CLI:

```
sqlite> DELETE FROM students WHERE id = 5;
sqlite> SELECT * FROM students WHERE id = 5;
-- No results returned
```

### Running this in Python:

```python
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM students WHERE id = 5")

# Always commit changes for DELETE, UPDATE, and INSERT
conn.commit()

# Verify the deletion
cursor.execute("SELECT * FROM students WHERE id = 5")
print("Rows found:", len(cursor.fetchall()))

conn.close()
```

## Deleting Multiple Records

You can delete multiple records that match a condition:

```sql
-- Delete all students in grade 11
DELETE FROM students
WHERE grade = 11;
```

## Deleting Related Records

When working with related tables, you might need to delete records from multiple tables:

```sql
-- First, delete enrollments for a student
DELETE FROM enrollments
WHERE student_id = 3;

-- Then, delete the student
DELETE FROM students
WHERE id = 3;
```

Some database systems support CASCADE DELETE, which automatically deletes related records, but SQLite requires you to handle this manually unless you've set up foreign key constraints with CASCADE.

## Deleting with Subqueries

You can use subqueries in your DELETE statements:

```sql
-- Delete all enrollments for Computer Science
DELETE FROM enrollments
WHERE course_id IN (
    SELECT id FROM courses WHERE name = 'Computer Science'
);
```

## Safe DELETE Practices

### 1. Always test your WHERE clause first

Before running a DELETE, test your WHERE clause with a SELECT to make sure it targets the right rows:

```sql
-- First, check which rows will be affected
SELECT * FROM students WHERE grade = 11;

-- If the results look correct, then run the delete
DELETE FROM students WHERE grade = 11;
```

### 2. Use transactions for safety

Transactions let you roll back changes if something goes wrong:

```sql
BEGIN TRANSACTION;

DELETE FROM students WHERE grade = 11;

-- Check if the deletion looks correct
SELECT * FROM students WHERE grade = 11;

-- If everything looks good
COMMIT;

-- If something went wrong
-- ROLLBACK;
```

### 3. Consider soft deletes

Instead of actually deleting records, consider adding an "is_deleted" or "status" column:

```sql
-- Instead of DELETE FROM students WHERE id = 5;
UPDATE students
SET status = 'inactive'
WHERE id = 5;
```

This preserves the data for historical purposes while removing it from active use.

## Truncating Tables

If you do want to delete all records from a table (but keep the table structure), you can use:

```sql
DELETE FROM table_name;
```

Or more efficiently:

```sql
-- This is faster for large tables
DROP TABLE table_name;
CREATE TABLE table_name (...);
```

## Common DELETE Scenarios

### Deleting duplicate records

```sql
-- Delete duplicate enrollments (keeping the one with the lowest id)
DELETE FROM enrollments
WHERE id NOT IN (
    SELECT MIN(id)
    FROM enrollments
    GROUP BY student_id, course_id
);
```

### Deleting orphaned records

```sql
-- Delete enrollments for courses that no longer exist
DELETE FROM enrollments
WHERE course_id NOT IN (SELECT id FROM courses);
```

### Deleting old records

```sql
-- Delete enrollments from previous years
DELETE FROM enrollments
WHERE enrollment_date < '2023-01-01';
```

## Practice Exercises

1. Delete a specific student by name
2. Delete all enrollments for a specific student
3. Delete all courses that have no students enrolled
4. Use a transaction to safely delete all students in grade 10
5. Delete the oldest enrollment for each student (if they have multiple)

## Next Steps

Now that you know how to delete records, in the next section we'll learn about database design basics, including primary keys and table relationships.
