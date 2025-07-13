from fastapi import APIRouter
from models.schemas import ScheduleRequest
from dotenv import load_dotenv


load_dotenv()

router = APIRouter()
# Mock function
def check_calendar(date, time):
    return time == "10:00"

def suggest_alternative_slots():
    return ["10:00", "11:00", "14:00"]


@router.post("/schedule_visit")
def schedule_visit(request: ScheduleRequest):
    # Simulate checking availability
    available = check_calendar(request.date, request.time)
    if available:
        return {"status": "confirmed", "message": f"Visit scheduled for {request.date} at {request.time}"}
    else:
        return {"status": "unavailable", "suggestions": suggest_alternative_slots()}

__all__ = ["router"]  