# 7. Ordering Results

When retrieving data from a database, you often want to control the order in which results are returned. The ORDER BY clause allows you to sort your query results based on one or more columns.

## Basic ORDER BY Syntax

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

## Sorting in Ascending Order

To sort students by name in alphabetical order:

```sql
SELECT * FROM students ORDER BY name;
```

or explicitly:

```sql
SELECT * FROM students ORDER BY name ASC;
```

### Running this in SQLite CLI:

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

### Running this in Python:

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

## Sorting in Descending Order

To sort students by age from oldest to youngest:

```sql
SELECT * FROM students ORDER BY age DESC;
```

This will place the oldest students first, followed by younger students.

## Sorting by Multiple Columns

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

## Sorting by Column Position

You can also refer to columns by their position in the SELECT list:

```sql
SELECT name, age, grade FROM students ORDER BY 3, 1;
```

This sorts by the 3rd column (grade) and then by the 1st column (name). However, using column names is generally clearer and less prone to errors.

## Sorting with Expressions

You can sort based on calculated values:

```sql
SELECT name, age, grade FROM students ORDER BY age + grade DESC;
```

This sorts by the sum of age and grade in descending order.

## NULL Values in Sorting

By default, NULL values appear first in ascending order and last in descending order:

```sql
-- NULL values will appear first
SELECT * FROM students ORDER BY age ASC;

-- NULL values will appear last
SELECT * FROM students ORDER BY age DESC;
```

## Practical Examples

### Finding the oldest student in each grade:

```sql
SELECT grade, MAX(age) as max_age
FROM students
GROUP BY grade
ORDER BY grade;
```

### Listing courses by teacher name:

```sql
SELECT * FROM courses ORDER BY teacher;
```

### Finding students enrolled in the most courses:

```sql
SELECT 
    students.name,
    COUNT(enrollments.id) as course_count
FROM 
    students
JOIN 
    enrollments ON students.id = enrollments.student_id
GROUP BY 
    students.id
ORDER BY 
    course_count DESC;
```

## Practice Exercises

1. List all students from youngest to oldest
2. List courses alphabetically by name
3. List students by grade (highest first) and then by name (alphabetically)
4. Find the youngest and oldest student in each grade
5. List teachers alphabetically along with the courses they teach

## Next Steps

Now that you know how to order your results, in the next section we'll learn how to limit the number of results returned using the LIMIT clause.
