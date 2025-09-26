from fastapi import Depends
from sqlalchemy.orm import Session

from cache import get_redis_connection
from database.database import get_db
from repository import TaskRepository, TaskCached
from service import TaskService


def get_task_repository(db: Session = Depends(get_db)) -> TaskRepository:
    return TaskRepository(db_session=db)


def get_task_cached_repository() -> TaskCached:
    redis_connection = get_redis_connection()
    return TaskCached(redis_connection)


def get_task_service(
    task_repository: TaskRepository = Depends(get_task_repository),
    task_cached: TaskCached = Depends(get_task_cached_repository),
) -> TaskService:
    return TaskService(
        task_repository=task_repository,
        task_cached=task_cached,
    )
