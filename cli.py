"""Command-line interface: turns typed commands into calls to the task functions."""

import argparse

import storage
import tasks


def build_parser():
    """Return an ArgumentParser for the program."""
    parser = argparse.ArgumentParser(description="Task tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add a task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")

    # List tasks
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--status",
        choices=tasks.VALID_STATUSES,
        help="Filter tasks by status",
    )

    # Change a task's status
    mark_parser = subparsers.add_parser("mark", help="Change a task's status")
    mark_parser.add_argument("task_id", type=int, help="ID of the task")
    mark_parser.add_argument("status", choices=tasks.VALID_STATUSES, help="New status")

    # Delete a task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")
    return parser


def run():
    """Read the command, run it, and save the tasks if they changed."""
    parser = build_parser()
    args = parser.parse_args()

    tasks_list = storage.load_tasks()

    if args.command == "add":
        task = tasks.add_task(tasks_list, args.description)
        storage.save_tasks(tasks_list)
        print(f"Added task {task['id']}: {task['description']}")

    elif args.command == "list":
        filtered_tasks = tasks.list_tasks(tasks_list, status=args.status)
        if not filtered_tasks:
            print("No tasks found.")
        for task in filtered_tasks:
            print(f"{task['id']}: {task['description']} [{task['status']}]")

    elif args.command == "mark":
        task = tasks.mark_status(tasks_list, args.task_id, args.status)
        if task is None:
            print(f"No task with ID {args.task_id}")
        else:
            storage.save_tasks(tasks_list)
            print(f"Task {task['id']} marked as {task['status']}")

    elif args.command == "delete":
        success = tasks.delete_task(tasks_list, args.task_id)
        if not success:
            print(f"No task with ID {args.task_id}")
        else:
            storage.save_tasks(tasks_list)
            print(f"Deleted task {args.task_id}")