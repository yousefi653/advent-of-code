import re


def find_condition(row):
    pattern = re.compile(r"\d{1,2}\|\d{1,2}")

    match = re.match(pattern, row)

    if match:
        numbers = re.findall(r"\d{1,2}", match.group())
        a, b = list(map(lambda x: int(x), numbers))
        return a, b


def find_pages_update(data):
    pattern = re.compile(r"\d{1,2}[,].*")

    match = re.match(pattern, data)
    if match:
        numbers = match.group().split(",")
        numbers = list(map(lambda x: int(x), numbers))
        return numbers


def check_conditions(pages, conditions):
    temp = pages.copy()

    for page in pages:
        for t in temp:
            if page == t:
                continue

            if not ((page, t) in conditions):
                return False
        temp.remove(page)
    return True


def fix_pages(pages, conditions):
    finall = pages.copy()

    for i in range(len(pages)):
        for j in range(len(finall)):
            if pages[i] == finall[j]:
                continue

            if not ((pages[i], finall[j]) in conditions):
                if ((finall[j], pages[i]) in conditions) and (
                    finall.index(finall[j]) > finall.index(pages[i])
                ):
                    finall[finall.index(pages[i])] = finall[j]
                    finall[j] = pages[i]
    return finall


with open("puzzle_input.txt", "r") as file:
    conditions = []
    pages = []
    for line in file:
        con = find_condition(line.strip())
        if con:
            conditions.append(con)
        else:
            pg = find_pages_update(line.strip())
            if pg:
                pages.append(pg)

middle = 0
for page in pages:
    if not (check_conditions(page, conditions)):
        fixed_pages = fix_pages(page, conditions)
        middle += fixed_pages[int(len(fixed_pages) / 2)]

print(f"sum of middle: {middle}")
