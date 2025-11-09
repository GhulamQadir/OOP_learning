from math import isclose


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

    # Example 1: Using larger tolerances
    a = 2.45
    b = 2.45678

    abs_tol = 0.01
    rel_tol = 0.001

    result = isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)
    print(result)  # Output: True
    # Explanation:
    # abs(a - b) = 0.00678
    # rel_tol * max(a,b) = 0.001 * 2.45678 = 0.00245678
    # max(0.01, 0.00245678) = 0.01
    # Since 0.00678 <= 0.01 → returns True

    #  Example 2: Using very small tolerances
    a = 2.45
    b = 2.45678
    abs_tol = 1e-5  # = 0.00001
    rel_tol = 1e-5  # = 0.00001

    result = isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)
    print(result)  # Output: False
    # Explanation:
    # abs(a - b) = 0.00678
    # rel_tol * max(a,b) = 1e-5 * 2.45678 = 0.0000245678
    # max(0.00001, 0.0000245678) = 0.0000245678
    # Since 0.00678 > 0.0000245678 → returns False


example_isclose()

"""
Logic:
    abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

Defaults:
    rel_tol = 1e-09 (always active unless overridden)
    abs_tol = 0.0   (always active unless overridden)

Notes:
    - If only abs_tol is given → rel_tol = 1e-09 (default)
    - If only rel_tol is given → abs_tol = 0.0 (default)
    - If neither is given → uses both defaults
"""
