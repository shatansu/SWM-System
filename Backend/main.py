from fastapi import FastAPI, UploadFile, File, Form

from services.scan_services import process_scan
from services.waste_service import save_report
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Eco Visionars Backend Running 🚀"
    }

@app.post("/scan")
async def scan(
    image: UploadFile = File(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
    user_id: str = Form(...)
):

    # AI Scan
    ai_result = process_scan(image)

    # MongoDB Save
    report_id = save_report(
        user_id=user_id,
        latitude=latitude,
        longitude=longitude,
        image_name=image.filename,
        ai_result=ai_result
    )

    return {
        "report_id": report_id,
        "ai_result": ai_result
    }