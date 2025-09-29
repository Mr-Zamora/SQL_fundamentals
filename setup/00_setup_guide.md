# Getting Started with SQLite in Windsurf

This guide will help you get started with SQLite in the Windsurf environment for this SQL tutorial.

## What is SQLite?

SQLite is a lightweight, disk-based database that doesn't require a separate server process. It's perfect for learning SQL as it's:
- Self-contained
- Serverless
- Zero-configuration
- Transactional

## Using SQLite in Windsurf

Good news! Since you're using Windsurf and already have Python installed, you're ready to start using SQLite right away. SQLite comes built-in with Python, so no additional installation is needed.

### Setting Up the Tutorial

1. Download the tutorial repository using the terminal in Windsurf:
   ```
   git clone https://github.com/Mr-Zamora/SQL_fundamentals.git
   cd SQL_fundamentals
   ```

2. Verify SQLite is working by running this Python code in the terminal:
   ```python
   python -c "import sqlite3; print('SQLite version:', sqlite3.sqlite_version)"
   ```

   You should see the SQLite version number displayed.



### Step 1: Using SQLite Command Line in Windsurf Terminal

You can also use the SQLite command-line interface directly in the Windsurf terminal:

1. In the Windsurf terminal, navigate to your project folder (if you're not already there):
   ```
   cd SQL_fundamentals
   ```

2. Start SQLite with a new database file:
   ```
   sqlite3 school.db
   ```

3. You should see the SQLite prompt:
   ```
   SQLite version X.X.X
   Enter ".help" for usage hints.
   sqlite>
   ```

4. To exit the SQLite prompt and return to the terminal, type:
   ```
   .exit
   ```


## Optional: Using DB Browser for SQLite (Visual Tool)

If you prefer a graphical interface to work with your SQLite databases, DB Browser for SQLite (DB4S) is an excellent free, open-source tool.

### What is DB Browser for SQLite?

DB Browser for SQLite provides a visual way to:
- Create, design, and edit database files
- View and edit tables, indexes, and views
- Run SQL queries with syntax highlighting
- See the results in a spreadsheet-like interface
- Import and export data in various formats

### Installing DB Browser for SQLite

1. Download the installer from the [official website](https://sqlitebrowser.org/dl/)
2. Choose the appropriate version for your operating system
3. Run the installer and follow the prompts

### Using DB Browser with Your Databases

1. Open DB Browser for SQLite
2. Click "Open Database" and navigate to your `.db` file
3. You'll see four main tabs:
   - **Database Structure**: View tables, indexes, and other objects
   - **Browse Data**: View and edit table contents
   - **Edit Pragmas**: Configure database settings
   - **Execute SQL**: Write and run SQL queries

### Benefits of Using DB Browser

- Visualize your database structure
- Easily inspect table contents
- Get immediate feedback on your SQL queries
- Export query results to CSV or other formats
- Understand relationships between tables

### When to Use DB Browser vs. Command Line

While DB Browser is helpful for visualization, we recommend still learning the command-line approach first, as it:
- Reinforces SQL syntax knowledge
- Works in environments where GUI tools aren't available
- Prepares you for working with databases in professional settings

Consider DB Browser as a supplementary tool rather than a replacement for writing SQL directly.

## Next Steps

Now that you know how to access SQLite in Windsurf, you're ready to proceed with the tutorial! Continue to the next section to learn about creating tables and working with data.
