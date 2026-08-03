import heapq

from dispatch.core.task import Task

class Scheduler:
    """Schedules tasks by priority"""

    def __init__(self) -> None:
        self._queue: list[tuple[int, int, Task]] = []

    def add_task(self, task: Task) -> None:
        heapq.heappush(
            self._queue,
            (-task.priority.value, task.id, task)
        )

    def next_task(self) -> Task:
        if not self._queue:
            raise IndexError("Scheduler is empty.")

        _, _, task = heapq.heappop(self._queue)

        return task

    def peek(self) -> Task:
        if not self._queue:
            raise IndexError("Scheduler is empty.")

        return self._queue[0][2]

    def __len__(self) -> int:
        return len(self._queue)