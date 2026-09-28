# Programming Lab 1: Developing and Testing Functions

This lab is completed over three class meetings.

You will use **GitHub Codespaces** as your programming environment instead of Google Colab.

> **This is not a Git lab.**
> You are not required to commit, push, create branches, or submit work through GitHub.
> GitHub Codespaces is being used as your browser-based programming environment.

There is **nothing to submit to Canvas**. Completion is recorded through daily instructor sign-offs.

---

## Files

| Day | Functions | Tests |
|---|---|---|
| Day 1 | `day1.py` | `test_1.py` |
| Day 2 | `day2.py` | `test_2.py` |
| Day 3 | `day3.py` | `test_3.py` |

---

# Day 1 — Testing and Unit Testing

## Setup: GitHub Codespaces

1. Sign in to GitHub.
2. Open the public Programming Lab 1 repository provided by your instructor.
3. Click **Code**.
4. Select **Codespaces**.
5. Create a new Codespace.
6. Wait for Visual Studio Code to load in your browser.
7. Open:
   - `day1.py`
   - `test_1.py`

Write today's functions in `day1.py` and today's tests in `test_1.py`.

---

## Task 1 — `absolute_value`

Develop a function named:

```python
absolute_value
```

The function must:

- take one parameter of type `float`;
- return the absolute value of the argument as a `float`;
- **not** use Python's predefined `abs` function.

### Testing

Write multiple unit tests.

At minimum, consider:

- a positive value;
- a negative value;
- zero.

### Questions to Consider

- Which inputs require the function to change the value?
- Which inputs may already have the desired value?
- Why is zero useful to test?

---

## Task 2 — `smallest`

Develop a function named:

```python
smallest
```

The function must:

- take two parameters of type `float`;
- return the smaller value;
- return that value when the two arguments are equal;
- **not** use Python's predefined `min` function.

### Testing

Your tests should include cases where:

- the first argument is smaller;
- the second argument is smaller;
- the arguments are equal.

### Questions to Consider

- Why is testing only one ordering of the arguments insufficient?
- Why is the equal-values case useful to test?

---

## Day 1 Sign-Off

Show an instructor:

- your working GitHub Codespace;
- your implementation of `absolute_value`;
- multiple tests for `absolute_value`;
- your implementation of `smallest`;
- multiple tests for `smallest`;
- all Day 1 tests running successfully.

Be prepared to explain why one of your tests represents a meaningfully different category of input.

---

# Day 2 — Debugging and Program Reasoning

Open:

- `day2.py`
- `test_2.py`

Today, begin by investigating code that does **not** behave according to its specification.

Do not randomly change code until the tests pass.

Use this workflow:

1. **Reproduce** the problem.
2. **Predict** what should happen.
3. **Observe** what actually happens.
4. **Compare** expected and actual execution.
5. **Correct** the problem.
6. **Retest** the complete test suite.

---

## Task 3 — Testing and Debugging Existing Code

The starter code contains a function named:

```python
double
```

The function is intended to return twice its argument.

The provided implementation contains a bug.

### Part A — Run the Tests

Run the provided tests in `test_2.py`.

At least one test should fail.

Before changing the code, identify:

1. Which test failed?
2. What value was expected?
3. What value was actually returned?
4. Which assertion detected the failure?

### Part B — Debug the Failing Test

Run the failing test using the debugger.

Place a breakpoint at the beginning of the failing test and follow execution into `double`.

Observe:

- the value passed to the function;
- the value bound to the parameter;
- the statements executed;
- the value returned.

Determine where the program's actual behavior differs from its required behavior.

### Part C — Correct and Retest

Once you understand the cause of the problem:

1. correct the implementation;
2. rerun the previously failing test;
3. run **all** tests again.

### Questions to Consider

- Why should the complete test suite be rerun after changing a function?
- Would one passing test prove that a function is correct for every possible input?

---

## Task 4 — `clamp`

Develop a function named:

```python
clamp
```

The function takes three parameters of type `float`:

```text
value
lower
upper
```

You may assume:

```python
lower <= upper
```

