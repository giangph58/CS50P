answer = input(
    "What is the Answer to the Great Question Of Life, the Universe and Everything? "
)

if (
    answer.strip() == "42"
    or answer.lstrip().rstrip().lower() == "forty two"
    or answer.strip().lower() == "forty-two"
):
    print("Yes")
else:
    print("No")