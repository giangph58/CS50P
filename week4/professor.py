import random


def main():
    """
    Prompt for a level.
    Randomly generate 10 math problems.
    Prompt for correct solutions, maximum 3 times.
    Display output.
    """
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        solution = x + y
        n_try = 3
        while n_try > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == solution:
                    score += 1
                    break
                else:
                    print("EEE")
                    n_try -= 1
            except ValueError:
                print("EEE")
                n_try -= 1
                pass
        if n_try == 0:
            print(f"{x} + {y} = {solution}")
    print(f"Score: {score}")


def get_level():
    """
    Randomly generates an integer between 1 and 3, inclusive.
    """
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    """
    Randomly generate a number with a given number of digits.
    """
    num = random.randint(10 ** (level - 1), 10**level - 1)
    return num


if __name__ == "__main__":
    main()