from datetime import datetime

tasks = []

def validate_task_title(title):
    return isinstance(title, str) and len(title.strip()) > 0


def validate_task_description(description):
    return isinstance(description, str) and len(description.strip()) > 0


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def add_task(title, description, due_date):
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index):
    index = index - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")


def view_pending_tasks():
    return [t for t in tasks if not t["completed"]]


def view_all_tasks():
    return tasks


def task_progress():
    if len(tasks) == 0:
        return 0
    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100


def display_tasks(tasks_list):
    if not tasks_list:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks_list, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} | {task['due_date']} | {status}")


def get_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        return None


def main():
    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = get_input("Enter choice: ")
        if choice is None:
            break

        if choice == "1":
            title = get_input("Title: ")
            if title is None:
                break
            description = get_input("Description: ")
            if description is None:
                break
            due_date = get_input("Due Date (YYYY-MM-DD): ")
            if due_date is None:
                break

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
            index_str = get_input("Enter task index to mark complete: ")
            if index_str is None:
                break
            try:
                index = int(index_str)
            except ValueError:
                print("Invalid task index.")
                continue
            mark_task_as_complete(index)

        elif choice == "3":
            display_tasks(view_pending_tasks())

        elif choice == "4":
            print(f"Progress: {task_progress():.2f}%")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
