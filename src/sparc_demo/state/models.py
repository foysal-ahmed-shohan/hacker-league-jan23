from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoItem(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
