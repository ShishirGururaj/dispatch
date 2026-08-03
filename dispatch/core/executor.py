from concurrent.futures import ThreadPoolExecutor

from dispatch.core.scheduler import Scheduler
from dispatch.core.task import Task
from dispatch.utils.logger import logger

from time import sleep
import random

class TaskExecutor:
    """Executes scheduled tasks concurrently"""

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers

    def execute_task(self, task: Task) -> None:
        logger.info("Running task %s", task.id)

        sleep(random.uniform(0.5, 2))

        logger.info("Completed task %s", task.id)

    def run(self, scheduler: Scheduler) -> None:
        with ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:

            while len(scheduler):
                executor.submit(
                    self.execute_task,
                    scheduler.next_task()
                )