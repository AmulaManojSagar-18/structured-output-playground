import os
import json
# pyrefly: ignore [missing-import]
from google import genai
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_json(user_text, schema_text):

    prompt = f"""
You are an information extraction system.

Extract information from the provided text.

Return ONLY valid JSON.

Follow this schema exactly:

{schema_text}

Text:

{user_text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text
