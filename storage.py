"""Reading and writing tasks to a JSON file."""

import json

FILE_NAME = "tasks.json"


def load_tasks(path=FILE_NAME):
    """Return all saved tasks as a list of dictionaries.

    Returns an empty list if the file doesn't exist yet or is empty.
    """
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # An empty or corrupted file should behave like a new start,
        # not crash the program.
        return []


def save_tasks(tasks, path=FILE_NAME):
    """Overwrite the file with the given list of tasks."""
    with open(path, "w") as f:
        json.dump(tasks, f, indent=4)