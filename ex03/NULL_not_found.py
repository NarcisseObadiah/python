def NULL_not_found(object: any) -> int:
    """Print the type of a "Null" like object.

    Return 0 if the object is one of the NULL types, 1 otherwise.
    """
    kind = type(object)
    if object is None:
        print("Nothing:", object, kind)
    elif kind is float and object != object:
        print("Cheese:", object, kind)
    elif kind is int and object == 0:
        print("Zero:", object, kind)
    elif kind is str and object == "":
        print("Empty:", kind)
    elif kind is bool and object is False:
        print("Fake:", object, kind)
    else:
        print("Type not Found")
        return 1
    return 0


def main() -> None:
    """Running this file alone must print nothing."""
    return


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass

# ---------------- TEST ----------------
# python3.10 NULL_not_found.py
# (should print nothing)
#
# python3.10 -c "from NULL_not_found import NULL_not_found as f; \
# Nothing=None; Garlic=float('NaN'); Zero=0; Empty=''; Fake=False; \
# f(Nothing); f(Garlic); f(Zero); f(Empty); f(Fake); print(f('Brian'))"
#
# Expected:
# Nothing: None <class 'NoneType'>
# Cheese: nan <class 'float'>
# Zero: 0 <class 'int'>
# Empty: <class 'str'>
# Fake: False <class 'bool'>
# Type not Found
# 1
# --------------------------------------
