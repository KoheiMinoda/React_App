from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class ToDo(BaseModel):
    title: str
    completed: bool = False

todos = []

@app.get("/todos/", response_model=List[ToDo])
async def get_todos():
    return todos

@app.post("/todos/", response_model=ToDo)
async def create_todo(todo: ToDo):
    todos.append(todo)
    return todo

@app.delete("/todos/{todo_id}", response_model=ToDo)
async def delete_todo(todo_id: int):
    if todo_id < 0 or todo_id >= len(todos):
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todos.pop(todo_id)

