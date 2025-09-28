# 4. Inserting Data

Now that we've created tables, let's learn how to add data to them.

## INSERT INTO Syntax

The basic syntax for inserting data is:

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

Where:
- `table_name` is the table you want to add data to
- The columns in parentheses specify which columns you're providing values for
- The `VALUES` clause contains the actual data to insert

## Inserting a Single Row

Let's add a student to our "students" table:

```sql
INSERT INTO students (name, age, grade)
VALUES ('John Smith', 17, 12);
```

Notice:
- We didn't specify the `id` column because it's an auto-incrementing primary key
- Text values are enclosed in single quotes
- Numeric values don't need quotes
- The order of values must match the order of columns

### Running this in SQLite CLI:

```
sqlite> INSERT INTO students (name, age, grade)
   ...> VALUES ('John Smith', 17, 12);
```

### Running this in Python:

```python
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''
INSERT INTO students (name, age, grade)
VALUES ('John Smith', 17, 12)
''')

conn.commit()  # Don't forget to commit the transaction!
conn.close()
```

## Inserting Multiple Rows

You can insert multiple rows in a single statement:

```sql
INSERT INTO students (name, age, grade)
VALUES 
    ('Sarah Johnson', 18, 12),
    ('Michael Wong', 17, 12),
    ('Emma Brown', 16, 11);
```

This is more efficient than executing multiple separate INSERT statements.

## Inserting Data with All Columns

If you're providing values for all columns in the table, you can omit the column list:

```sql
INSERT INTO courses
VALUES (1, 'Mathematics', 'Mr. Anderson', 'Room 101');
```

However, it's generally better practice to explicitly list the columns for clarity and to avoid errors if the table structure changes.

## Inserting with Default and NULL Values

If a column has a default value or allows NULL, you can omit it from your INSERT:

```sql
INSERT INTO students (name, grade)
VALUES ('David Lee', 11);
```

In this example, the `age` column will be NULL since we didn't provide a value.

## Inserting Data into Related Tables

Let's add some courses and enrollments:

```sql
-- Add courses
INSERT INTO courses (name, teacher, room)
VALUES 
    ('Mathematics', 'Mr. Anderson', 'Room 101'),
    ('English Literature', 'Ms. Davis', 'Room 203'),
    ('Computer Science', 'Mrs. Wilson', 'Lab 3');

-- Add enrollments (connecting students to courses)
INSERT INTO enrollments (student_id, course_id, enrollment_date)
VALUES 
    (1, 1, '2023-09-01'),  -- John Smith in Mathematics
    (1, 3, '2023-09-01'),  -- John Smith in Computer Science
    (2, 1, '2023-09-01'),  -- Sarah Johnson in Mathematics
    (2, 2, '2023-09-01');  -- Sarah Johnson in English Literature
```

## Inserting Data from Another Table

You can insert data based on a SELECT statement:

```sql
INSERT INTO seniors (student_id, name, age)
SELECT id, name, age FROM students WHERE grade = 12;
```

This would copy all grade 12 students into a "seniors" table.

## Checking Your Inserted Data

After inserting data, you can verify it was added correctly:

```sql
SELECT * FROM students;
```

We'll cover SELECT statements in detail in the next section.

## Practice Exercise

1. Insert at least 5 more students into the students table
2. Insert 3 more courses into the courses table
3. Create enrollment records to connect students with courses

## Common Errors When Inserting Data

1. **Violating NOT NULL constraint**: Trying to insert NULL into a column that doesn't allow it
2. **Violating UNIQUE constraint**: Trying to insert a duplicate value in a column that must be unique
3. **Foreign key constraint failure**: Referencing an ID that doesn't exist in the parent table
4. **Data type mismatch**: Trying to insert text into a numeric column or vice versa

## Next Steps

Now that you've added data to your tables, in the next section we'll learn how to retrieve and view that data using SELECT statements.
