text = input("Input: ")
print("Output: ", end="")
for c in text:
    if c.lower() in ["a", "i", "e", "o", "u"]:
        continue
    print(c, end="")