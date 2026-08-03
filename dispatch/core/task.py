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