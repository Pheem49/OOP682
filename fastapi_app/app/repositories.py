from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Task, TaskCreate

class ITaskRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def create(self, task: TaskCreate) -> Task:
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def update_task_complete(self, task_id: int, task_in: TaskCreate) -> Optional[Task]:
        pass


class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks: List[Task] = []
        self.current_id = 1

    def get_all(self) -> List[Task]:
        return self.tasks

    def create(self, task_in: TaskCreate) -> Task:
        task = Task(id=self.current_id, **task_in.model_dump())
        self.tasks.append(task)
        self.current_id += 1
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task_complete(self, task_id: int, task_in: TaskCreate) -> Optional[Task]:
        task = self.get_by_id(task_id)
        if task:
            task.completed = task_in.completed
            return task
        return None


from sqlalchemy.orm import Session
from . import models_orm

class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(models_orm.TaskORM).all()

    def create(self, task_in: TaskCreate):
        db_task = models_orm.TaskORM(**task_in.model_dump())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_by_id(self, task_id: int):
        return self.db.query(models_orm.TaskORM).filter(models_orm.TaskORM.id == task_id).first()

    def update_task_complete(self, task_id: int, task_in: TaskCreate) -> Optional[Task]:
        db_task = self.get_by_id(task_id)
        if db_task:
            db_task.completed = task_in.completed
            self.db.commit()
            self.db.refresh(db_task)
        return db_task
