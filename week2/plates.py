def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not s.isalnum():
        return False
    if not s[:2].isalpha():
        return False
    for c in s:
        if c.isdigit():
            index = s.index(c)
            if not s[index:].isdigit() or s[index] == "0":
                return False
            break
    return True


main()