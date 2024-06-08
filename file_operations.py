import os
import zipfile
from pathlib import Path
from gemini_api import generate_gemini_prompt

def create_folder(current_path):
    os.makedirs(current_path, exist_ok=True)

def create_files_and_folders(path, file_structure, project_description):
    files_generated = 0
    print("Maximum number of files can be generated: 20")

    lines = file_structure.split('\n')[2:-1]

    current_path = path
    stack = [path]
    folder_generated = 0

    for line in lines:
        if files_generated >= 20:
            print("Maximum file limit reached. Stopping file generation.")
            break

        if "├──" in line or "└──" in line:
            if "." in line:
                if line[2] == " ":
                    file_name = line.split(" ")[-1]
                    file_path = current_path.joinpath(file_name)
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    generate_file_content(project_description, file_structure, file_name, file_path)
                    files_generated += 1
                    print("Created", file_name)
                else:
                    file_name = line.strip().split(" ")[1]
                    file_path = stack[folder_generated - 1].joinpath(file_name)
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    generate_file_content(project_description, file_structure, file_name, file_path)
                    files_generated += 1
                    print("Created", file_name)
            else:
                folder_name = line.strip().split(" ")[1]
                current_path = stack[folder_generated - 1].joinpath(folder_name)
                create_folder(current_path)
                stack.append(current_path)
                folder_generated += 1

        else:
            folder_name = line
            current_path = current_path.joinpath(folder_name)
            create_folder(current_path)
            stack.append(current_path)
            folder_generated += 1

    print(f"Files and directories created under '{path}'")

def generate_file_content(description, structure, name, path):
    prompt = f"Based on the following project description and file structure, generate the content for the file '{name}':\n\nProject Description:\n{description}\n\nFile Structure:\n{structure}"
    content = generate_gemini_prompt(prompt)
    with open(path, 'w') as f:
        if "```" in content:
            lines = content.split('\n')[1:-1]
        else:
            lines = content.split("\n")
        for line in lines:
            f.write(line + "\n")

def zip_project_files(project_path, zip_name='generated_project.zip'):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(project_path):
            for file in files:
                file_path = Path(root) / file
                zipf.write(file_path, file_path.relative_to(project_path))
