# 2. Getting Started with SQLite

## What is SQLite?

SQLite is a lightweight, file-based database system that's perfect for learning SQL. Unlike other database systems that require a server, SQLite stores the entire database in a single file on your computer.

Key features of SQLite:
- Self-contained (no external dependencies)
- Zero configuration (no setup required)
- Portable (the entire database is in one file)
- Reliable (ACID-compliant transactions)
- Small footprint (less than 600KB)

## Accessing SQLite

There are two main ways to work with SQLite:

1. **Command-line Interface (CLI)**: Using the `sqlite3` command
2. **Through Python**: Using the built-in `sqlite3` module

We'll cover both methods, but focus primarily on the command-line interface for this tutorial.

## Method 1: Using the SQLite Command-line Interface

### Starting the SQLite Shell

Once SQLite is installed (see the setup guide), you can start the SQLite shell by opening a command prompt or terminal and typing:

```
sqlite3 school.db
```

This command:
- Opens the SQLite shell
- Creates a new database file called "school.db" if it doesn't exist, or opens it if it does

You should see something like:

```
SQLite version 3.36.0
Enter ".help" for usage hints.
sqlite>
```

The `sqlite>` prompt indicates that you're now in the SQLite shell, ready to execute SQL commands.

### Useful SQLite Shell Commands

These commands start with a dot (.) and are specific to the SQLite shell (not SQL language):

- `.help` - Display help information
- `.tables` - List all tables in the database
- `.schema TABLE_NAME` - Show the CREATE statement for a table
- `.mode column` - Display results in a column format (more readable)
- `.headers on` - Show column names in results
- `.exit` or `.quit` - Exit the SQLite shell

### Example Session

```
$ sqlite3 school.db
SQLite version 3.36.0
Enter ".help" for usage hints.
sqlite> .mode column
sqlite> .headers on
sqlite> .tables
(no tables yet)
sqlite> .exit
```

## Method 2: Using SQLite with Python

Python has built-in support for SQLite through the `sqlite3` module.

### Basic Python Example

```python
import sqlite3

# Connect to a database (creates it if it doesn't exist)
conn = sqlite3.connect('school.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute SQL commands
cursor.execute("SELECT sqlite_version();")

# Fetch the result
version = cursor.fetchone()
print(f"SQLite version: {version[0]}")

# Close the connection when done
conn.close()
```

Save this as `check_sqlite.py` and run it to verify your Python SQLite setup.

## Creating a New Database

### With Command Line

Simply specify a new filename when starting SQLite:

```
sqlite3 new_database.db
```

### With Python

```python
import sqlite3
conn = sqlite3.connect('new_database.db')
# ... work with the database ...
conn.close()
```

## Database Location

When you create a database, it's stored in your current working directory unless you specify a full path.

For this tutorial, we'll use a database called `school.db` that will contain information about students, courses, and enrollments.

## Next Steps

Now that you know how to access SQLite, in the next section we'll learn how to create tables to store our data.
