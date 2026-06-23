import os
import json
import tempfile

from dotenv import load_dotenv
from google import genai
from PIL import Image

from prompts.waste_prompt import WASTE_ANALYSIS_PROMPT


# -----------------------
# Load Environment
# -----------------------
load_dotenv()


# -----------------------
# Gemini Client
# -----------------------
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# -----------------------
# AI Scan Function
# -----------------------
def process_scan(upload_file):

    # Read uploaded image
    contents = upload_file.file.read()

    # Save temporary image
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        temp.write(contents)
        temp_path = temp.name

    # Open image
    image = Image.open(temp_path)

    # Gemini API Call
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            WASTE_ANALYSIS_PROMPT,
            image
        ]
    )

    # Convert JSON string to Python Dictionary
    ai_result = json.loads(response.text)

    # Delete temp file
    os.remove(temp_path)

    return ai_result