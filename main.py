import argparse

from dispatch.core.task_manager import TaskManager
from dispatch.core.task import Task, Priority
from dispatch.core.scheduler import Scheduler
from dispatch.core.executor import TaskExecutor
from dispatch.storage.store import TaskStore

def main():

    parser = argparse.ArgumentParser(
        description="Dispatch Task Manager"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    add_parser = subparsers.add_parser(
        "add",
        help="Add a task",
    )

    add_parser.add_argument("--id", type = int, required=True)
    add_parser.add_argument("--name", required=True)
    add_parser.add_argument(
        "--priority",
        choices=["LOW", "MEDIUM", "HIGH"],
        required=True,
    )
    subparsers.add_parser(
        "list",
        help="List all tasks",
    )

    subparsers.add_parser(
        "run",
        help="Run scheduled tasks",
    )

    args = parser.parse_args()

    store = TaskStore()
    manager = store.load()

    if args.command == "add":
        task = Task(
            id=args.id,
            name=args.name,
            priority=Priority[args.priority],
        )

        manager.add_task(task)

        store.save(manager)

        print("Task added.")

    elif args.command == "list":
        for task in manager:
            print(task)

    elif args.command == "run":
        scheduler = Scheduler()

        for task in manager:
            scheduler.add_task(task)

        executor = TaskExecutor()

        executor.run(scheduler)

if __name__ == "__main__":
    main()