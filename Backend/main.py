from fastapi import FastAPI, UploadFile, File, Form

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

    return {
        "filename": image.filename,
        "content_type": image.content_type,
        "latitude": latitude,
        "longitude": longitude,
        "user_id": user_id,
        "message": "Image received successfully"
    }