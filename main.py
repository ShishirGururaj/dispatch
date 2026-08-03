from dispatch.core.scheduler import Scheduler
from dispatch.core.task import Priority, Task


scheduler = Scheduler()

scheduler.add_task(Task(1, "Email", Priority.LOW))
scheduler.add_task(Task(2, "Backup", Priority.HIGH))
scheduler.add_task(Task(3, "Cleanup", Priority.MEDIUM))
scheduler.add_task(Task(4, "Database", Priority.HIGH))

while len(scheduler):
    print(scheduler.next_task())