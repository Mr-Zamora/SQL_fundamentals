# SQL Cheat Sheet

## Database Operations

### Create a new database
```sql
-- In SQLite, just connect to a new file
sqlite3 database_name.db
```

### List all tables
```sql
.tables
```

### Show table structure
```sql
.schema table_name
```

## Creating Tables

### Basic CREATE TABLE
```sql
CREATE TABLE table_name (
    column1_name data_type constraints,
    column2_name data_type constraints,
    ...
);
```

### Example: Create students table
```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade INTEGER
);
```

### Common Data Types
- `INTEGER`: Whole numbers
- `REAL`: Decimal numbers
- `TEXT`: Text strings
- `BLOB`: Binary data
- `NULL`: Missing data

### Common Constraints
- `PRIMARY KEY`: Unique identifier
- `NOT NULL`: Value cannot be NULL
- `UNIQUE`: All values must be different
- `DEFAULT value`: Default if no value provided
- `CHECK (condition)`: Must satisfy condition
- `FOREIGN KEY`: References another table

## Inserting Data

### Basic INSERT
```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

### Example: Insert a student
```sql
INSERT INTO students (name, age, grade)
VALUES ('John Smith', 17, 12);
```

### Insert multiple rows
```sql
INSERT INTO students (name, age, grade)
VALUES 
    ('Sarah Johnson', 18, 12),
    ('Michael Wong', 17, 12);
```

## Selecting Data

### Select all columns
```sql
SELECT * FROM table_name;
```

### Select specific columns
```sql
SELECT column1, column2 FROM table_name;
```

### Select with condition
```sql
SELECT * FROM table_name WHERE condition;
```

### Example: Select students in grade 12
```sql
SELECT * FROM students WHERE grade = 12;
```

## Filtering Data

### Comparison operators
- `=` Equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to
- `!=` or `<>` Not equal to

### Text pattern matching
```sql
SELECT * FROM table_name WHERE column LIKE pattern;
```

### Common LIKE patterns
- `%` Matches any sequence of characters
- `_` Matches any single character

### Examples
```sql
-- Names starting with 'J'
SELECT * FROM students WHERE name LIKE 'J%';

-- Names ending with 'son'
SELECT * FROM students WHERE name LIKE '%son';

-- Names containing 'oh'
SELECT * FROM students WHERE name LIKE '%oh%';
```

### Combining conditions
```sql
-- AND: Both conditions must be true
SELECT * FROM students WHERE grade = 12 AND age >= 18;

-- OR: Either condition can be true
SELECT * FROM students WHERE grade = 11 OR grade = 12;

-- NOT: Negates a condition
SELECT * FROM students WHERE NOT grade = 12;
```

### Working with NULL
```sql
-- Find NULL values
SELECT * FROM students WHERE age IS NULL;

-- Find non-NULL values
SELECT * FROM students WHERE age IS NOT NULL;
```

### IN operator
```sql
SELECT * FROM students WHERE grade IN (11, 12);
```

### BETWEEN operator
```sql
SELECT * FROM students WHERE age BETWEEN 16 AND 18;
```

## Ordering Results

### Basic ORDER BY
```sql
SELECT * FROM table_name ORDER BY column;
```

### Ascending/descending order
```sql
-- Ascending (default)
SELECT * FROM students ORDER BY name ASC;

-- Descending
SELECT * FROM students ORDER BY age DESC;
```

### Multiple columns
```sql
SELECT * FROM students ORDER BY grade, name;
```

## Limiting Results

### Basic LIMIT
```sql
SELECT * FROM table_name LIMIT number_of_rows;
```

### LIMIT with OFFSET
```sql
SELECT * FROM table_name LIMIT number_of_rows OFFSET start_position;
```

### Example: Pagination
```sql
-- Page 1 (rows 1-10)
SELECT * FROM students LIMIT 10 OFFSET 0;

-- Page 2 (rows 11-20)
SELECT * FROM students LIMIT 10 OFFSET 10;
```

## Updating Records

### Basic UPDATE
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

### Example: Update a student's grade
```sql
UPDATE students
SET grade = 12
WHERE id = 5;
```

## Deleting Records

### Basic DELETE
```sql
DELETE FROM table_name
WHERE condition;
```

### Example: Delete a student
```sql
DELETE FROM students
WHERE id = 5;
```

## Joins

### INNER JOIN
```sql
SELECT columns
FROM table1
INNER JOIN table2 ON table1.column = table2.column;
```

### LEFT JOIN
```sql
SELECT columns
FROM table1
LEFT JOIN table2 ON table1.column = table2.column;
```

### Example: Students and their courses
```sql
SELECT students.name, courses.name as course_name
FROM students
INNER JOIN enrollments ON students.id = enrollments.student_id
INNER JOIN courses ON enrollments.course_id = courses.id;
```

## Aggregate Functions

### Common aggregate functions
- `COUNT()`: Count rows
- `SUM()`: Sum values
- `AVG()`: Average of values
- `MIN()`: Minimum value
- `MAX()`: Maximum value

### Examples
```sql
-- Count all students
SELECT COUNT(*) FROM students;

-- Count students in grade 12
SELECT COUNT(*) FROM students WHERE grade = 12;

-- Average age of students
SELECT AVG(age) FROM students;
```

### GROUP BY
```sql
SELECT column, aggregate_function(column)
FROM table_name
GROUP BY column;
```

### Example: Count students in each grade
```sql
SELECT grade, COUNT(*) as student_count
FROM students
GROUP BY grade;
```

## Transactions

### Basic transaction
```sql
BEGIN TRANSACTION;
-- SQL statements
COMMIT;  -- Save changes
-- or
ROLLBACK;  -- Discard changes
```

## Indexes

### Create index
```sql
CREATE INDEX index_name ON table_name (column);
```

### Create unique index
```sql
CREATE UNIQUE INDEX index_name ON table_name (column);
```
