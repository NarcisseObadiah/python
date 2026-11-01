import string
import sys


def count_chars(text: str) -> None:
    """Print the number of each kind of character in the text."""
    upper = sum(c.isupper() for c in text)
    lower = sum(c.islower() for c in text)
    punct = sum(c in string.punctuation for c in text)
    spaces = sum(c.isspace() for c in text)
    digits = sum(c.isdigit() for c in text)
    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Count the character categories of a string given as argument.

    If no argument is given, the text is read from the standard input.
    """
    try:
        args = sys.argv[1:]
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")
        if args:
            text = args[0]
        else:
            print("What is the text to count?")
            text = sys.stdin.readline()
        count_chars(text)
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()

# ---------------- TEST ----------------
# python3.10 building.py 'Hello World!'
#
# python3.10 building.py
# (then type: Hello World and press Enter)
#
# Or automatic stdin:
# printf 'Hello World!\n' | python3.10 building.py
# --------------------------------------
