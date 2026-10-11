"""Reading and writing tasks to a JSON file."""

import json

FILE_NAME = "tasks.json"


def load_tasks():
    """Return all saved tasks as a list of dictionaries.

    Returns an empty list if the file doesn't exist yet or is empty.
    """
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # An empty or corrupted file should behave like a new start,
        # not crash the program.
        return []


def save_tasks(tasks):
    """Overwrite the file with the given list of tasks."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)