# Structured Output Playground

This is a Streamlit application that uses Google's Gemini AI to extract information from unstructured text and format it into a valid JSON object based on a provided schema.

## Dependencies

The project relies on the following Python packages:
- `streamlit` - For the web interface
- `google-genai` - For communicating with the Gemini API
- `pydantic` - For data validation
- `python-dotenv` - For loading environment variables

## Setup & Installation

1. **Create a virtual environment:**
   ```powershell
   python -m venv .venv
   ```

2. **Activate the virtual environment:**
   * On Windows (PowerShell):
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   * On Windows (Command Prompt):
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
   * On Mac/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies:**
   Make sure your virtual environment is active (you should see `(.venv)` in your terminal), then run:
   ```powershell
   python -m pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add your Gemini API Key:
   ```env
   GEMINI_API_KEY="your_api_key_here"
   ```

## How to Run

With your virtual environment activated, start the Streamlit server:
```powershell
python -m streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`.

## Screenshot

![App Screenshot](C:/Users/manoj%20sagar/.gemini/antigravity-ide/brain/9290738c-e8bf-4af7-aea0-0b1c0f992345/streamlit_output_mockup_1784112300022.png)
