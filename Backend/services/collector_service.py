from db.mongodb_connection import reports_collection
from bson import ObjectId
from datetime import datetime
from constants.status import ACCEPTED

def get_pending_reports():

    reports = list(
        reports_collection.find(
            {"status": "Pending"},
            {
                "_id": 1,
                "user_id": 1,
                "waste_type": 1,
                "confidence": 1,
                "latitude": 1,
                "longitude": 1,
                "status": 1,
                "created_at": 1
            }
        )
    )

    # ObjectId ko string me convert karna
    for report in reports:
        report["_id"] = str(report["_id"])

    return reports

from bson import ObjectId
from datetime import datetime


def accept_report(report_id: str, collector_id: str):

    result = reports_collection.update_one(
        {"_id": ObjectId(report_id)},
        {
            "$set": {
                "status": ACCEPTED,
                "collector_id": collector_id,
                "accepted_at": datetime.utcnow()
            }
        }
    )

    return result.modified_count