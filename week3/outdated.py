def main():
    """
    Prompt for a date and output that same date in YYYY-MM-DD format.
    """
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    date = get_date(months)
    if date:
        print_reformatted_date(date, months)
    else:
        return


def get_date(months):
    """
    Prompts the user for a date, formatted like 9/8/1636 or September 8, 1636.
    If not a valid date in either format, prompt again.
    """
    while True:
        try:
            date = input("Date: ").lstrip().rstrip()
            if date.lower() == "q":
                return None
            elif (
                "/" in date
                and 1 <= int(date.split(sep="/")[1]) <= 31
                and 1 <= int(date.split(sep="/")[0]) <= 12
            ):
                return date
            elif (
                "," in date
                and date.split(sep=" ")[0] in months
                and 1 <= int(date.split(sep=" ")[1].replace(",", "")) <= 31
            ):
                return date
            else:
                raise ValueError
        except ValueError:
            continue


def print_reformatted_date(d, months):
    """
    Output that same date in YYYY-MM-DD format by adjusting the different older formats.
    """
    if "/" in d:
        mdy = d.split("/")
        m, d, y = map(int, mdy)
        print(f"{y}-{m:02}-{d:02}")
    else:
        m = int(months.index(d.split(sep=" ")[0]) + 1)
        y = int(d.split(sep=" ")[2])
        d = int(d.split(sep=" ")[1].replace(",", ""))
        print(f"{y}-{m:02}-{d:02}")


main()