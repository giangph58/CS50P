def main():
    text = input("Greeting: ")
    print(value(text))


def value(greeting: str) -> int:
    if greeting[:5].lower() == "hello":
        return 0
    elif greeting[:1].lower() == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
