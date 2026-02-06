from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        return self.repo.create(task_in)

    def update_task_complete(self, task_id: int, task_in: TaskCreate):
        return self.repo.update_task_complete(task_id, task_in)
