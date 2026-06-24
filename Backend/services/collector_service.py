from db.mongodb_connection import reports_collection
from bson import ObjectId
from datetime import datetime
from constants.status import ACCEPTED, ON_THE_WAY, COMPLETED, REJECTED, PENDING

def get_pending_reports(collector_id: str):

    reports = list(
       reports_collection.find(
    {
        "status": PENDING,
        "rejection_history.collector_id": {
            "$ne": collector_id
        }
    },
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

def start_pickup(report_id: str):

    result = reports_collection.update_one(

        {
            "_id": ObjectId(report_id)
        },

        {
            "$set": {
                "status": ON_THE_WAY,
                "on_the_way_at": datetime.utcnow()
            }
        }

    )

    return result.modified_count


def complete_pickup(report_id: str):

    result = reports_collection.update_one(
        {"_id": ObjectId(report_id)},
        {
            "$set": {
                "status": COMPLETED,
                "completed_at": datetime.utcnow()
            }
        }
    )

    return result.modified_count

def reject_report(
    report_id: str,
    collector_id: str,
    reason: str
):

    result = reports_collection.update_one(

        {
            "_id": ObjectId(report_id)
        },

        {
            "$set": {
                "status": PENDING,
                "collector_id": None
            },

            "$unset": {
                "accepted_at": ""
            },

            "$push": {
                "rejection_history": {

                    "collector_id": collector_id,

                    "reason": reason,

                    "rejected_at": datetime.utcnow()

                }
            }

        }

    )

    return result.modified_count


def update_collector_location(
    collector_id: str,
    latitude: float,
    longitude: float
):

    result = reports_collection.update_many(

        {
            "collector_id": collector_id,
            "status": ON_THE_WAY
        },

        {
            "$set": {
                "collector_location.latitude": latitude,
                "collector_location.longitude": longitude,
                "collector_location.updated_at": datetime.utcnow()
            }
        }

    )

    return result.modified_count