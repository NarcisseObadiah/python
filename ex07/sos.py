import sys


def get_morse() -> dict:
    """Return the dictionary used to encode characters in Morse code."""
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
        "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
        "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
        "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
        "8": "---.. ", "9": "----. ",
    }
    return NESTED_MORSE


def encode(text: str) -> str:
    """Encode a text made of spaces and alphanumeric characters."""
    morse = get_morse()
    text = text.upper()
    if not all(char in morse for char in text):
        raise AssertionError("the arguments are bad")
    return "".join(morse[char] for char in text).rstrip()


def main():
    """Encode the string given as argument into Morse code."""
    try:
        args = sys.argv[1:]
        if len(args) != 1:
            raise AssertionError("the arguments are bad")
        print(encode(args[0]))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()

# ---------------- TEST ----------------
# python3.10 sos.py "sos"
# python3.10 sos.py 'h$llo'
# python3.10 sos.py
# python3.10 sos.py a b
#
# Expected:
# ... --- ...
# AssertionError: the arguments are bad
# AssertionError: the arguments are bad
# AssertionError: the arguments are bad
# --------------------------------------
