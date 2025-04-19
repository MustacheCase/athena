import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Set the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def summarize_article(title, content):
    prompt = f"TL;DR Professional summary of '{title}':\n\n{content}"


    # Generate content using the correct method
    response = model.generate_content(prompt)

    return response.text
