# GenAI Project Builder

## Project Builder with Gemini API

This project automates the generation of a project structure based on a given description using the Gemini API. It creates the directory structure, generates the necessary files, and packages everything into a zip archive.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Environment Variables](#environment-variables)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/project-builder.git
   cd project-builder
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the environment variables:**
   - Create a `.env` file in the root directory of the project.
   - Add your Gemini API key to the `.env` file:
     ```ini
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

## Usage

1. **Run the script:**

   ```bash
   python main.py
   ```

2. **Follow the prompt to describe the project:**
   - The script will ask you to input a description of what you want to build.
   - Based on the description, it will generate a file structure, create the files and folders, and zip them into `generated_project.zip`.

## Files

- **`main.py`**: The main script that ties everything together.
- **`config.py`**: Configuration settings and environment variable loading.
- **`gemini_api.py`**: Functions related to interacting with the Gemini API.
- **`file_operations.py`**: Functions related to creating files, folders, and zipping them.
- **`.env`**: Environment variables file (not included, you need to create this).
- **`requirements.txt`**: List of Python packages required to run the project.

## Environment Variables

The project requires the following environment variable:

- `GEMINI_API_KEY`: Your Gemini API key. You can obtain this key by signing up for the Gemini API.

To set up the environment variables, create a `.env` file in the root directory of the project and add the key as follows:

```ini
GEMINI_API_KEY=your_gemini_api_key_here
```
