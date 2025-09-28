# 8. Limiting Results

When working with large datasets, you often don't need to retrieve all rows at once. The LIMIT clause allows you to restrict the number of rows returned by a query, which can improve performance and make results more manageable.

## Basic LIMIT Syntax

The basic syntax for limiting results is:

```sql
SELECT column1, column2, ...
FROM table_name
LIMIT number_of_rows;
```

Where `number_of_rows` is the maximum number of rows to return.

## Simple LIMIT Example

To retrieve only the first 3 students:

```sql
SELECT * FROM students LIMIT 3;
```

This will return at most 3 rows, regardless of how many students are in the table.

### Running this in SQLite CLI:

```
sqlite> SELECT * FROM students LIMIT 3;
id  name           age  grade
--  -------------  ---  -----
1   John Smith     17   12
2   Sarah Johnson  18   12
3   Michael Wong   17   12
```

### Running this in Python:

```python
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM students LIMIT 3")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
```

## LIMIT with OFFSET

The OFFSET clause lets you skip a certain number of rows before starting to return results:

```sql
SELECT column1, column2, ...
FROM table_name
LIMIT number_of_rows OFFSET start_position;
```

For example, to get the 4th and 5th students:

```sql
SELECT * FROM students LIMIT 2 OFFSET 3;
```

This skips the first 3 rows and then returns the next 2 rows.

## Alternative Syntax

SQLite also supports an alternative syntax for LIMIT with OFFSET:

```sql
SELECT * FROM students LIMIT 3, 2;
```

In this format, the first number is the OFFSET and the second is the LIMIT. This is equivalent to `LIMIT 2 OFFSET 3`.

However, the `LIMIT x OFFSET y` syntax is clearer and less prone to confusion.

## Combining LIMIT with ORDER BY

LIMIT is often used with ORDER BY to get the "top N" or "bottom N" rows:

```sql
-- Get the 3 oldest students
SELECT * FROM students ORDER BY age DESC LIMIT 3;

-- Get the 3 youngest students (with known ages)
SELECT * FROM students 
WHERE age IS NOT NULL 
ORDER BY age ASC 
LIMIT 3;
```

## Practical Use Cases

### Pagination

LIMIT and OFFSET are commonly used for pagination in applications:

```sql
-- Page 1 (rows 1-10)
SELECT * FROM students LIMIT 10 OFFSET 0;

-- Page 2 (rows 11-20)
SELECT * FROM students LIMIT 10 OFFSET 10;

-- Page 3 (rows 21-30)
SELECT * FROM students LIMIT 10 OFFSET 20;
```

### Top N Records

Getting the top N records based on some criteria:

```sql
-- Top 3 students by age
SELECT * FROM students ORDER BY age DESC LIMIT 3;
```

### Sample Data

Getting a sample of data:

```sql
-- Random sample of 5 students
SELECT * FROM students ORDER BY RANDOM() LIMIT 5;
```

## Performance Considerations

Using LIMIT can significantly improve performance when working with large tables:

- The database can stop processing once it has found the requested number of rows
- Less data needs to be transferred from the database to your application
- Less memory is required to store the results

## Practice Exercises

1. Retrieve the 2 youngest students
2. Get the 3 most recently enrolled students
3. List the first 5 courses alphabetically
4. Implement a pagination system that shows 3 students per page
5. Get a random sample of 2 courses

## Next Steps

Now that you know how to limit your results, in the next section we'll learn how to update existing records in the database.
