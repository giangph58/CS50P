def main():
    """
    Prompt user for items.
    Then, display the total cost of all items inputted.
    """
    total_cost = 0
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    while True:
        try:
            item = input("Item: ").title()
            if item.lower() == "q":
                break
            total_cost += menu[item]
            print(f"Total: ${total_cost:.2f}")
        except KeyError:
            continue


main()