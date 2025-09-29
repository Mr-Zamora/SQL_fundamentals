# 7. Ordering and Limiting Results

When retrieving data from a database, you often want to control both the order of results and how many results are returned. In this tutorial, we'll learn how to sort query results and limit their number.

## Part 1: Ordering Results

The ORDER BY clause allows you to sort your query results based on one or more columns.

### Basic ORDER BY Syntax

The basic syntax for ordering results is:

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column_name [ASC|DESC];
```

Where:
- `column_name` is the column to sort by
- `ASC` means ascending order (default if not specified)
- `DESC` means descending order

### Sorting in Ascending Order

To sort students by name in alphabetical order:

```sql
SELECT * FROM students ORDER BY name;
```

or explicitly:

```sql
SELECT * FROM students ORDER BY name ASC;
```

#### Running this in SQLite CLI:

```
sqlite> SELECT * FROM students ORDER BY name;
id  name           age  grade
--  -------------  ---  -----
5   David Lee      NULL 11
4   Emma Brown     16   11
1   John Smith     17   12
3   Michael Wong   17   12
2   Sarah Johnson  18   12
```

#### Running this in Python:

```python
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM students ORDER BY name")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
```

### Sorting in Descending Order

To sort students by age from oldest to youngest:

```sql
SELECT * FROM students ORDER BY age DESC;
```

This will place the oldest students first, followed by younger students.

### Sorting by Multiple Columns

You can sort by multiple columns, which is useful when the first column has duplicate values:

```sql
SELECT * FROM students ORDER BY grade, name;
```

This will sort students first by their grade, and then by name within each grade.

You can mix ascending and descending orders:

```sql
SELECT * FROM students ORDER BY grade DESC, name ASC;
```

This sorts by grade in descending order (12, 11, ...) and then by name in ascending order within each grade.

### NULL Values in Sorting

By default, NULL values appear first in ascending order and last in descending order:

```sql
-- NULL values will appear first
SELECT * FROM students ORDER BY age ASC;

-- NULL values will appear last
SELECT * FROM students ORDER BY age DESC;
```

## Part 2: Limiting Results

When working with large datasets, you often don't need to retrieve all rows at once. The LIMIT clause allows you to restrict the number of rows returned by a query.

### Basic LIMIT Syntax

The basic syntax for limiting results is:

```sql
SELECT column1, column2, ...
FROM table_name
LIMIT number_of_rows;
```

Where `number_of_rows` is the maximum number of rows to return.

### Simple LIMIT Example

To retrieve only the first 3 students:

```sql
SELECT * FROM students LIMIT 3;
```

This will return at most 3 rows, regardless of how many students are in the table.

#### Running this in SQLite CLI:

```
sqlite> SELECT * FROM students LIMIT 3;
id  name           age  grade
--  -------------  ---  -----
1   John Smith     17   12
2   Sarah Johnson  18   12
3   Michael Wong   17   12
```

### LIMIT with OFFSET

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

### Combining ORDER BY and LIMIT

ORDER BY and LIMIT are often used together to get the "top N" or "bottom N" rows:

```sql
-- Get the 3 oldest students
SELECT * FROM students ORDER BY age DESC LIMIT 3;

-- Get the 3 youngest students (with known ages)
SELECT * FROM students 
WHERE age IS NOT NULL 
ORDER BY age ASC 
LIMIT 3;
```

### Practical Use Cases

#### Pagination

LIMIT and OFFSET are commonly used for pagination in applications:

```sql
-- Page 1 (rows 1-10)
SELECT * FROM students LIMIT 10 OFFSET 0;

-- Page 2 (rows 11-20)
SELECT * FROM students LIMIT 10 OFFSET 10;

-- Page 3 (rows 21-30)
SELECT * FROM students LIMIT 10 OFFSET 20;
```

#### Top N Records

Getting the top N records based on some criteria:

```sql
-- Top 3 students by age
SELECT * FROM students ORDER BY age DESC LIMIT 3;
```

#### Sample Data

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

1. List all students from youngest to oldest
2. List students by grade (highest first) and then by name (alphabetically)
3. Retrieve the 3 youngest students
4. Implement a pagination system that shows 5 students per page
5. Get the top 2 oldest students in each grade

## Next Steps

Now that you know how to order and limit your results, in the next section we'll learn how to update and delete records in the database.
