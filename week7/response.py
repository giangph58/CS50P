import validators


def main():
    print(is_valid(input("What's your email address? ")))


def is_valid(s) -> str:
    if validators.email(s):
        return "Valid"
    return "Invalid"


if __name__ == "__main__":
    main()
