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
# TODO 2: is_urgent is True when the task is due tomorrow.
# TODO 3: is_urgent is True when the task is due in exactly 2 days (the limit).
# TODO 4: is_urgent is False when the task is overdue.
# TODO 5: sort_by_due puts the soonest task first.
# TODO 6: completion_rate returns 0.0 when there are no tasks.
# TODO 7: completion_rate(1, 3) returns 33.3.
