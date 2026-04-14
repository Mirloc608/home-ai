from fastapi import APIRouter
from core.cognition.router import route_task

router = APIRouter()


@router.post("/task")
async def run_task(payload: dict):
    """
    Entry point for all Home AI requests.
    """
    result = await route_task(payload)
    return {"result": result}
