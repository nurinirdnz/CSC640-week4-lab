from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


# This test is already written for you. Read it, then run pytest.
def test_days_left_counts_days_until_due():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == 3


# Now write the tests below. Use the same three steps: Arrange, Act, Assert.

# TODO 1: days_left is negative when the task is overdue.
def test_days_left_when_overdue():
    today = date(2026, 10, 19)
    due = date(2026, 10, 17)
    result = days_left(due, today)
    assert result == -2


# TODO 2: is_urgent is True when the task is due tomorrow.
def test_is_urgent_when_due_tomorrow():
    today = date(2026, 10, 19)
    due = date(2026, 10, 20)
    assert is_urgent(due, today) is True


# TODO 3: is_urgent is True when due in exactly 2 days.
def test_is_urgent_when_due_in_two_days():
    today = date(2026, 10, 19)
    due = date(2026, 10, 21)
    assert is_urgent(due, today) is True


# TODO 4: is_urgent is False when overdue.
def test_is_urgent_when_overdue():
    today = date(2026, 10, 19)
    due = date(2026, 10, 18)
    assert is_urgent(due, today) is False


# TODO 5: sort_by_due puts the soonest task first.
def test_sort_by_due_soonest_first():
    tasks = [
        {"title": "Task A", "due": date(2026, 10, 22)},
        {"title": "Task B", "due": date(2026, 10, 20)}
    ]
    result = sort_by_due(tasks)
    assert result[0]["title"] == "Task B"


# TODO 6: completion_rate returns 0.0 when there are no tasks.
def test_completion_rate_no_tasks():
    assert completion_rate(0, 0) == 0.0


# TODO 7: completion_rate(1, 3) returns 33.3.
def test_completion_rate_one_of_three():
    assert completion_rate(1, 3) == 33.3
