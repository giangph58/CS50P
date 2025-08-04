def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word: str) -> str:
    """Return shortened word without vowels"""
    return "".join(c for c in word if c.lower() not in ["a", "i", "e", "o", "u"])


if __name__ == "__main__":
    main()
