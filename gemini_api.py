import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def generate_gemini_prompt(prompt):
    response = model.generate_content(prompt)
    return response.text

def generate_file_structure(description):
    prompt = f"Generate a file structure for a project with the following description: {description}"
    return generate_gemini_prompt(prompt)
