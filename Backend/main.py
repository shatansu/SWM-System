from fastapi import FastAPI, UploadFile, File, Form

from services.scan_services import process_scan
from services.waste_service import save_report

# -----------------------------
# Load Environment Variables
# -----------------------------
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Eco Visionars Backend Running 🚀"
    }