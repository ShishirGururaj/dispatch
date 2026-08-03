from pathlib import Path

from dispatch.core.task import Task, Priority
from dispatch.core.task_manager import TaskManager
from dispatch.storage.store import TaskStore

def test_save_and_load(tmp_path: Path):
    file_path = tmp_path / "tasks.json"

    store = TaskStore(file_path)

    manager = TaskManager()
    manager.add_task(Task(id=1, name="Backup", priority=Priority.HIGH,))

    store.save(manager)

    loaded = store.load()

    assert len(loaded) == 1
    assert next(iter(loaded)).name == "Backup"

