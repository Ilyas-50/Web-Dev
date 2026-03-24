import json
import os
from models import Task

def load_tasks(filename):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        data = json.load(file)

    tasks = []
    for item in data:
        task = Task.from_dict(item)
        tasks.append(task)
    return tasks

def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        json.dump([task.to_dict() for task in tasks], file)