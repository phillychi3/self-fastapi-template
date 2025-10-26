from fastapi import APIRouter
from pydantic import BaseModel, Field

from worker.tasks import countdown_task

worker_router = APIRouter()


class TaskRequest(BaseModel):
    seconds: int = Field(default=10, description="countdown seconds")


class TaskResponse(BaseModel):
    task_id: str = Field(..., description="task id")
    message: str = Field(..., description="task message")


@worker_router.post("/start-countdown", response_model=TaskResponse)
async def start_countdown(request: TaskRequest):
    message = countdown_task.send(request.seconds)
    return TaskResponse(task_id=message.message_id, message=f"Countdown task started for {request.seconds} seconds")
