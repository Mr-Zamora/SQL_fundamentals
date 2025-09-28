# SQL Troubleshooting Guide

This guide covers common SQL errors and how to fix them. Use this as a reference when you or your students encounter issues with SQL queries.

## Syntax Errors

### 1. Missing Semicolons

**Error**: `near "SELECT": syntax error`

**Problem**: SQL statements should end with a semicolon (;)

**Fix**:
```sql
-- Incorrect
SELECT * FROM students
SELECT * FROM courses

-- Correct
SELECT * FROM students;
SELECT * FROM courses;
```

### 2. Incorrect Quotes

**Error**: `unrecognized token: "'"`

**Problem**: Using incorrect quote types (SQLite uses single quotes for text values)

**Fix**:
```sql
-- Incorrect
SELECT * FROM students WHERE name = "John";

-- Correct
SELECT * FROM students WHERE name = 'John';
```

### 3. Reserved Keywords as Identifiers

**Error**: `near "ORDER": syntax error`

**Problem**: Using SQL reserved keywords as table or column names without proper quoting

**Fix**:
```sql
-- Incorrect
CREATE TABLE order (id INTEGER, date TEXT);

-- Correct
CREATE TABLE "order" (id INTEGER, date TEXT);
-- Or better yet, rename to avoid keywords
CREATE TABLE orders (id INTEGER, date TEXT);
```

## Table and Column Errors

### 4. Table Doesn't Exist

**Error**: `no such table: students`

**Problem**: Referencing a table that doesn't exist

**Fix**:
- Check if the table exists: `.tables`
- Check for typos in the table name
- Create the table if needed

### 5. Column Doesn't Exist

**Error**: `no such column: student_name`

**Problem**: Referencing a column that doesn't exist

**Fix**:
- Check the table schema: `.schema table_name`
- Use the correct column name
- Add the column if needed: `ALTER TABLE table_name ADD COLUMN column_name data_type;`

### 6. Ambiguous Column Name

**Error**: `ambiguous column name: name`

**Problem**: Multiple tables in a join have columns with the same name

**Fix**:
```sql
-- Incorrect
SELECT name FROM students JOIN teachers;

-- Correct
SELECT students.name FROM students JOIN teachers;
-- Or use aliases
SELECT s.name FROM students s JOIN teachers t;
```

## Constraint Violations

### 7. PRIMARY KEY Constraint Failed

**Error**: `UNIQUE constraint failed: table.column`

**Problem**: Trying to insert a duplicate value into a PRIMARY KEY or UNIQUE column

**Fix**:
- Use a different value
- Use `INSERT OR REPLACE` if you want to overwrite
- Use `INSERT OR IGNORE` if you want to skip duplicates

### 8. NOT NULL Constraint Failed

**Error**: `NOT NULL constraint failed: table.column`

**Problem**: Trying to insert NULL into a column that doesn't allow NULL values

**Fix**:
- Provide a value for the column
- Make the column nullable if appropriate

### 9. FOREIGN KEY Constraint Failed

**Error**: `FOREIGN KEY constraint failed`

**Problem**: Referencing a value that doesn't exist in the parent table

**Fix**:
- Make sure the referenced value exists in the parent table
- Add the referenced value to the parent table first
- Use `ON DELETE CASCADE` if appropriate

## Data Type Issues

### 10. Data Type Mismatch

**Error**: `datatype mismatch`

**Problem**: Trying to insert data of the wrong type

**Fix**:
```sql
-- Incorrect
INSERT INTO students (age) VALUES ('twenty');

-- Correct
INSERT INTO students (age) VALUES (20);
```

### 11. Invalid Date Format

**Error**: `Error: near "date": syntax error`

**Problem**: Using incorrect date format

**Fix**:
```sql
-- Incorrect
INSERT INTO events (event_date) VALUES (2023-09-15);

-- Correct (SQLite stores dates as TEXT, ISO format recommended)
INSERT INTO events (event_date) VALUES ('2023-09-15');
```

## Query Logic Errors

### 12. Incorrect WHERE Clause

**Problem**: Query returns unexpected results due to logical errors in the WHERE clause

