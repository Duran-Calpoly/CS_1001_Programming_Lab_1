"""
Programming Lab 1 - Day 2
Debugging and Program Reasoning

Complete Tasks 3 and 4 in this file.

IMPORTANT:
The function double() below is intentionally incorrect.
Do not change it until you have:
1. run the provided tests,
2. identified the failing test,
3. compared expected and actual values, and
4. followed execution using the debugger.
"""


def double(n: int) -> int:
    """
    Return twice the value of n.

    This starter implementation contains a bug.
    """
    result = n * n
    return result


def clamp(value: float, lower: float, upper: float) -> float:
    """
    Return value constrained to the inclusive range [lower, upper].

    You may assume lower <= upper.

    Required behavior:
    - return lower when value is less than lower
    - return upper when value is greater than upper
    - return value otherwise
    """
    raise NotImplementedError("Complete Task 4: clamp")
