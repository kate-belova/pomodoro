from typing import Optional

from pydantic import BaseModel, ConfigDict, model_validator


class TaskSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    pomodoro_count: Optional[int] = None
    category_id: int

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode='after')
    def check_name_or_pomodoro_count_is_not_none(self):
        if self.name is None and self.pomodoro_count is None:
            raise ValueError('Name or pomodoro count is required')
        return self
