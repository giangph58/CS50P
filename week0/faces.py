def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


user_input = input("You are saying: ")
print(convert(user_input))