from datetime import datetime

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
