from typing import Dict, List, Optional
from src.sparc_demo.state.models import TodoItem

class TodoStorage:
    def __init__(self):
        self.todos: Dict[int, TodoItem] = {}
        self.counter: int = 1

    def create(self, todo: TodoItem) -> TodoItem:
        todo.id = self.counter
        self.todos[self.counter] = todo
        self.counter += 1
        return todo

    def get(self, todo_id: int) -> Optional[TodoItem]:
        return self.todos.get(todo_id)

    def list(self) -> List[TodoItem]:
        return list(self.todos.values())

    def update(self, todo_id: int, todo: TodoItem) -> Optional[TodoItem]:
        if todo_id in self.todos:
            todo.id = todo_id
            self.todos[todo_id] = todo
            return todo
        return None

    def delete(self, todo_id: int) -> bool:
        if todo_id in self.todos:
            del self.todos[todo_id]
            return True
        return False

# Global storage instance
storage = TodoStorage()