**Fix**:
- Check your logical operators (AND, OR)
- Check your comparison operators (=, <, >, etc.)
- Use parentheses to clarify order of operations

```sql
-- Might not do what you expect
SELECT * FROM students WHERE grade = 11 OR grade = 12 AND age > 17;

-- Clearer with parentheses
SELECT * FROM students WHERE (grade = 11 OR grade = 12) AND age > 17;
```

### 13. Incorrect JOIN Condition

**Problem**: JOIN returns unexpected results

**Fix**:
- Verify the join condition is correct
- Check that you're using the right type of join (INNER, LEFT, etc.)
- Make sure the columns you're joining on have matching data types

### 14. GROUP BY Issues

**Error**: `misuse of aggregate function`

**Problem**: Using columns in SELECT that aren't in GROUP BY

**Fix**:
```sql
-- Incorrect
SELECT name, grade, COUNT(*) FROM students GROUP BY grade;

-- Correct
SELECT grade, COUNT(*) FROM students GROUP BY grade;
-- Or
SELECT name, grade, COUNT(*) FROM students GROUP BY grade, name;
```

## Performance Issues

### 15. Slow Queries

**Problem**: Queries take too long to execute

**Fix**:
- Add appropriate indexes: `CREATE INDEX idx_name ON table(column);`
- Avoid using functions in WHERE clauses
- Limit the amount of data returned
- Use more specific conditions in WHERE clauses

### 16. Inefficient JOINs

**Problem**: Joins perform poorly

**Fix**:
- Ensure joined columns are indexed
- Join on the smallest necessary tables first
- Use subqueries or temporary tables for complex joins

## Common Logical Errors

### 17. Using = with NULL

**Problem**: Conditions with NULL don't work as expected

**Fix**:
```sql
-- Incorrect (will not find rows where age is NULL)
SELECT * FROM students WHERE age = NULL;

-- Correct
SELECT * FROM students WHERE age IS NULL;
```

### 18. Forgetting WHERE in UPDATE/DELETE

**Problem**: Accidentally updating or deleting all rows

**Fix**:
```sql
-- Dangerous (updates ALL rows)
UPDATE students SET grade = 12;

-- Safe (updates only specific rows)
UPDATE students SET grade = 12 WHERE id = 5;
```

### 19. Incorrect Aggregation

**Problem**: Getting unexpected results from aggregate functions

**Fix**:
- Remember that aggregate functions ignore NULL values
- Use GROUP BY appropriately
- Consider using COALESCE() for NULL values

## SQLite-Specific Issues

### 20. Foreign Keys Not Enforced

**Problem**: Foreign key constraints aren't being enforced

**Fix**:
- Enable foreign key support: `PRAGMA foreign_keys = ON;`
- Run this command each time you connect to the database

### 21. Case Sensitivity in LIKE

**Problem**: LIKE pattern matching is case-insensitive by default in SQLite

**Fix**:
- Use GLOB for case-sensitive matching
- Or use the LIKE operator with the BINARY keyword in some systems

### 22. Transaction Issues

**Problem**: Changes not being saved

**Fix**:
- Make sure to COMMIT your transactions
- Check for implicit transactions
- Verify you're not rolling back accidentally

## Debugging Techniques

### 1. Check Table Structure

```sql
.schema table_name
```

### 2. Examine Data

```sql
SELECT * FROM table_name LIMIT 10;
```

### 3. Test Simpler Queries First

Break down complex queries into simpler parts and test each part separately.

### 4. Use EXPLAIN to Analyze Query Execution

```sql
EXPLAIN QUERY PLAN SELECT * FROM students WHERE grade = 12;
```

### 5. Enable Verbose Error Messages

```sql
.bail on
.echo on
```

## Common Error Prevention Tips

1. **Back Up Your Data**: Always back up your database before making significant changes
2. **Use Transactions**: Wrap multiple related operations in transactions
3. **Test Queries**: Test SELECT queries before running UPDATE or DELETE
4. **Use Descriptive Names**: Choose clear, descriptive names for tables and columns
5. **Comment Your Code**: Add comments to explain complex queries
6. **Format Your SQL**: Use consistent formatting to make queries readable
7. **Validate Input**: Always validate and sanitize user input before using it in queries
