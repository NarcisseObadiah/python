import time
from datetime import datetime


def main() -> None:
    """Print epoch seconds with formatting + current date like 'Oct 21 2022'."""
    seconds = time.time()
    print(
        "Seconds since January 1, 1970:",
        f"{seconds:,.4f} or {seconds:.2e} in scientific notation",
    )
    print(datetime.now().strftime("%b %d %Y"))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # no uncaught exceptions
        pass

# ---------------- TEST ----------------
# python3.10 format_ft_time.py
# Expected:
# Seconds since January 1, 1970: ...
# todays date printed 
# --------------------------------------
