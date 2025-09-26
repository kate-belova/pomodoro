from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from database import Task
from schemas.tasks import TaskSchema


class TaskRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_tasks(self):
        tasks = self.db_session.execute(select(Task)).scalars().all()
        return tasks

    def get_task(self, task_id: int) -> Task | None:
        query = select(Task).where(Task.id == task_id)
        task = self.db_session.execute(query).scalar_one_or_none()
        return task

    def create_task(self, task_data: TaskSchema) -> int:
        task_model = Task(
            name=task_data.name,
            pomodoro_count=task_data.pomodoro_count,
            category_id=task_data.category_id,
        )

        self.db_session.add(task_model)
        self.db_session.commit()
        self.db_session.refresh(task_model)

        return task_model.id

    def update_task_name(self, task_id: int, name: str) -> None:
        query = (
            update(Task)
            .where(Task.id == task_id)
            .values(name=name)
            .returning(Task.id)
        )
        updated_task_id = self.db_session.execute(query).scalar_one_or_none()
        self.db_session.commit()
        return self.get_task(updated_task_id)

    def delete_task(self, task_id: int) -> None:
        query = delete(Task).where(Task.id == task_id)
        self.db_session.execute(query)
        self.db_session.commit()
