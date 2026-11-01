import sys


def parity(number: int) -> str:
    """Return the parity message for the given integer."""
    return "I'm Even." if number % 2 == 0 else "I'm Odd."


def main():
    """Check whether the number given as argument is odd or even."""
    try:
        args = sys.argv[1:]
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")
        if not args:
            return
        try:
            number = int(args[0])
        except ValueError:
            raise AssertionError("argument is not an integer")
        print(parity(number))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()


# ---------------- TEST ----------------
# python3.10 whatis.py 14
# python3.10 whatis.py -5
# python3.10 whatis.py
# python3.10 whatis.py 0
# python3.10 whatis.py 'Hi!'
# python3.10 whatis.py 13 5
#
# Expected:
# I'm Even.
# I'm Odd.
# I'm Even.
# AssertionError: argument is not an integer
# AssertionError: more than one argument is provided
# --------------------------------------
