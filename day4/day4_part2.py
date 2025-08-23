def diagonal_lr(grid):

    temp = "".join(grid[i][i] for i in range(3))
    temp_reverse = temp[::-1]

    if temp == "MAS" or temp_reverse == "MAS":
        return True
    return False


def diagonal_rl(grid):

    temp = ""
    row = 0
    for i in range(len(grid) - 1, -1, -1):
        temp += grid[row][i]
        row += 1

    temp_reverse = temp[::-1]

    if temp == "MAS" or temp_reverse == "MAS":
        return True
    return False


with open("puzzle_input.txt", "r") as file:
    grid = list(map(lambda x: x.strip(), file.readlines()))


sum = 0
for j in range(len(grid) - 2):
    for i in range(len(grid[0]) - 2):
        temp = []
        for row in range(j, j + 3):
            temp.append(grid[row][i : i + 3])

        if diagonal_lr(temp) and diagonal_rl(temp):
            sum += 1
print(f"sum: {sum}")
