"""
Programming Lab 1 - Day 3
Function Design

Complete Tasks 5 and 6 in this file.

Today, follow the function design recipe:
1. State the purpose.
2. Identify parameter and return types.
3. Name and template the function.
4. Work examples by hand and write tests.
5. Complete the implementation.
6. Run all tests and debug as needed.
"""

from math import sqrt


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Return the Euclidean distance between the points
    (x1, y1) and (x2, y2).

    You may use sqrt() from the math module.
    """
    raise NotImplementedError("Complete Task 5: distance")


def triangle_perimeter(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    x3: float,
    y3: float,
) -> float:
    """
    Return the perimeter of the triangle formed by the three points.

    REQUIRED:
    Use the distance() function above.

    Do not duplicate the distance calculation inside this function.
    """
    raise NotImplementedError("Complete Task 6: triangle_perimeter")
