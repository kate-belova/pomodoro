from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from dependencies import get_task_repository, get_task_service
from repository import TaskRepository
from schemas.tasks import TaskSchema
from service.task import TaskService

task_router = APIRouter(prefix='/tasks', tags=['tasks'])


@task_router.get('/', response_model=list[TaskSchema])
async def get_tasks(
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    return task_service.get_tasks()


@task_router.post('/', response_model=TaskSchema)
async def create_task(
    task: TaskSchema,
    task_repository: Annotated[TaskRepository, Depends(get_task_repository)],
):
    task_id = task_repository.create_task(task)
    task.id = task_id
    return task


@task_router.patch('/{task_id}', response_model=TaskSchema)
async def update_task_name(
    task_id: int,
    name: str,
    task_repository: Annotated[TaskRepository, Depends(get_task_repository)],
):
    return task_repository.update_task_name(task_id, name)


@task_router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    task_repository: Annotated[TaskRepository, Depends(get_task_repository)],
):
    task_repository.delete_task(task_id)
