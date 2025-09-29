# 8. Updating and Deleting Records

After adding data to your database, you'll often need to modify or remove it. In this tutorial, we'll learn how to update existing records and delete unwanted ones.

## Part 1: Updating Records

The UPDATE statement allows you to change existing records in a table.

### Basic UPDATE Syntax

The basic syntax for updating records is:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

Where:
- `table_name` is the table containing the records you want to update
- The SET clause specifies which columns to modify and their new values
- The WHERE clause determines which rows will be updated

### IMPORTANT: Always Use WHERE with UPDATE

If you omit the WHERE clause, the UPDATE will modify ALL rows in the table! This is rarely what you want and can lead to data loss.

```sql
-- DON'T DO THIS unless you really want to update all records
UPDATE students SET grade = 12;
```

### Simple UPDATE Example

To update a single student's grade:

```sql
UPDATE students
SET grade = 12
WHERE id = 5;
```

This changes the grade to 12 for the student with id = 5.

#### Running this in SQLite CLI:

```
sqlite> UPDATE students SET grade = 12 WHERE id = 5;
sqlite> SELECT * FROM students WHERE id = 5;
id  name       age   grade
--  ---------  ----  -----
5   David Lee  NULL  12
```

#### Running this in Python:

```python
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("UPDATE students SET grade = 12 WHERE id = 5")

# Always commit changes for UPDATE, DELETE, and INSERT
conn.commit()

# Verify the change
cursor.execute("SELECT * FROM students WHERE id = 5")
print(cursor.fetchone())

conn.close()
```

### Updating Multiple Columns

You can update multiple columns in a single statement:

```sql
UPDATE students
SET age = 17, grade = 12
WHERE name = 'David Lee';
```

### Updating Based on Calculations

You can update a column based on its current value:

```sql
-- Increment all grade 11 students to grade 12
UPDATE students
SET grade = grade + 1
WHERE grade = 11;

-- Give a 10% increase to all product prices
UPDATE products
SET price = price * 1.1;
```

### Safe UPDATE Practices

#### 1. Always test your WHERE clause first

Before running an UPDATE, test your WHERE clause with a SELECT to make sure it targets the right rows:

```sql
-- First, check which rows will be affected
SELECT * FROM students WHERE grade = 11;

-- If the results look correct, then run the update
UPDATE students SET grade = 12 WHERE grade = 11;
```

#### 2. Use transactions for safety

Transactions let you roll back changes if something goes wrong:

```sql
BEGIN TRANSACTION;

UPDATE students SET grade = grade + 1 WHERE grade < 12;

-- Check if the update looks correct
SELECT * FROM students;

-- If everything looks good
COMMIT;

-- If something went wrong
-- ROLLBACK;
```

#### 3. Limit the scope of your updates

Be as specific as possible with your WHERE clause:

```sql
-- Good: very specific
UPDATE students SET age = 18 WHERE id = 3;

-- Less good: might affect more rows than intended
UPDATE students SET age = 18 WHERE name LIKE 'M%';
```

### Common UPDATE Scenarios

#### Updating NULL values

```sql
-- Set missing ages to the average age
UPDATE students
SET age = (SELECT AVG(age) FROM students WHERE age IS NOT NULL)
WHERE age IS NULL;
```

## Part 2: Deleting Records

The DELETE statement allows you to remove records from a table.

### Basic DELETE Syntax

The basic syntax for deleting records is:

```sql
DELETE FROM table_name
WHERE condition;
```

Where:
- `table_name` is the table containing the records you want to delete
- The WHERE clause determines which rows will be deleted

### IMPORTANT: Always Use WHERE with DELETE

If you omit the WHERE clause, the DELETE will remove ALL rows from the table! This is rarely what you want and can lead to significant data loss.

```sql
-- DON'T DO THIS unless you really want to delete all records
DELETE FROM students;
```

### Simple DELETE Example

To delete a single student:

```sql
DELETE FROM students
WHERE id = 5;
```

This removes the student with id = 5 from the table.

#### Running this in SQLite CLI:

```
sqlite> DELETE FROM students WHERE id = 5;
sqlite> SELECT * FROM students WHERE id = 5;
-- No results returned
```

#### Running this in Python:

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

### Deleting Multiple Records

You can delete multiple records that match a condition:

```sql
-- Delete all students in grade 11
DELETE FROM students
WHERE grade = 11;
```

### Safe DELETE Practices

#### 1. Always test your WHERE clause first

Before running a DELETE, test your WHERE clause with a SELECT to make sure it targets the right rows:

```sql
-- First, check which rows will be affected
SELECT * FROM students WHERE grade = 11;

-- If the results look correct, then run the delete
DELETE FROM students WHERE grade = 11;
```

#### 2. Use transactions for safety

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

#### 3. Consider soft deletes

Instead of actually deleting records, consider adding an "is_deleted" or "status" column:

```sql
-- Instead of DELETE FROM students WHERE id = 5;
UPDATE students
SET status = 'inactive'
WHERE id = 5;
```

This preserves the data for historical purposes while removing it from active use.

### Truncating Tables

If you do want to delete all records from a table (but keep the table structure), you can use:

```sql
DELETE FROM table_name;
```

### Common DELETE Scenarios

#### Deleting duplicate records

```sql
-- Delete duplicate students (keeping the one with the lowest id)
DELETE FROM students
WHERE id NOT IN (
    SELECT MIN(id)
    FROM students
    GROUP BY name, age, grade
);
```

#### Deleting old records

```sql
-- Delete products that haven't been updated in over a year
DELETE FROM products
WHERE last_updated < date('now', '-1 year');
```

## Practice Exercises

1. Update the grade for all students named "John" to 12
2. Increase the age of all students by 1 (to simulate a new school year)
3. Delete a specific student by name
4. Use a transaction to safely delete all students with NULL ages
5. Update all products with prices less than $10 to have a 5% price increase

## Next Steps

Now that you know how to modify and remove data from your tables, in the next section we'll learn about database relationships and how they connect different tables together.
