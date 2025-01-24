from fastapi import FastAPI, HTTPException
from typing import List, Optional
from src.sparc_demo.state.models import TodoItem
from src.sparc_demo.process.todo_manager import TodoManager

app = FastAPI(title="SPARC Todo API")

@app.post("/todos/", response_model=TodoItem)
async def create_todo(title: str, description: Optional[str] = None):
    return TodoManager.create_todo(title, description)

@app.get("/todos/", response_model=List[TodoItem])
async def list_todos():
    return TodoManager.list_todos()

@app.get("/todos/{todo_id}", response_model=TodoItem)
async def get_todo(todo_id: int):
    todo = TodoManager.get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=TodoItem)
async def update_todo(todo_id: int, title: str, description: Optional[str] = None, completed: bool = False):
    todo = TodoManager.update_todo(todo_id, title, description, completed)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    if not TodoManager.delete_todo(todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}

@app.post("/todos/{todo_id}/toggle", response_model=TodoItem)
async def toggle_todo(todo_id: int):
    todo = TodoManager.toggle_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
