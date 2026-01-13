from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from utils import load_tasks, save_tasks

app = FastAPI(title="FastAPI Task Management System")

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.get("/")
def root():
    return {"message": "Task Management API is running"}

@app.get("/tasks", response_model=List[Task])
def get_tasks(completed: Optional[bool] = None):
    tasks = load_tasks()
    if completed is not None:
        tasks = [t for t in tasks if t["completed"] == completed]
    return tasks

@app.get("/tasks/stats")
def get_task_stats():
    tasks = load_tasks()
    total_tasks = len(tasks)
    completed_count = sum(1 for t in tasks if t["completed"])
    pending_count = total_tasks - completed_count
    completion_percentage = (completed_count / total_tasks * 100) if total_tasks > 0 else 0

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_count,
        "pending_tasks": pending_count,
        "completion_percentage": f"{completion_percentage:.2f}%"
    }

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_in: TaskCreate):
    tasks = load_tasks()
    
    if tasks:
        new_id = max(t["id"] for t in tasks) + 1
    else:
        new_id = 1
        
    new_task = {
        "id": new_id,
        "title": task_in.title,
        "description": task_in.description,
        "completed": task_in.completed
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskCreate):
    tasks = load_tasks()
    
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            updated_task = {
                "id": task_id,
                "title": task_update.title,
                "description": task_update.description,
                "completed": task_update.completed
            }
            tasks[i] = updated_task
            save_tasks(tasks)
            return updated_task
            
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()

    new_tasks = [t for t in tasks if t["id"] != task_id]
    
    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
        
    save_tasks(new_tasks)
    return {"message": "Task deleted successfully"}

@app.delete("/tasks")
def delete_all_tasks():
    save_tasks([])  # Overwrite with empty list
    return {"message": "All tasks deleted successfully"}