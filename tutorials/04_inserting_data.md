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
INSERT INTO teachers
VALUES (1, 'Mr. Anderson', 'Mathematics', 'anderson@school.edu');
```

However, it's generally better practice to explicitly list the columns for clarity and to avoid errors if the table structure changes.

## Inserting with Default and NULL Values

If a column has a default value or allows NULL, you can omit it from your INSERT:

```sql
INSERT INTO students (name, grade)
VALUES ('David Lee', 11);
```

In this example, the `age` column will be NULL since we didn't provide a value.

## Using DEFAULT Keyword

You can explicitly use the DEFAULT keyword to use a column's default value:

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    in_stock INTEGER DEFAULT 0,
    date_added TEXT DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (name, price, in_stock)
VALUES ('Laptop', 999.99, DEFAULT);
```

This will use the default value of 0 for the in_stock column.

## Handling Dates

SQLite doesn't have a dedicated date type, but you can store dates as TEXT, INTEGER, or REAL:

```sql
-- Storing as TEXT (ISO8601 format: YYYY-MM-DD)
INSERT INTO students (name, age, grade, enrollment_date)
VALUES ('Lisa Chen', 16, 11, '2023-09-01');

-- Using SQLite date functions
INSERT INTO students (name, age, grade, enrollment_date)
VALUES ('James Wilson', 17, 12, date('now'));
```

## Inserting Data from Another Table

You can insert data based on a SELECT statement:

```sql
-- First create a seniors table
CREATE TABLE seniors (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);

-- Then copy data from students table
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
2. Create a "courses" table with columns for id, name, credits, and department
3. Insert at least 3 courses into your new courses table
4. Create a "teachers" table and insert at least 3 teachers

## Common Errors When Inserting Data

1. **Violating NOT NULL constraint**: Trying to insert NULL into a column that doesn't allow it
2. **Violating UNIQUE constraint**: Trying to insert a duplicate value in a column that must be unique
3. **Data type mismatch**: Trying to insert text into a numeric column or vice versa
4. **Constraint violation**: Inserting data that doesn't meet CHECK constraints

## Reference: Example Data

Here's a summary of all the example data we've inserted in this tutorial. You can refer back to this when working through later tutorials:

### Students Table

```
id | name           | age  | grade
---+----------------+------+-------
1  | John Smith     | 17   | 12
2  | Sarah Johnson  | 18   | 12
3  | Michael Wong   | 17   | 12
4  | Emma Brown     | 16   | 11
5  | David Lee      | NULL | 11
```

### Teachers Table

```
id | name         | subject          | email
---+--------------+-----------------+--------------------
1  | Mr. Anderson | Mathematics     | anderson@school.edu
```

### Products Table (Example for DEFAULT values)

```
id | name    | price  | in_stock | date_added
---+---------+--------+----------+----------------
1  | Laptop  | 999.99 | 0        | [current_timestamp]
```

### Seniors Table (Example for INSERT with SELECT)

```
student_id | name           | age
-----------+----------------+-----
1          | John Smith     | 17
2          | Sarah Johnson  | 18
3          | Michael Wong   | 17
```

Note: The actual data in your database may vary depending on which examples and practice exercises you've completed.

## Next Steps

Now that you've added data to your tables, in the next section we'll learn how to retrieve and view that data using SELECT statements.
