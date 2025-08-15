import sys
from datetime import date, datetime

import inflect


def main():
    date_of_birth = input("Date of Birth: ")
    if not is_valid_date(date_of_birth):
        sys.exit("Invalid date")
    minutes = calculate_minutes_lived(date_of_birth)

    p = inflect.engine()
    minutes_str = p.number_to_words(
        minutes,  # type: ignore
        andword="",
    ).capitalize()  # type: ignore
    print(f"{minutes_str} minutes")


def is_valid_date(date_str: str) -> bool:
    """Return True if date_str matches YYYY-MM-DD format, else False."""
    try:
        datetime.strptime(
            date_str, "%Y-%m-%d"
        )  # return a datetimefrom a string according to given format
        return True
    except ValueError:
        return False


def calculate_minutes_lived(date_str):
    """Return the amount of time since date of birth in minutes."""
    birth_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    today = date.today()
    days_lived = (today - birth_date).days
    return days_lived * 24 * 60


if __name__ == "__main__":
    main()
