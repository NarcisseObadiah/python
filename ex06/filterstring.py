import sys

from ft_filter import ft_filter


def filter_words(text: str, size: int) -> list:
    """Return the words of text whose length is greater than size."""
    words = [word for word in text.split()]
    return ft_filter(lambda word: len(word) > size, words)


def main():
    """Print the words of a string longer than a given integer."""
    try:
        args = sys.argv[1:]
        if len(args) != 2:
            raise AssertionError("the arguments are bad")
        try:
            size = int(args[1])
        except ValueError:
            raise AssertionError("the arguments are bad")
        print(filter_words(args[0], size))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()


# ---------------- TEST ----------------
# python3.10 filterstring.py 'Hello the World' 4
# python3.10 filterstring.py 'Hello the World' 99
# python3.10 filterstring.py 3 'Hello the World'
# python3.10 filterstring.py
#
# Expected:
# ['Hello', 'World']
# []
# AssertionError: the arguments are bad
# AssertionError: the arguments are bad
# --------------------------------------
