from dispatch.core.task import Task, Priority

def test_create_task():
    task = Task(
        id = 1,
        name = "Backup",
        priority=Priority.HIGH,
    )

    assert task.id == 1
    assert task.name == "Backup"
    assert task.priority == Priority.HIGH