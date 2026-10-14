# Task Tracker CLI

A command-line task manager written in Python. Add, update, delete, and list
tasks from the terminal. Tasks are saved in a JSON file, and the project uses
only the standard library, with nothing to install.

## Requirements

Python 3 (developed on 3.14).

## Usage

Run commands from the project folder:

```
python main.py add "Buy milk"
python main.py list
python main.py list --status done
python main.py mark 1 in-progress
python main.py mark 1 done
python main.py delete 1
```

Statuses: `todo`, `in-progress`, `done`. New tasks start as `todo`.

## How it works

| File | Job |
|------|-----|
| `main.py` | Entry point |
| `cli.py` | Reads the typed command and calls the right function |
| `tasks.py` | Task logic: add, find, update status, delete, filter |
| `storage.py` | Reads and writes `tasks.json` |

Each task is stored as `{"id": 1, "description": "Buy milk", "status": "todo"}`.

## Notes

- Tasks are saved in `tasks.json` in the folder where you run the command,
  so run it from the project folder to keep one task list.
- `tasks.json` is not committed to the repository.