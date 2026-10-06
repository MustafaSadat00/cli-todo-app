"""A simple command-line to-do app that saves tasks to a JSON file."""

import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks():
    """Load tasks from the JSON file. Returns an empty list if none exist."""
    if not TASKS_FILE.exists():
        return []
    try:
        with TASKS_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Warning: could not read tasks.json, starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save the task list to the JSON file."""
    with TASKS_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def show_tasks(tasks):
    """Print all tasks with their status."""
    if not tasks:
        print("\nNo tasks yet. Add one!")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"  {i}. [{mark}] {task['title']}")


def choose_task(tasks, action):
    """Ask the user for a task number. Returns a valid index or None."""
    if not tasks:
        print("\nThere are no tasks.")
        return None
    show_tasks(tasks)
    raw = input(f"\nNumber of the task to {action}: ").strip()
    if not raw.isdigit() or not 1 <= int(raw) <= len(tasks):
        print("Invalid number.")
        return None
    return int(raw) - 1


def add_task(tasks):
    title = input("New task: ").strip()
    if not title:
        print("A task cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: {title}")


def complete_task(tasks):
    index = choose_task(tasks, "complete")
    if index is None:
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f"Completed: {tasks[index]['title']}")


def delete_task(tasks):
    index = choose_task(tasks, "delete")
    if index is None:
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted: {removed['title']}")


def main():
    tasks = load_tasks()
    actions = {
        "1": ("Add task", add_task),
        "2": ("Show tasks", lambda t: show_tasks(t)),
        "3": ("Complete task", complete_task),
        "4": ("Delete task", delete_task),
    }

    while True:
        print("\n=== To-Do App ===")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("5. Quit")

        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        if choice in actions:
            actions[choice][1](tasks)
        else:
            print("Invalid option, please choose 1-5.")


if __name__ == "__main__":
    main()
