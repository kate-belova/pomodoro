import json

from redis import Redis

from schemas.tasks import TaskSchema


class TaskCached:
    def __init__(self, redis: Redis):
        self.redis = redis

    def get_tasks(self) -> list[TaskSchema]:
        with self.redis as redis:
            tasks_json = redis.lrange('tasks', 0, -1)
            return [
                TaskSchema.model_validate(json.loads(task.decode('utf-8')))
                for task in tasks_json
            ]

    def set_tasks(self, tasks: list[TaskSchema]):
        tasks_json = [task.model_dump_json() for task in tasks]
        with self.redis as redis:
            self.redis.lpush('tasks', *tasks_json)
