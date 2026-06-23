from fastapi import APIRouter
from fastapi import HTTPException

from services.collector_service import (
    get_pending_reports,
    accept_report
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