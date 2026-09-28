"""
Programming Lab 1 - Day 2 Tests

Task 3 begins with provided tests for double().
One or more tests should fail before you correct the implementation.

Task 4 requires you to write your own tests for clamp().
"""

from day2 import double, clamp


# ---------------------------------------------------------------------------
# Task 3 - Testing and Debugging Existing Code
# ---------------------------------------------------------------------------

def test_double_zero():
    assert double(0) == 0


def test_double_positive_value():
    assert double(4) == 8


def test_double_negative_value():
    assert double(-3) == -6


# ---------------------------------------------------------------------------
# Task 4 - clamp
# ---------------------------------------------------------------------------

# TODO: Write multiple unit tests for clamp below.
#
# At minimum, include:
# - a value below the lower bound
# - a value between the bounds
# - a value above the upper bound
# - a value equal to the lower bound
# - a value equal to the upper bound
