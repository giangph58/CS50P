def main():
    """
    Get input fractions
    Print corresponding fuel status.
    """
    while True:
        fraction = input("Fraction: ").strip()
        if fraction.lower() == "q":
            break
        x, y = fraction.split("/")
        try:
            x = int(x)
            y = int(y)
            percent = x / y * 100
            if x > y:
                continue
            print_fuel(percent)
        except (ValueError, ZeroDivisionError):
            continue


def print_fuel(p):
    """Prints fuel status based on the given percentage."""
    if p <= 1:
        print("E")
    elif p >= 99:
        print("F")
    else:
        print(f"{p:.0f}%")


if __name__ == "__main__":
    main()
