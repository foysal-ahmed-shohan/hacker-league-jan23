from datetime import datetime
from typing import List, Optional
from src.sparc_demo.state.models import TodoItem
from src.sparc_demo.resource.storage import storage

class TodoManager:
    @staticmethod
    def create_todo(title: str, description: Optional[str] = None) -> TodoItem:
        todo = TodoItem(
            title=title,
            description=description,
            created_at=datetime.now()
        )
        return storage.create(todo)

    @staticmethod
    def get_todo(todo_id: int) -> Optional[TodoItem]:
        return storage.get(todo_id)

    @staticmethod
    def list_todos() -> List[TodoItem]:
        return storage.list()

    @staticmethod
    def update_todo(todo_id: int, title: str, description: Optional[str] = None, completed: bool = False) -> Optional[TodoItem]:
        existing_todo = storage.get(todo_id)
        if not existing_todo:
            return None
        
        updated_todo = TodoItem(
            id=todo_id,
            title=title,
            description=description,
            completed=completed,
            created_at=existing_todo.created_at,
            updated_at=datetime.now()
        )
        return storage.update(todo_id, updated_todo)

    @staticmethod
    def delete_todo(todo_id: int) -> bool:
        return storage.delete(todo_id)

    @staticmethod
    def toggle_todo(todo_id: int) -> Optional[TodoItem]:
        todo = storage.get(todo_id)
        if not todo:
            return None
        
        todo.completed = not todo.completed
        todo.updated_at = datetime.now()
        return storage.update(todo_id, todo)