The function must:

- return `lower` when `value` is less than `lower`;
- return `upper` when `value` is greater than `upper`;
- return `value` otherwise.

### Testing

At minimum, test:

- a value below the lower bound;
- a value between the bounds;
- a value above the upper bound;
- a value equal to the lower bound;
- a value equal to the upper bound.

### Questions to Consider

- How many meaningfully different behaviors does this function have?
- Why are the exact boundary values useful tests?
- What kinds of problems might remain hidden if you tested only values between the bounds?

If a test fails, apply the same debugging process used in Task 3.

---

## Day 2 Sign-Off

Show an instructor:

- the failure produced by the original `double` implementation;
- the expected and actual values from the failed test;
- your ability to follow execution from the test into the function using the debugger;
- the corrected `double` function;
- your implementation of `clamp`;
- tests covering the different behaviors and boundary cases of `clamp`;
- all Day 2 tests running successfully.

Be prepared to explain how the failed test helped you identify the problem.

---

# Day 3 — Function Design

Open:

- `day3.py`
- `test_3.py`

Today, organize the activities from the previous two days into a deliberate function-design process.

## Function Design Recipe

For each function:

1. **State the purpose.**
   - What does the function compute?
   - What information does it receive?
   - What does it return?

2. **Identify the data representation.**
   - What are the parameter types?
   - What is the return type?

3. **Name and template the function.**
   - Write the definition, parameters, and return type.

4. **Work examples by hand and write tests.**
   - Determine expected results for representative inputs before completing the implementation.

5. **Complete the implementation.**

6. **Run all tests.**
   - If a test fails, compare expected and actual behavior, correct the implementation, and rerun the tests.

The goal is to move from:

**problem → examples → tests → implementation**

rather than immediately beginning with the function body.

---

## Task 5 — `distance`

Develop a function named:

```python
distance
```

The function takes four parameters of type `float`:

```text
x1
y1
x2
y2
```

These values represent two points:

```text
(x1, y1)
(x2, y2)
```

The function must return the Euclidean distance between the points as a `float`.

Use the distance formula:

```text
sqrt((x2 - x1)^2 + (y2 - y1)^2)
```

You may use `sqrt` from Python's `math` module.

### Testing

Consider tests involving:

- two different points;
- the same point twice;
- negative coordinates;
- points where only one coordinate differs;
- reversing the order of the two points.

### Questions to Consider

- What should the distance from a point to itself be?
- Should reversing the two points change the result?
- How could a test check that property?

---

## Task 6 — `triangle_perimeter`

Develop a function named:

```python
triangle_perimeter
```

The function takes six parameters of type `float`:

```text
x1
y1
x2
y2
x3
y3
```

These values represent three points.

The function must return the perimeter of the triangle formed by those points.

### Required Design

Your implementation must use the `distance` function from Task 5.

**Do not duplicate the distance calculation inside `triangle_perimeter`.**

### Testing

At minimum, include:

- a triangle whose side lengths you can determine independently;
- a triangle located somewhere else in the coordinate system;
- another triangle with known side lengths.

### Questions to Consider

- Which pairs of points form the three sides?
- What arguments should be passed to each call to `distance`?
- Why is using `distance` preferable to copying its implementation?
- If a problem were discovered in `distance`, what advantage does this design provide?

---

## Day 3 / Final Sign-Off

Show an instructor:

- your implementation of `distance`;
- multiple meaningful tests for `distance`;
- your implementation of `triangle_perimeter`;
- multiple meaningful tests for `triangle_perimeter`;
- `triangle_perimeter` using `distance`;
- all Day 3 tests running successfully;
- completed sign-offs for Days 1 and 2.

Be prepared to explain how you applied the design recipe to one of today's functions.

There is **nothing to submit to Canvas**.

---

# After Final Sign-Off

Only after your instructor completes your final sign-off:

1. return to your GitHub Codespaces page;
2. locate the Codespace for Programming Lab 1;
3. open the `...` menu;
4. select **Delete**;
5. confirm the deletion.

Do not delete the Codespace before receiving the final sign-off.
