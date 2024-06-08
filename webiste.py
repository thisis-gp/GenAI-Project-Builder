import streamlit as st
from pathlib import Path
from file_operations import create_files_and_folders, zip_project_files
from gemini_api import generate_file_structure

def main():
    st.title("AI Project Generator")

    project_description = st.text_input("Describe what you want to build:")

    if st.button("Generate Project"):
        if not project_description:
            st.error("Please provide a project description.")
        else:
            with st.spinner("Generating file structure..."):
                file_structure = generate_file_structure(project_description)
                st.success("File structure generated.")
                st.text_area("Generated File Structure", value=file_structure, height=200)

            with st.spinner("Creating files and folders..."):
                project_path = Path('generated_project')
                create_files_and_folders(project_path, file_structure, project_description)
                zip_project_files(project_path)
                st.success("Project files created and zipped.")
                
                with open("generated_project.zip", "rb") as zip_file:
                    st.download_button(label="Download Project ZIP", data=zip_file, file_name="generated_project.zip", mime="application/zip")

if __name__ == "__main__":
    main()
