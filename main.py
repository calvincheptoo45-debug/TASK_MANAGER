import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from task_utils import add_task, mark_task_as_complete, view_all_tasks, view_pending_tasks, task_progress
from validation import validate_task_title, validate_task_description, validate_due_date


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} | {task['due_date']} | {status}")


def main():
    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. Mark Task as Complete")
        print("5. View Progress")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")

            if not validate_task_title(title):
                print("Invalid title")
                continue
            if not validate_task_description(description):
                print("Invalid description")
                continue
            if not validate_due_date(due_date):
                print("Invalid date format")
                continue

            add_task(title, description, due_date)

        elif choice == "2":
            display_tasks(view_all_tasks())

        elif choice == "3":
            display_tasks(view_pending_tasks())

        elif choice == "4":
            display_tasks(view_all_tasks())
            index = int(input("Enter task index to mark complete: "))
            mark_task_as_complete(index)

        elif choice == "5":
            print(f"Progress: {task_progress():.2f}%")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
