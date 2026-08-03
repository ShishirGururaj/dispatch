from dispatch.core.scheduler import Scheduler
from dispatch.core.task import Task, Priority

def test_scheduler_priority_order():
    scheduler = Scheduler()

    scheduler.add_task(
        Task(id=1, name="Low", priority=Priority.LOW)
    )

    scheduler.add_task(
        Task(id=2, name="High", priority=Priority.HIGH)
    )

    scheduler.add_task(
        Task(id=3, name="Medium", priority=Priority.MEDIUM)
    )

    assert scheduler.next_task().id == 2
    assert scheduler.next_task().id == 3
    assert scheduler.next_task().id == 1