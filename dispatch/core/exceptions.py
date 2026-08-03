class DispatchError(Exception):
    """Base expection for dispatch application."""

class DuplicateTaskError(DispatchError):
    """Raised when additing a task whose ID already exist."""

class TaskNotFoundError(DispatchError):
    """Raised when a requested task can't be found."""

class InvalidTaskError(DispatchError):
    """Raised when task data is invalid."""