from pathlib import Path
from datetime import datetime
import json

from dispatch.core.task import Task, Priority, Status
from dispatch.core.task_manager import TaskManager


class TaskStore:
    """Handles saving and loading tasks."""

    def __init__(self, file_path: str = "dispatch/data/tasks.json") -> None:
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def _task_to_dict(self, task: Task) -> dict:
        return {
            "id": task.id,
            "name": task.name,
            "priority": task.priority.name,
            "status": task.status.name,
            "retries": task.retries,
            "created_at": task.created_at.isoformat(),
        }

    def _dict_to_task(self, data: dict) -> Task:
        return Task(
            id=data["id"],
            name=data["name"],
            priority=Priority[data["priority"]],
            status=Status[data["status"]],
            retries=data["retries"],
            created_at=datetime.fromisoformat(data["created_at"]),
        )

    def save(self, manager: TaskManager) -> None:
        """Save all tasks to disk."""

        tasks = [
            self._task_to_dict(task)
            for task in manager
        ]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)

    def load(self) -> TaskManager:
        """Load tasks from disk."""

        manager = TaskManager()

        if not self.file_path.exists():
            return manager

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            manager.add_task(self._dict_to_task(item))

        return manager