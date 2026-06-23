from datetime import datetime
from db.mongodb_connection import reports_collection


def save_report(
    user_id,
    latitude,
    longitude,
    image_name,
    ai_result
):

    report = {
        "user_id": user_id,

        "image_name": image_name,

        "latitude": latitude,
        "longitude": longitude,

        "is_waste": ai_result["is_waste"],
        "waste_type": ai_result["waste_type"],
        "confidence": ai_result["confidence"],
        "reason": ai_result["reason"],
        "pickup_required": ai_result["pickup_required"],

        "status": "Pending",

        "created_at": datetime.utcnow()
    }

    result = reports_collection.insert_one(report)

    return str(result.inserted_id)