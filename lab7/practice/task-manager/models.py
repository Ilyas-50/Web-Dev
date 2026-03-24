class Task:
    def __init__(self, task_id: int, title: str, completed: bool = False):
        self.id = task_id
        self.title = title
        self.completed = completed
    
    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = ""
        if self.completed:
            status = "✅" 
        else:
            status = "❌"
        return f"[{self.id}] {self.title} {status}"

    def to_dict(self):
        return {
        "id": self.id,
        "title": self.title,
        "completed": self.completed
    }

    @classmethod #чтобы псиать Task.from_dict(ышав) - у же еще нет обьекта
    def from_dict(cls, data: dict):
        return cls(data["id"], data["title"], data["completed"])
    

class TaskManager:
    def __init__(self, tasks=None):
        if tasks != None:
            self.tasks = tasks
        else : self.tasks = []

    def _get_next_id(self):
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def add_task(self, title):
        task = Task(self._get_next_id(), title)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_completed()
                return True
        return False
    
    def delete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False