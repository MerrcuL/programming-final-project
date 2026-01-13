import json
import os
from typing import List

# Constants
TASKS_FILE = "tasks.txt"

def load_tasks() -> List[dict]:
    if not os.path.exists(TASKS_FILE):
        return []
    
    tasks = []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                try:
                    tasks.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return tasks

def save_tasks(tasks: List[dict]):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(json.dumps(task, ensure_ascii=False) + "\n")
            