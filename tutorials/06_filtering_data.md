# 6. Filtering Data

Filtering data is essential for retrieving only the specific information you need. In this section, we'll explore various ways to filter data using the WHERE clause.

## Comparison Operators

SQLite supports the following comparison operators:

| Operator | Description              | Example                       |
|----------|--------------------------|-------------------------------|
| =        | Equal to                 | `WHERE age = 17`              |
| >        | Greater than             | `WHERE age > 16`              |
| <        | Less than                | `WHERE age < 18`              |
| >=       | Greater than or equal to | `WHERE age >= 17`             |
| <=       | Less than or equal to    | `WHERE age <= 18`             |
| !=       | Not equal to             | `WHERE grade != 11`           |
| <>       | Not equal to (alternate) | `WHERE grade <> 11`           |

## Basic WHERE Examples

```sql
-- Students who are 17 years old
SELECT * FROM students WHERE age = 17;

-- Students who are not in grade 11
SELECT * FROM students WHERE grade != 11;

-- Students who are 18 or older
SELECT * FROM students WHERE age >= 18;
```

## Filtering Text Data

When filtering text data, you need to use quotes:

```sql
-- Find a specific student by name
SELECT * FROM students WHERE name = 'John Smith';

-- Find courses taught by a specific teacher
SELECT * FROM courses WHERE teacher = 'Mr. Anderson';
```

## Using LIKE for Pattern Matching

The LIKE operator allows you to search for patterns in text:

```sql
-- Names that start with 'J'
SELECT * FROM students WHERE name LIKE 'J%';

-- Names that end with 'son'
SELECT * FROM students WHERE name LIKE '%son';

-- Names that contain 'oh'
SELECT * FROM students WHERE name LIKE '%oh%';
```

In these patterns:
- `%` represents any sequence of characters (including zero characters)
- `_` represents exactly one character

More examples:

```sql
-- Names with exactly 4 characters
SELECT * FROM students WHERE name LIKE '____';

-- Names that have 'o' as the second letter
SELECT * FROM students WHERE name LIKE '_o%';
```

## Case Sensitivity

By default, SQLite's LIKE operator is case-insensitive:

```sql
-- Both of these will match 'John Smith'
SELECT * FROM students WHERE name LIKE 'john%';
SELECT * FROM students WHERE name LIKE 'JOHN%';
```

If you need case-sensitive matching, use the GLOB operator instead of LIKE.

## Working with NULL Values

NULL represents missing or unknown data. To check for NULL values, use IS NULL or IS NOT NULL:

```sql
-- Students with no age recorded
SELECT * FROM students WHERE age IS NULL;

-- Students with an age recorded
SELECT * FROM students WHERE age IS NOT NULL;
```

Note: You cannot use `= NULL` or `!= NULL` as these won't work as expected.

## Combining Conditions with AND, OR, and NOT

### AND Operator

The AND operator returns rows that satisfy both conditions:

```sql
-- Students who are in grade 12 and are 18 years old
SELECT * FROM students WHERE grade = 12 AND age = 18;
```

### OR Operator

The OR operator returns rows that satisfy either condition:

```sql
-- Students who are either in grade 11 or grade 12
SELECT * FROM students WHERE grade = 11 OR grade = 12;
```

### NOT Operator

The NOT operator negates a condition:

```sql
-- Students who are not in grade 12
SELECT * FROM students WHERE NOT grade = 12;
-- Alternatively: SELECT * FROM students WHERE grade != 12;
```

### Complex Conditions

You can combine multiple conditions using parentheses:

```sql
-- Students who are in grade 12 and are either 17 or 18 years old
SELECT * FROM students 
WHERE grade = 12 AND (age = 17 OR age = 18);
```

## IN Operator

The IN operator checks if a value matches any value in a list:

```sql
-- Students in grades 11 or 12
SELECT * FROM students WHERE grade IN (11, 12);

-- Equivalent to: WHERE grade = 11 OR grade = 12
```

## BETWEEN Operator

The BETWEEN operator checks if a value is within a range:

```sql
-- Students between 16 and 18 years old (inclusive)
SELECT * FROM students WHERE age BETWEEN 16 AND 18;

-- Equivalent to: WHERE age >= 16 AND age <= 18
```

## Practice Exercises

1. Find all students whose names start with 'M'
2. Find all courses that have 'Room' in their room description
3. Find all students who are either 16 years old or in grade 11
4. Find all students who are in grade 12 but not 18 years old
5. Find all courses taught by teachers whose names contain 'son'

## Next Steps

Now that you know how to filter data, in the next section we'll learn how to sort and limit the results using ORDER BY and LIMIT.
