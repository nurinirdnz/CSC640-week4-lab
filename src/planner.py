"""A tiny study planner: helper functions for deadlines.

This is the code you will test in the Week 4 lab.
"""


def days_left(due, today):
    """Return how many days are left from today until the due date.

    A negative number means the task is overdue.
    """
    return (due - today).days


def is_urgent(due, today, limit=2):
    """Return True if the task is due within `limit` days.

    A task that is already overdue is not urgent. It is late.
    """
    left = days_left(due, today)
    return 0 <= left <= limit


def sort_by_due(tasks):
    """Return a new list of tasks, soonest due date first.

    Each task is a dictionary with the keys "title" and "due".
    """
    return sorted(tasks, key=lambda task: task["due"])


def completion_rate(done, total):
    """Return the percentage of tasks that are done, rounded to 1 decimal place.

    If there are no tasks, the rate is 0.0.
    """
    if total == 0:
        return 0.0
    return round(done / total * 100, 1)
