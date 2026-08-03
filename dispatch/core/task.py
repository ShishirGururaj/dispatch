from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
from .exceptions import InvalidTaskError

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    COMPLETED = auto()
    FAILED = auto()

@dataclass(slots=True)
class Task:
    id: int
    name: str
    priority: Priority
    status: Status = Status.PENDING
    retries: int = 0
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        """Validate and normalize task data after initialization."""
        
        if self.id <= 0:
            raise InvalidTaskError("Taks ID must be greater than zero (0).")

        self.name = self.name.strip()

        if not self.name:
            raise InvalidTaskError("Task Name can't be empty.")

        if self.retries < 0:
            raise InvalidTaskError("Retries can't be negative.")

    def start(self) -> None:
        """Mark the task as running."""
        self.status = Status.RUNNING

    def complete(self) -> None:
        """Mark the task as completed."""
        self.status = Status.COMPLETED

    def fail(self) -> None:
        """Mark the task as failed."""
        self.status = Status.FAILED

    def __str__(self) -> str:
        return (
            f"[{self.id}] "
            f"{self.name} "
            f"({self.priority.name}) - "
            f"{self.status.name}"
        )

    @property
    def is_pending(self) -> bool:
        return self.status == Status.PENDING

    @property
    def is_running(self) -> bool:
        return self.status == Status.RUNNING

    @property
    def is_completed(self) -> bool:
        return self.status == Status.COMPLETED

    @property
    def is_failed(self) -> bool:
        return self.status == Status.FAILED

    def __lt__(self, other: "Task") -> bool:
        return self.priority.value < other.priority.value
    