def example_isclose():
    """
    Definition:
        math.isclose(a, b) returns True if two numbers a and b are approximately equal,
        considering both relative and absolute tolerances.

    Example: Using math.isclose() with absolute and relative tolerance

    Numbers:
        a = 2.45
        b = 2.45678

    Tolerances:
        Absolute tolerance (abs_tol) = 0.01
        Relative tolerance (rel_tol) = 0.001

    Step 1: Calculate actual difference
        abs(a - b) = abs(2.45 - 2.45678) = 0.00678

    Step 2: Calculate relative tolerance difference
        rel_tol * max(abs(a), abs(b)) = 0.001 * 2.45678 ≈ 0.00245678

    Step 3: Determine maximum allowed difference
        allowed_diff = max(relative_diff, abs_tol)
                     = max(0.00245678, 0.01) = 0.01

    Step 4: Compare actual difference with allowed difference
        0.00678 <= 0.01 → True

    Conclusion:
        math.isclose(a, b, rel_tol=0.001, abs_tol=0.01) returns True
        because the actual difference (0.00678) is less than the allowed maximum (0.01).

    """
    import math

    a = 2.45
    b = 2.45678
    abs_tol = 0.01
    rel_tol = 0.001

    result = math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)
    print(result)  # Output: True


example_isclose()
