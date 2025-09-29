# Getting Started with SQLite in Windsurf

This guide will help you get started with SQLite in the Windsurf environment for this SQL tutorial.

## What is SQLite?

SQLite is a lightweight, disk-based database that doesn't require a separate server process. It's perfect for learning SQL as it's:
- Self-contained
- Serverless
- Zero-configuration
- Transactional

## Using SQLite in Windsurf

SQLite comes built-in with Python, but to use the SQLite command-line interface directly, you'll need to install the SQLite command-line tools. Below are instructions for different operating systems.

### Setting Up the Tutorial

1. Download the tutorial repository using the terminal in Windsurf:
   ```
   git clone https://github.com/Mr-Zamora/SQL_fundamentals.git
   cd SQL_fundamentals
   ```

2. Verify SQLite is available through Python by running this code in the terminal:
   ```python
   python -c "import sqlite3; print('SQLite version:', sqlite3.sqlite_version)"
   ```

   You should see the SQLite version number displayed.

### Installing SQLite Command-Line Tools

#### For Windows Users

1. **Download SQLite Tools**:
   - Visit the [SQLite Download Page](https://www.sqlite.org/download.html)
   - Find and download the latest "Precompiled Binaries for Windows" > "sqlite-tools-win32-x86..." ZIP file

2. **Extract and Install**:
   - Create a folder at `C:\SQLite`
   - Extract the contents of the downloaded ZIP file to this folder

3. **Add to PATH** (to use `sqlite3` from any location):
   - Open PowerShell as Administrator
   - Run this command to add SQLite to your PATH:
     ```powershell
     [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\SQLite", "User")
     ```
   - Close and reopen your terminal for the changes to take effect
   
   > **Note for Windsurf Users**: If `sqlite3` works in your regular PowerShell but not in the Windsurf terminal, you may need to use the full path to the SQLite executable in the Windsurf terminal: `C:\SQLite\sqlite3` instead of just `sqlite3`

4. **Verify Installation**:
   - In a new terminal window, run:
     ```
     sqlite3 --version
     ```
   - If you see the SQLite version, the installation was successful

#### For Mac Users

1. **Using Homebrew** (recommended):
   - If you don't have Homebrew installed, install it first:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Install SQLite:
     ```bash
     brew install sqlite
     ```

2. **Verify Installation**:
   - Run:
     ```bash
     sqlite3 --version
     ```
   - If you see the SQLite version, the installation was successful

### Step 1: Using SQLite Command Line

#### Understanding Working Directories

**Important to understand**: When using SQLite, your database files are created and accessed in your current working directory, not where the SQLite program is installed.

- If you run `sqlite3 school.db` or `C:\SQLite\sqlite3 school.db`, the database file `school.db` will be created/accessed in your current working directory
- The SQLite program location (`C:\SQLite`) and your working directory (where your project files are) are completely separate concepts

#### Using SQLite

Once SQLite is installed, you can use the SQLite command-line interface:

1. In the terminal, navigate to your project folder where you want your database to be located:
   ```
   cd SQL_fundamentals
   ```

2. Start SQLite with a new database file (this will create or open the file in your current directory):

   **Option A**: If SQLite is in your PATH:
   ```
   sqlite3 school.db
   ```
   
   **Option B**: If the `sqlite3` command isn't recognized (especially in Windsurf terminal), use the full path:
   ```
   C:\SQLite\sqlite3 school.db
   ```
   
   > **Important**: Both commands create/open the database in your current directory, not in C:\SQLite. The full path only tells Windows where to find the SQLite program.

3. You should see the SQLite prompt:
   ```
   SQLite version X.X.X
   Enter ".help" for usage hints.
   sqlite>
   ```

4. **IMPORTANT**: SQLite commands (like `.help`, `.tables`, etc.) and SQL queries can ONLY be run within the SQLite shell after you see the `sqlite>` prompt. These commands will not work directly in PowerShell or Terminal.

   For example, once you see the `sqlite>` prompt, you can run:
   ```
   .help                   (shows available SQLite commands)
   .tables                 (lists all tables in the database)
   .schema table_name      (shows the structure of a table)
   .databases              (shows the path to your current database file - confirms your working directory)
   SELECT * FROM table;    (runs an SQL query - note the semicolon)
   ```

5. To exit the SQLite prompt and return to the terminal, type:
   ```
   .exit
   ```

#### Troubleshooting

If the `sqlite3` command is not recognized:
- For Windows: Use the full path: `C:\SQLite\sqlite3 school.db`
  - Note: Using the full path only specifies where to find the SQLite program; it does NOT change your working directory. Your database operations will still work in your current directory.
  - To verify your current working directory in SQLite, you can run: `.databases` (this shows the path to your current database file)
- **For Windsurf Terminal Users**: The Windsurf terminal may have a different PATH setting than your regular PowerShell. If `sqlite3` works in your regular PowerShell but not in Windsurf, always use the full path in Windsurf: `C:\SQLite\sqlite3 school.db`
- For Mac: Make sure Homebrew's bin directory is in your PATH
- If you've just added SQLite to your PATH, you may need to close and reopen your terminal


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
