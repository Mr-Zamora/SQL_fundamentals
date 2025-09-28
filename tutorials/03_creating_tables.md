# 3. Creating Tables

## Understanding Tables in SQL

Before we create tables, let's understand what they represent:

- Tables are the fundamental storage structure in a relational database
- Each table should represent one "entity" or "concept" (e.g., students, courses, teachers)
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

## Creating More Tables

Let's create two more tables for our school database:

### Courses Table

```sql
CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher TEXT,
    room TEXT
);
```

### Enrollments Table (Connecting Students and Courses)

```sql
CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id)
);
```

The `FOREIGN KEY` constraints establish relationships between tables.

## Viewing Table Structure

To see the structure of a table you've created:

```
sqlite> .schema students
```

This will show the CREATE TABLE statement used to create the table.

## Dropping (Deleting) Tables

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
3. Create an "assignments" table that references both students and courses

## Next Steps

Now that you've created tables to store your data, in the next section we'll learn how to insert data into these tables.
