tasks = []

def add_task(title, description, due_date):
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")


def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    return pending


def view_all_tasks(tasks=tasks):
    return tasks


def task_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0
    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100
