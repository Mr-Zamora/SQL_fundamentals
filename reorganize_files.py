"""
Script to reorganize the SQL tutorial files into a folder structure.
This script will:
1. Create the necessary folders
2. Move files to their appropriate folders
3. Update the index.md file with new file paths
"""

import os
import shutil
import re

# Define the folder structure and which files go where
folder_structure = {
    "tutorials": [
        "01_introduction_to_databases.md",
        "02_getting_started_with_sqlite.md",
        "03_creating_tables.md",
        "04_inserting_data.md",
        "05_reading_data.md",
        "06_filtering_data.md",
        "07_ordering_results.md",
        "08_limiting_results.md",
        "09_updating_records.md",
        "10_deleting_records.md",
        "11_database_design_basics.md",
        "12_next_steps.md"
    ],
    "setup": [
        "00_setup_guide.md"
    ],
    "references": [
        "sql_cheat_sheet.md",
        "sql_glossary.md",
        "visual_sql_guide.md",
        "sql_best_practices.md"
    ],
    "examples": [
        "complete_example.py",
        "python_sql_examples.py",
        "classroom_demo.py"
    ],
    "exercises": [
        "exercises.md",
        "exercise_solutions.md",
        "assessment_guide.md",
        "interview_questions.md"
    ],
    "resources": [
        "project_ideas.md",
        "troubleshooting_guide.md",
        "teaching_guide.md"
    ]
}

# Files to keep in the root directory
keep_in_root = ["index.md", "README.md", "reorganize_files.py"]

def create_folders():
    """Create the necessary folders if they don't exist"""
    print("Creating folders...")
    for folder in folder_structure.keys():
        os.makedirs(folder, exist_ok=True)
        print(f"  Created {folder}/")

def move_files():
    """Move files to their appropriate folders"""
    print("\nMoving files...")
    for folder, files in folder_structure.items():
        for file in files:
            source = file
            destination = os.path.join(folder, file)
            
            if os.path.exists(source):
                shutil.move(source, destination)
                print(f"  Moved {source} -> {destination}")
            else:
                print(f"  Warning: {source} not found, skipping")

def update_index():
    """Update the index.md file with new file paths"""
    print("\nUpdating index.md...")
    
    if not os.path.exists("index.md"):
        print("  Warning: index.md not found, skipping update")
        return
    
    with open("index.md", "r") as file:
        content = file.read()
    
    # Update links in the content
    for folder, files in folder_structure.items():
        for file in files:
            # Match markdown links like [text](file.md) or [text](file.py)
            pattern = r'\[([^\]]+)\]\(' + re.escape(file) + r'\)'
            replacement = r'[\1](' + folder + '/' + file + r')'
            content = re.sub(pattern, replacement, content)
    
    # Write the updated content back to index.md
    with open("index.md", "w") as file:
        file.write(content)
    
    print("  Updated index.md with new file paths")

def update_readme():
    """Update the README.md file with new file paths if it exists"""
    print("\nChecking for README.md...")
    
    if not os.path.exists("README.md"):
        print("  README.md not found, skipping update")
        return
    
    with open("README.md", "r") as file:
        content = file.read()
    
    # Update links in the content
    for folder, files in folder_structure.items():
        for file in files:
            # Match markdown links like [text](file.md) or [text](file.py)
            pattern = r'\[([^\]]+)\]\(' + re.escape(file) + r'\)'
            replacement = r'[\1](' + folder + '/' + file + r')'
            content = re.sub(pattern, replacement, content)
    
    # Write the updated content back to README.md
    with open("README.md", "w") as file:
        file.write(content)
    
    print("  Updated README.md with new file paths")

def update_internal_links():
    """Update links within tutorial files to point to the new locations"""
    print("\nUpdating internal links in files...")
    
    # Create a mapping of old to new file paths
    file_mapping = {}
    for folder, files in folder_structure.items():
        for file in files:
            file_mapping[file] = f"{folder}/{file}"
    
    # Process each folder and its files
    for folder, files in folder_structure.items():
        for file in files:
            file_path = os.path.join(folder, file)
            
            # Only process markdown files
            if not file_path.endswith('.md'):
                continue
                
            try:
                with open(file_path, "r") as f:
                    content = f.read()
                
                # Update each link
                for old_path, new_path in file_mapping.items():
                    # Match markdown links like [text](file.md) or [text](file.py)
                    pattern = r'\[([^\]]+)\]\(' + re.escape(old_path) + r'\)'
                    replacement = r'[\1](' + new_path + r')'
                    content = re.sub(pattern, replacement, content)
                
                # Write the updated content back to the file
                with open(file_path, "w") as f:
                    f.write(content)
                    
                print(f"  Updated links in {file_path}")
            except Exception as e:
                print(f"  Error updating links in {file_path}: {e}")

def main():
    """Main function to reorganize files"""
    print("Starting file reorganization...\n")
    
    create_folders()
    move_files()
    update_index()
    update_readme()
    update_internal_links()
    
    print("\nReorganization complete!")
    print("\nNote: You may need to manually check and update some links in your files.")
    print("Especially check links in the tutorial files that reference other tutorial files.")

if __name__ == "__main__":
    main()
