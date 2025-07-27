from collections import defaultdict


def main():
    """
    Output the user's grocery list with items:
    - Printed in all uppercase.
    - Sorted alphabetically.
    - Prefixed by the number of times.
    """
    grocery_list = get_items()
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item}")


def get_items():
    """
    Prompt users for items and organize them in a dictionary.
    """
    basket = defaultdict(int)  # Initialize defaultdict with int type
    while True:
        item = input("").upper()
        if item.lower() == "q":
            print()
            break
        basket[item] += 1
    return basket


if __name__ == "__main__":
    main()
