import sys
import requests


def main():
    """
    Specify number of bitcoins as a command-line argument.
    Outputs the current cost of Bitcoins in USD to four decimal places,
    using , as a thousands separator.
    """
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        try:
            n = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        rate = o["bpi"]["USD"]["rate_float"]
        result = rate * n
        print(f"${result:,.4f}")
        sys.exit(0)
    except requests.RequestException:
        raise requests.RequestException


if __name__ == "__main__":
    main()