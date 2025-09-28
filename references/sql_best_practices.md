# SQL Best Practices

This guide outlines best practices for writing clean, efficient, and maintainable SQL code. Following these guidelines will help you avoid common pitfalls and develop good habits as you learn SQL.

## Naming Conventions

### Table Names

- Use plural nouns for table names (e.g., `students`, `courses`, `enrollments`)
- Use lowercase with underscores for multi-word names (snake_case)
- Be descriptive but concise
- Avoid SQL reserved keywords as table names

```sql
-- Good
CREATE TABLE students (...);
CREATE TABLE course_enrollments (...);

-- Avoid
CREATE TABLE student (...);  -- Singular
CREATE TABLE tbl1 (...);     -- Not descriptive
CREATE TABLE "order" (...);  -- Reserved keyword (use orders instead)
```

### Column Names

- Use singular nouns for column names
- Use lowercase with underscores for multi-word names
- Use `id` for primary key columns
- Use `table_name_id` for foreign key columns
- Be consistent with naming patterns

```sql
-- Good
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    date_of_birth DATE
);

CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date DATE
);

-- Avoid
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,  -- Redundant prefix
    firstName TEXT,                  -- Inconsistent casing
    LastName TEXT,                   -- Inconsistent casing
    DOB DATE                         -- Unclear abbreviation
);
```

## Database Design

### Normalization

- Normalize your database to at least 3NF for most applications
- Each table should represent one entity or concept
- Avoid storing redundant data
- Use foreign keys to establish relationships between tables

### Primary Keys

- Every table should have a primary key
- Consider using surrogate keys (auto-incrementing integers) for simplicity
- Use natural keys only when they are truly unique and unlikely to change

### Foreign Keys

- Always define foreign key constraints to maintain referential integrity
- Consider what happens on UPDATE/DELETE (CASCADE, SET NULL, RESTRICT)
- Index foreign key columns for better join performance

```sql
CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses (id) ON DELETE RESTRICT
);
```

### Indexes

- Index columns that are frequently used in WHERE clauses, JOIN conditions, or ORDER BY
- Don't over-index - each index adds overhead to write operations
- Consider composite indexes for queries that filter on multiple columns
- Remove indexes that aren't being used

```sql
-- Index for frequently filtered column
CREATE INDEX idx_students_grade ON students (grade);

-- Composite index for columns often used together
CREATE INDEX idx_enrollments_student_course ON enrollments (student_id, course_id);
```

## Writing Queries

### Readability

- Use consistent indentation and formatting
- Capitalize SQL keywords for clarity (optional but common)
- Use meaningful aliases for tables
- Break long queries into multiple lines
- Add comments for complex logic

```sql
-- Good: Formatted for readability
SELECT 
    s.name AS student_name,
    c.name AS course_name,
    e.enrollment_date
FROM 
    students s
JOIN 
    enrollments e ON s.id = e.student_id
JOIN 
    courses c ON e.course_id = c.id
WHERE 
    s.grade = 12
    AND e.enrollment_date > '2023-01-01'
ORDER BY 
    s.name, c.name;

-- Avoid: Hard to read
SELECT s.name AS student_name, c.name AS course_name, e.enrollment_date FROM students s JOIN enrollments e ON s.id = e.student_id JOIN courses c ON e.course_id = c.id WHERE s.grade = 12 AND e.enrollment_date > '2023-01-01' ORDER BY s.name, c.name;
```

### Table Aliases

- Use meaningful aliases for tables (not just a, b, c)
- For single-letter aliases, use the first letter of the table name
- Be consistent with your aliasing style throughout a project

```sql
-- Good
SELECT 
    s.name,
    c.name AS course_name
FROM 
    students s
JOIN 
    courses c ON s.course_id = c.id;

-- Avoid
SELECT 
    a.name,
    b.name AS course_name
FROM 
    students a
JOIN 
    courses b ON a.course_id = b.id;
```

### SELECT Statements

- Specify only the columns you need, avoid `SELECT *` in production code
- Give columns with calculations or functions clear aliases
- Use table aliases to qualify column names when joining tables

```sql
-- Good
SELECT 
    student_id,
    AVG(score) AS average_score
FROM 
    grades
GROUP BY 
    student_id;

-- Avoid
SELECT * FROM grades;  -- Returns all columns
```

### WHERE Clauses

- Put the most selective conditions first (though the optimizer may reorder them)
- Use appropriate operators for the data type
- Be careful with NULL values (use IS NULL or IS NOT NULL)
- Use parentheses to clarify complex conditions

```sql
-- Good
WHERE 
    (grade = 12 OR grade = 11)
    AND age >= 16
    AND name IS NOT NULL;

-- Avoid
WHERE 
    name IS NOT NULL
    AND age >= 16
    AND grade = 12 OR grade = 11;  -- Ambiguous precedence
```

### JOINs

- Specify the type of join explicitly (INNER, LEFT, etc.)
- Use the USING clause when join columns have the same name
- Consider performance implications of different join types
- Join only the tables you need

```sql
-- Good
SELECT 
    s.name,
    c.name AS course_name
FROM 
    students s
LEFT JOIN 
    enrollments e ON s.id = e.student_id
LEFT JOIN 
    courses c ON e.course_id = c.id;

-- Alternative with USING when column names match
SELECT 
    s.name,
    c.name AS course_name
FROM 
    students s
LEFT JOIN 
    enrollments e USING (student_id)
LEFT JOIN 
    courses c USING (course_id);
```

