import datetime


def main():
    """
    Prompt for a date and output that same date in YYYY-MM-DD format.
    """
    date = get_valid_date()
    if date:
        print_reformatted_date(date)
    else:
        print("Invalid date format. Please enter a valid date.")


def get_valid_date():
    """
    Prompts the user for a date and validates its format.
    Returns the date if valid, otherwise returns None.
    """
    while True:
        try:
            date_str = input("Date: ").strip()
            if date_str.lower() == "q":
                return None
            date = parse_date(date_str)
            return date
        except ValueError:
            print("Invalid date format. ", end="")
            print("Please enter the date in MM/DD/YYYY or Month Day, Year format.")


def parse_date(date_str):
    """
    Parses the date string in MM/DD/YYYY or Month Day, Year format.
    Returns a datetime object if valid, otherwise raises a ValueError.
    """
    formats = ["%m/%d/%Y", "%B %d, %Y"]
    for fmt in formats:
        try:
            date = datetime.datetime.strptime(date_str, fmt).date()
            return date
        except ValueError:
            continue
    raise ValueError


def print_reformatted_date(date):
    """
    Output that same date in YYYY-MM-DD format.
    """
    formatted_date = date.strftime("%Y-%m-%d")
    print(formatted_date)


if __name__ == "__main__":
    main()
