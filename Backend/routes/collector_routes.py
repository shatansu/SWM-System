from fastapi import APIRouter
from fastapi import HTTPException

from services.collector_service import (
    get_pending_reports,
    accept_report,
    start_pickup,
    complete_pickup
)

router = APIRouter()


@router.get("/collector/reports")
def collector_reports():

    reports = get_pending_reports()

    return reports

@router.patch("/collector/accept/{report_id}")
def accept(report_id: str, collector_id: str):

    updated = accept_report(report_id, collector_id)

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return {
        "message": "Report Accepted Successfully"
    }


@router.patch("/collector/start/{report_id}")
def start(report_id: str):

    updated = start_pickup(report_id)

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return {
        "message": "Pickup Started"
    }

@router.patch("/collector/complete/{report_id}")
def complete(report_id: str):

    updated = complete_pickup(report_id)

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return {
        "message": "Pickup Completed"
    }