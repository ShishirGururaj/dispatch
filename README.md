# Dispatch

A lightweight task dispatch system that demonstrates how to build a real, end-to-end application using **pure Python**.

Rather than relying on web frameworks or third-party libraries, Dispatch showcases Python's standard library and core language features to model common backend engineering concepts, including data modeling, persistence, priority scheduling, structured logging, concurrent execution, testing, and a command-line interface.

---

## Features

* Task management with validation
* Priority-based scheduling using `heapq`
* JSON-based persistence
* Structured application logging
* Execution decorators for tracing and timing
* Concurrent task execution with `ThreadPoolExecutor`
* Command-line interface with `argparse`
* Unit tests using `pytest`

---

## Architecture

```text
                   CLI (argparse)
                         │
                         ▼
                    TaskStore
                         │
                         ▼
                   TaskManager
                         │
                         ▼
                    Scheduler
                     (heapq)
                         │
                         ▼
                  TaskExecutor
             (ThreadPoolExecutor)
```

Each component has a single responsibility:

* **Task** – domain model representing a unit of work.
* **TaskManager** – manages the collection of tasks.
* **TaskStore** – persists tasks to disk using JSON.
* **Scheduler** – orders tasks by priority.
* **TaskExecutor** – executes scheduled tasks concurrently.
* **CLI** – provides the application's user interface.

---

## Project Structure

```text
dispatch/
│
├── dispatch/
│   ├── core/
│   │   ├── task.py
│   │   ├── task_manager.py
│   │   ├── scheduler.py
│   │   └── executor.py
│   │
│   ├── storage/
│   │   └── store.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   └── decorators.py
│   │
│   ├── exceptions/
│   └── data/
│
├── tests/
├── logs/
├── main.py
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/dispatch.git
cd dispatch
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Linux/macOS**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install pytest
```

---

## Usage

Add a task:

```bash
python main.py add --id 1 --name "Backup Database" --priority HIGH
```

List tasks:

```bash
python main.py list
```

Run scheduled tasks:

```bash
python main.py run
```

Run the test suite:

```bash
pytest
```

---

## Python Concepts Demonstrated

### Core Language

* Classes and object-oriented programming
* Dataclasses
* Enums
* Properties
* Type hints
* Custom exceptions

### Standard Library

* `argparse`
* `concurrent.futures`
* `datetime`
* `heapq`
* `json`
* `logging`
* `pathlib`
* `threading`
* `time`

### Engineering Concepts

* Separation of concerns
* Layered architecture
* JSON serialization
* Decorators
* Priority queues
* Concurrent execution
* Structured logging
* Command-line applications
* Unit testing

---

## Example Output

```text
INFO | Running task 2
INFO | Running task 4
INFO | Running task 3

INFO | Completed task 4
INFO | Completed task 2
INFO | Completed task 3
```

---

## Future Improvements

Potential enhancements include:

* Task retries and backoff
* Status transitions (Pending → Running → Completed)
* Configuration via environment variables
* SQLite persistence
* Task dependencies
* Scheduled execution based on time
* Colored CLI output
