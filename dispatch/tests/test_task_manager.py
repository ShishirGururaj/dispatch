import pytest

from dispatch.core.task import Task, Priority
from dispatch.core.task_manager import TaskManager
from dispatch.core.exceptions import DuplicateTaskError


def test_add_task():
    manager = TaskManager()
    task = Task(id=1, name="Backup", priority=Priority.HIGH,)

    manager.add_task(task)

    assert len(manager) == 1


def test_duplicate_task():
    manager = TaskManager()
    task = Task(id=1, name="Backup", priority=Priority.HIGH,)

    manager.add_task(task)

    with pytest.raises(DuplicateTaskError):
        manager.add_task(task)