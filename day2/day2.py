def inc_dec(report):
    inc = True
    dec = True
    temp = report.copy()
    
    for i in range(len(temp) - 1):
        if not (temp[i] < temp[i + 1]):
            inc = False
            break
    if inc:
        return True
    
    for i in range(len(temp) - 1):
        if not (temp[i] > temp[i + 1]):
            dec = False
            break
    if dec:
        return True
    return False


def difference(report):
    for i in range(len(report) - 1):
        diff = abs(report[i + 1] - report[i])
        if not (1 <= diff <= 3):
            return False
    return True


with open("puzzle_input.txt", "r") as file:
    safes = 0
    for line in file:
        report = line.strip().split()
        report = list(map(lambda x: int(x), report))

        if difference(report) and inc_dec(report):
            safes += 1

print(f"safes: {safes}")
