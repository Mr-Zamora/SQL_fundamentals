# 3. Creating Tables

## Understanding Tables in SQL

Before we create tables, let's understand what they represent:

- Tables are the fundamental storage structure in a relational database
- Each table should represent one "entity" or "concept" (e.g., students, products, tasks)
- Tables have a defined structure (schema) that specifies what data they can contain

## CREATE TABLE Syntax

The basic syntax for creating a table is:

```sql
CREATE TABLE table_name (
    column1_name data_type constraints,
    column2_name data_type constraints,
    ...
);
```

Where:
- `table_name` is what you want to call your table
- `column_name` is the name for each column
- `data_type` specifies what kind of data can be stored in the column
- `constraints` are optional rules for the data (e.g., NOT NULL, UNIQUE)

## SQLite Data Types

SQLite has five main data types:

1. **INTEGER**: Whole numbers (e.g., 1, 42, -7)
2. **REAL**: Decimal numbers (e.g., 3.14, -2.5)
3. **TEXT**: Text strings (e.g., "Hello", "John Smith")
4. **BLOB**: Binary data (e.g., images, files)
5. **NULL**: Represents missing data

Unlike some other database systems, SQLite uses "type affinity" which means it's somewhat flexible with data types.

## Planning Your Table Structure

Before creating a table, it's important to plan its structure:

1. Decide what entity the table will represent (e.g., students)
2. Identify the attributes you need to store (e.g., name, age, grade)
3. Choose appropriate data types for each attribute
4. Determine which constraints are needed

## Creating Your First Table

Let's create a simple "students" table:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade INTEGER
);
```

This SQL statement:
- Creates a table named "students"
- Defines 4 columns: id, name, age, and grade
- Makes "id" the primary key (unique identifier for each row)
- Requires "name" to have a value (NOT NULL)

### Running this in SQLite CLI:

```
sqlite> CREATE TABLE students (
   ...>     id INTEGER PRIMARY KEY,
   ...>     name TEXT NOT NULL,
   ...>     age INTEGER,
   ...>     grade INTEGER
   ...> );
sqlite> .tables
students
```

### Running this in Python:

```python
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade INTEGER
)
''')

conn.commit()
conn.close()
```

## Common Column Constraints

Constraints are rules that restrict what data can be stored:

- **PRIMARY KEY**: Uniquely identifies each row in the table
- **NOT NULL**: Column must have a value (can't be empty)
- **UNIQUE**: All values in the column must be different
- **DEFAULT value**: Specifies a default value for the column
- **CHECK (condition)**: Ensures data meets a specific condition

## Examples of Constraints

Let's see some examples of these constraints in action:

### DEFAULT Constraint

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    in_stock INTEGER DEFAULT 0
);
```

Here, new products will have `in_stock` set to 0 unless specified otherwise.

### UNIQUE Constraint

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
```

This ensures no two users can have the same username or email.

### CHECK Constraint

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL CHECK(salary > 0),
    department TEXT
);
```

This prevents negative salary values from being entered.

## Viewing Table Structure

To see the structure of a table you've created:

```
sqlite> .schema students
```

This will show the CREATE TABLE statement used to create the table.

## Modifying Tables

### Adding a Column

You can add a new column to an existing table:

```sql
ALTER TABLE students ADD COLUMN email TEXT;
```

### Renaming a Table

```sql
ALTER TABLE students RENAME TO school_students;
```

### Dropping (Deleting) Tables

If you need to delete a table:

```sql
DROP TABLE table_name;
```

For example:

```sql
DROP TABLE students;
```

Be careful with this command! It permanently deletes the table and all its data.

## Practice Exercise

1. Create a "teachers" table with columns for id, name, subject, and email
2. View the structure of your new table
3. Create a "courses" table with columns for id, name, description, and credits
4. Add a "start_date" column to your students table with a default value of the current date

## Next Steps

Now that you've created tables to store your data, in the next section we'll learn how to insert data into these tables.
