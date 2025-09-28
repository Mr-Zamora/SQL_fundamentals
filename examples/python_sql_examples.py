"""
Python SQL Integration Examples

This file contains practical examples of using SQL with Python.
These examples demonstrate how to integrate SQL databases into Python applications.
"""

import sqlite3
import os
import pandas as pd
from datetime import datetime

# Example 1: Basic Connection and Query
def basic_example():
    print("\n=== Example 1: Basic Connection and Query ===")
    
    # Connect to database (creates it if it doesn't exist)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
    ''')
    
    # Insert some data
    try:
        cursor.execute('''
        INSERT INTO users (name, email, age)
        VALUES (?, ?, ?)
        ''', ('Alice Smith', 'alice@example.com', 28))
    except sqlite3.IntegrityError:
        print("User already exists")
    
    # Query the data
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    
    print("Users in database:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")
    
    # Close the connection
    conn.close()

# Example 2: Using Context Managers
def context_manager_example():
    print("\n=== Example 2: Using Context Managers ===")
    
    # Using with statement automatically handles closing the connection
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        
        # Insert multiple users
        users_to_add = [
            ('Bob Johnson', 'bob@example.com', 35),
            ('Charlie Brown', 'charlie@example.com', 22),
            ('Diana Miller', 'diana@example.com', 41)
        ]
        
        try:
            cursor.executemany('INSERT INTO users (name, email, age) VALUES (?, ?, ?)', users_to_add)
            print(f"Added {cursor.rowcount} users")
        except sqlite3.IntegrityError as e:
            print(f"Error adding users: {e}")
        
        # Commit is automatic with context manager
        
        # Query with filtering
        cursor.execute('SELECT * FROM users WHERE age > ?', (30,))
        users = cursor.fetchall()
        
        print("\nUsers over 30:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")

# Example 3: Working with Pandas
def pandas_example():
    print("\n=== Example 3: Working with Pandas ===")
    
    # Connect to database
    conn = sqlite3.connect('example.db')
    
    # Read SQL query directly into a pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM users", conn)
    
    print("\nUsers DataFrame:")
    print(df)
    
    # Calculate statistics
    print("\nAge statistics:")
    print(df['age'].describe())
    
    # Filter data
    young_users = df[df['age'] < 30]
    print("\nUsers under 30:")
    print(young_users)
    
    # Create a new DataFrame
    new_users = pd.DataFrame([
        {'name': 'Eva Green', 'email': 'eva@example.com', 'age': 27},
        {'name': 'Frank White', 'email': 'frank@example.com', 'age': 33}
    ])
    
    # Write DataFrame to SQL
    new_users.to_sql('users', conn, if_exists='append', index=False)
    
    # Verify the new data
    updated_df = pd.read_sql_query("SELECT * FROM users", conn)
    print("\nUpdated users:")
    print(updated_df)
    
    conn.close()

# Example 4: Building a Simple Data Entry Application
def data_entry_app():
    print("\n=== Example 4: Simple Data Entry Application ===")
    
    # Connect to database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Create a tasks table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
        completed INTEGER DEFAULT 0
    )
    ''')
    conn.commit()
    
    def add_task():
        title = input("Task title: ")
        description = input("Description (optional): ")
        due_date = input("Due date (YYYY-MM-DD): ")
        priority = input("Priority (low/medium/high): ").lower()
        
        # Validate priority
        if priority not in ('low', 'medium', 'high'):
            print("Invalid priority. Setting to medium.")
            priority = 'medium'
        
        # Validate date format
        try:
            if due_date:
                datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Using empty date.")
            due_date = ''
        
        cursor.execute('''
        INSERT INTO tasks (title, description, due_date, priority)
        VALUES (?, ?, ?, ?)
        ''', (title, description, due_date, priority))
        conn.commit()
        print("Task added successfully!")
    
    def list_tasks():
        cursor.execute('''
        SELECT id, title, due_date, priority, completed FROM tasks
        ORDER BY 
            CASE 
                WHEN priority = 'high' THEN 1
                WHEN priority = 'medium' THEN 2
                WHEN priority = 'low' THEN 3
            END,
            due_date
        ''')
        
        tasks = cursor.fetchall()
        
        if not tasks:
            print("No tasks found.")
            return
        
        print("\nID | Title                 | Due Date   | Priority | Status")
        print("-" * 60)
        
        for task in tasks:
            task_id, title, due_date, priority, completed = task
            status = "Completed" if completed else "Pending"
            print(f"{task_id:2} | {title[:20]:<20} | {due_date or 'N/A':<10} | {priority:<8} | {status}")
    
    def complete_task():
        task_id = input("Enter task ID to mark as completed: ")
        
        try:
            task_id = int(task_id)
            cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
            
            if cursor.rowcount == 0:
                print(f"No task found with ID {task_id}")
            else:
                conn.commit()
                print("Task marked as completed!")
        except ValueError:
            print("Invalid task ID")
    
    # Simple menu system
    while True:
        print("\nTask Manager")
        print("1. Add new task")
        print("2. List all tasks")
        print("3. Mark task as completed")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
    
    conn.close()

# Example 5: Database Backup and Restore
def backup_restore_example():
    print("\n=== Example 5: Database Backup and Restore ===")
    
    # Function to backup the database
    def backup_database(source_db, backup_file):
        print(f"Backing up {source_db} to {backup_file}...")
        
        # Connect to source database
        source_conn = sqlite3.connect(source_db)
        
        # Connect to backup database
        backup_conn = sqlite3.connect(backup_file)
        
        # Copy data
        source_conn.backup(backup_conn)
        
        # Close connections
        source_conn.close()
        backup_conn.close()
        
        print("Backup completed!")
    
    # Function to restore from backup
    def restore_database(backup_file, target_db):
        print(f"Restoring from {backup_file} to {target_db}...")
        
        # Connect to backup database
        backup_conn = sqlite3.connect(backup_file)
        
        # Connect to target database
        target_conn = sqlite3.connect(target_db)
        
        # Copy data
        backup_conn.backup(target_conn)
        
        # Close connections
        backup_conn.close()
        target_conn.close()
        
        print("Restore completed!")
    
    # Create a backup
    backup_database('example.db', 'example_backup.db')
    
    # Simulate data loss
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id > 2')
        print(f"Simulated data loss: Deleted {cursor.rowcount} users")
        
        # Show remaining data
        cursor.execute('SELECT COUNT(*) FROM users')
        count = cursor.fetchone()[0]
        print(f"Remaining users: {count}")
    
    # Restore from backup
    restore_database('example_backup.db', 'example.db')
    
    # Verify restoration
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM users')
        count = cursor.fetchone()[0]
        print(f"Users after restore: {count}")

# Run all examples
if __name__ == "__main__":
    print("Python SQL Integration Examples")
    print("===============================")
    
    # Remove example database if it exists
    if os.path.exists('example.db'):
        os.remove('example.db')
    
    # Run examples
    basic_example()
    context_manager_example()
    pandas_example()
    
    choice = input("\nRun interactive task manager example? (y/n): ")
    if choice.lower() == 'y':
        data_entry_app()
    
    choice = input("\nRun backup/restore example? (y/n): ")
    if choice.lower() == 'y':
        backup_restore_example()
    
    print("\nAll examples completed!")
