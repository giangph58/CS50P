import inflect


def main():
    """Prompts for names.
    Then bid adieu to those names/n names with n - 1 commas and one and."""
    names = []
    while True:
        name = input("Name: ")
        if not name:
            if not names:
                print("Enter at least one name.")
                continue
            else:
                break
        names.append(name)

    p = inflect.engine()
    print(f"Adieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
