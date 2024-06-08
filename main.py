from pathlib import Path
from gemini_api import generate_file_structure
from file_operations import create_files_and_folders, zip_project_files

# Step 1: Take input from the user on what they want to build/generate
project_description = input("Describe what you want to build: ")

# Step 2: Generate the file structure
file_structure = generate_file_structure(project_description)
print("Generated file structure in the format:\n", file_structure)

# Step 3: Define base path for project files
project_path = Path('generated_project')
create_files_and_folders(project_path, file_structure, project_description)

# Step 4: Package the generated files into a zip archive
zip_project_files(project_path)

print(f"Project files have been generated and zipped into {project_path}.zip")

# Optional: clean up generated project files after zipping (uncomment if needed)
# import shutil
# shutil.rmtree(project_path)
