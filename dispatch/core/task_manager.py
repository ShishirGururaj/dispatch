from __future__ import annotations
from .task import Task

class TaskManager:
    """Manages the lifecycle of tasks"""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}

    def add_task(self, task: Task) -> None:
        if task.id in self._tasks:
            raise ValueError(f"Task with ID {task:id} already exists.")

        self._tasks[task.id] = task

    def get_task(self, task_id: int) -> Task:
        try:
            return self._tasks[task_id]
        except KeyError:
            raise ValueError(f"No task found with ID {task_id}.")

    def remove_task(self, task_id: int) -> None:
        if task_id not in self._tasks:
            raise ValueError(f"No task found with ID {task_id}.")

        del self._tasks[task_id]

    def list_tasks(self) -> list[Task]:
        return list(self._tasks.values())

    def __len__(self) -> int:
        """Return number of tasks"""
        return len(self._tasks)

    def __contains__(self, task_id: int) -> bool:
        """Check whether a task exists"""
        return task_id in self._tasks

    def __iter__(self):
        """Iterate over all tasks"""
        return iter(self._tasks.values())