### Subqueries

- Consider if a JOIN would be more efficient
- Use meaningful aliases for subquery results
- Format subqueries with clear indentation
- Consider using CTEs for complex subqueries

```sql
-- Using a subquery
SELECT 
    name,
    (SELECT COUNT(*) FROM enrollments WHERE student_id = s.id) AS course_count
FROM 
    students s;

-- Alternative using JOIN and GROUP BY
SELECT 
    s.name,
    COUNT(e.id) AS course_count
FROM 
    students s
LEFT JOIN 
    enrollments e ON s.id = e.student_id
GROUP BY 
    s.id, s.name;
```

### Common Table Expressions (CTEs)

- Use CTEs to break down complex queries into simpler parts
- Give CTEs meaningful names that describe what they represent
- Consider using recursive CTEs for hierarchical data

```sql
WITH student_course_counts AS (
    SELECT 
        student_id,
        COUNT(*) AS course_count
    FROM 
        enrollments
    GROUP BY 
        student_id
)
SELECT 
    s.name,
    COALESCE(scc.course_count, 0) AS course_count
FROM 
    students s
LEFT JOIN 
    student_course_counts scc ON s.id = scc.student_id
ORDER BY 
    course_count DESC;
```

## Performance Optimization

### General Tips

- Return only the data you need (limit columns and rows)
- Use appropriate indexes
- Avoid functions on indexed columns in WHERE clauses
- Consider the execution plan for complex queries
- Test performance with realistic data volumes

### Filtering Efficiently

- Filter data as early as possible in the query
- Use appropriate data types for comparisons
- Consider using EXISTS instead of IN for subqueries with large result sets
- Use BETWEEN for range queries on indexed columns

```sql
-- Less efficient
SELECT 
    *
FROM 
    students
WHERE 
    UPPER(name) = 'JOHN SMITH';  -- Function on indexed column

-- More efficient
SELECT 
    *
FROM 
    students
WHERE 
    name = 'John Smith';  -- Direct comparison
```

### Limiting Results

- Use LIMIT to restrict the number of rows returned
- Use pagination for large result sets
- Consider using window functions for top-N queries

```sql
-- Get the top 10 students by GPA
SELECT 
    name,
    gpa
FROM 
    students
ORDER BY 
    gpa DESC
LIMIT 10;
```

## Data Integrity and Security

### Transactions

- Use transactions for operations that must succeed or fail as a unit
- Keep transactions as short as possible
- Be aware of isolation levels and their implications

```sql
BEGIN TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Check if both updates succeeded
COMMIT;  -- or ROLLBACK if there was an error
```

### Input Validation

- Validate and sanitize all input before using it in SQL
- Use parameterized queries or prepared statements to prevent SQL injection
- Never concatenate user input directly into SQL strings

```python
# Bad (vulnerable to SQL injection)
name = user_input
cursor.execute(f"SELECT * FROM students WHERE name = '{name}'")

# Good (using parameterized query)
cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
```

### Error Handling

- Implement appropriate error handling in your application
- Log SQL errors for debugging
- Provide user-friendly error messages without exposing database details

## Documentation

### Comments

- Add comments to explain complex queries or non-obvious logic
- Document the purpose of tables and columns in your schema
- Include examples for how to use complex stored procedures or functions

```sql
-- Calculate the average grade for each student
-- Only includes grades from the current semester
SELECT 
    student_id,
    AVG(score) AS average_score
FROM 
    grades
WHERE 
    semester_id = (SELECT id FROM semesters WHERE is_current = 1)
GROUP BY 
    student_id;
```

### Schema Documentation

- Maintain an up-to-date ERD (Entity Relationship Diagram)
- Document constraints, indexes, and triggers
- Include information about expected data volumes and growth

## Testing

### Test Queries

- Test queries with edge cases (empty tables, NULL values, etc.)
- Verify results with known test data
- Test performance with realistic data volumes

### Regression Testing

- Create a test suite for critical database operations
- Run tests after schema changes
- Compare query results before and after optimizations

## Version Control

### Schema Changes

- Script all schema changes for version control
- Use migration tools for complex schema updates
- Include rollback scripts for each change

### Query Version Control

- Store important queries in version control
- Document changes to queries
- Consider using a query library or repository

## SQLite-Specific Best Practices

### Enable Foreign Keys

- SQLite doesn't enforce foreign key constraints by default
- Enable them explicitly:

```sql
PRAGMA foreign_keys = ON;
```

### Use Appropriate Data Types

- SQLite has a dynamic type system, but still use appropriate types
- Use INTEGER for primary keys to enable auto-increment
- Use TEXT for dates and times (ISO format: YYYY-MM-DD HH:MM:SS)

### Handle Concurrency

- Be aware of SQLite's concurrency limitations
- Use appropriate locking modes for your application
- Consider using WAL (Write-Ahead Logging) mode for better concurrency:

```sql
PRAGMA journal_mode = WAL;
```

### Regular Maintenance

- Run VACUUM periodically to reclaim space and defragment the database
- Check for and fix integrity issues:

```sql
PRAGMA integrity_check;
```
