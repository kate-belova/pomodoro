from dataclasses import dataclass

from repository import TaskRepository, TaskCached
from schemas.tasks import TaskSchema


@dataclass
class TaskService:
    task_repository: TaskRepository
    task_cached: TaskCached

    def get_tasks(self):
        if tasks := self.task_cached.get_tasks():
            return tasks

        tasks = self.task_repository.get_tasks()
        tasks_schema = [TaskSchema.model_validate(task) for task in tasks]
        self.task_cached.set_tasks(tasks_schema)
        return tasks
