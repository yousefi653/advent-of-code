import re


def mul(a, b):
    return a * b


pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
with open("puzzle_input.txt", "r") as file:
    sum = 0
    for line in file:
        for item in re.finditer(pattern, line):
            numbers = re.findall(r"\d{1,3}", item.group())
            a, b = list(map(lambda x: int(x), numbers))
            sum += mul(a, b)

print(f"sum: {sum}")
