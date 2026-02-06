from fastapi import HTTPException
from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        existing = self.repo.get_by_title(task_in.title)
        if existing:
            raise HTTPException(status_code=400, detail="Task with this title already exists")
        return self.repo.create(task_in)

def update_task_complete(self, task_id: int, task_in: TaskCreate):
    task = self.repo.update_task_complete(task_id, task_in)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task