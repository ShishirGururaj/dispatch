from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto

class Priority(Enum):
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()

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
            raise ValueError("Taks ID must be greater than zero (0).")

        self.name = self.name.strip()

        if not self.name:
            raise ValueError("Task Name can't be empty.")

        if self.retries < 0:
            raise ValueError("Retries can't be negative.")

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