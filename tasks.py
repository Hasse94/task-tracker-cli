"""Task logic: creating and changing tasks. No file handling here."""

VALID_STATUSES = ("todo", "in-progress", "done")


def check_status(status):
    """Raise ValueError if the status isn't one of VALID_STATUSES."""
    if status not in VALID_STATUSES:
        raise ValueError(f"Status must be one of: {', '.join(VALID_STATUSES)}")


def find_task(tasks, task_id):
    """Return the task with the given id, or None if there isn't one."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def mark_status(tasks, task_id, status):
    """Set a task's status and return the task, or None if the id doesn't exist.

    Raises ValueError if the status isn't one of VALID_STATUSES.
    """
    check_status(status)
    task = find_task(tasks, task_id)
    if task is None:
        return None
    task["status"] = status
    return task


def delete_task(tasks, task_id):
    """Remove the task with the given id. Return True if removed, False if not."""
    task = find_task(tasks, task_id)
    if task is None:
        return False
    tasks.remove(task)
    return True


def next_id(tasks):
    """Return an unused id: one higher than the largest existing id."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(tasks, description):
    """Add a new task with status 'todo' to the list and return it."""
    task = {
        "id": next_id(tasks),
        "description": description,
        "status": "todo",
    }
    tasks.append(task)
    return task


def list_tasks(tasks, status=None):
    """Return a list of tasks, optionally filtered by status."""
    if status is not None:
        check_status(status)
        return [task for task in tasks if task["status"] == status]
    return tasks