# GenAI Project Builder

# GenAI Project Builder

This project allows users to generate a project structure and files using Generative AI models, specifically leveraging the Gemini API. The project includes a frontend built with Streamlit, allowing users to interact with the AI and generate projects easily through a web interface.

## Features

- **Generative AI Integration**: Uses the Gemini API to generate project structures and file contents based on user descriptions.
- **Streamlit Frontend**: Provides a user-friendly web interface for generating and downloading project files.
- **File Structure Limitations**: Ensures that no more than 20 files are generated to manage API usage and performance.
- **Zipped Output**: Packages the generated project into a zip file for easy download.

## Installation

To run this project locally, you need to have Python installed. Follow the steps below to set up the project:

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your-username/genai-project-builder.git
   cd genai-project-builder
   ```

2. **Create a virtual environment** (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the environment variables**:

   Create a `.env` file in the project root directory and add your Gemini API key:

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Usage

You can run the Streamlit app locally to use the project builder:

```sh
streamlit run website.py
```

After running the above command, you can open your web browser and navigate to http://localhost:8501 to access the app.

## Deployed Application

The project is also deployed on Streamlit. You can access it via the following URL: [GenAI Project Builder](https://genai-project-builder.streamlit.app/)

## Files

- **`main.py`**: The main script that ties everything together.
- **`config.py`**: Configuration settings and environment variable loading.
- **`gemini_api.py`**: Functions related to interacting with the Gemini API.
- **`file_operations.py`**: Functions related to creating files, folders, and zipping them.
- **`website.py`**: Streamlit web application.
- **`.env`**: Environment variables file (not included, you need to create this).
- **`requirements.txt`**: List of Python packages required to run the project.

## Environment Variables

The project requires the following environment variable:

- `GEMINI_API_KEY`: Your Gemini API key. You can obtain this key by signing up for the Gemini API.

To set up the environment variables, create a `.env` file in the root directory of the project and add the key as follows:

```ini
GEMINI_API_KEY=your_gemini_api_key_here
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
