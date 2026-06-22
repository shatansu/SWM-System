from fastapi import FastAPI, UploadFile, File, Form

import os
import tempfile

from dotenv import load_dotenv
from google import genai
from PIL import Image

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

# -----------------------------
# Gemini Client
# -----------------------------
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Eco Visionars Backend Running 🚀"
    }


@app.post("/scan")
async def scan_waste(
    image: UploadFile = File(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
    user_id: str = Form(...)
):
    # Read uploaded image
    contents = await image.read()

    # Save image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        temp.write(contents)
        temp_path = temp.name

    # Open image using Pillow
    img = Image.open(temp_path)

    # Prompt for Gemini
    prompt = """
You are an AI Waste Detection System.

Analyze this image carefully.

Return ONLY the following information:

1. Is this image actually waste? (YES or NO)

2. Waste Category
(Plastic, Paper, Glass, Metal, Organic, Mixed, Other)

3. Confidence Score (0-100)

4. Short Reason (Maximum 20 words)

Return the response in plain text.
"""

    # Gemini API Call
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, img]
    )

    # Return Response
    return {
        "filename": image.filename,
        "content_type": image.content_type,
        "latitude": latitude,
        "longitude": longitude,
        "user_id": user_id,
        "ai_result": response.text
    }