import emoji


def main():
    """Prompt for emoji."""
    emo = input("Input: ")
    print(emoji.emojize(f"Output: {emo}", language="alias"))


if __name__ == "__main__":
    main()
