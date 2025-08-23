import re


def find_mul(row):
    sum = 0
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    matches = re.findall(pattern, row)

    for item in matches:
        numbers = re.findall(r"\d{1,3}", item)
        a, b = list(map(lambda x: int(x), numbers))
        sum += mul(a, b)

    return sum


def mul(a, b):
    return a * b


with open("puzzle_input.txt", "r") as file:
    kole_matn = """""" ""
    sum = 0

    for line in file:
        kole_matn += line.strip()

    first_dont = re.match(r".+?don't\(\)", kole_matn).group()
    sum += find_mul(first_dont)
    for item in re.finditer(r"(do\(\).+?).*?(don't\(\))|(do\(\).+)", kole_matn):
        sum += find_mul(item.group())
        
print(f"sum: {sum}")
