def find_garden(grid):
    for row in grid:
        if "^" in row:
            return grid.index(row), row.index("^")


def up(grid):

    row, index = find_garden(grid)
    temp = [x[index] for x in grid]
    temp.reverse()

    i = temp.index("^")
    while True:
        if temp[i + 1] == "#":
            temp[i] = "^"
            break
        temp[i] = "X"
        i += 1

    temp.reverse()
    i = 0
    for item in temp:
        grid[i][index] = item
        i += 1

    return grid


def right(grid):
    row, index = find_garden(grid)
    temp = grid[row]

    for i in range(index, len(temp)):
        if temp[i + 1] == "#":
            temp[i] = "^"
            break
        temp[i] = "X"

    grid[row] = [x for x in temp]
    return grid


def down(grid):
    row, index = find_garden(grid)
    temp = [x[index] for x in grid]

    i = temp.index("^")
    if not ("#" in temp[i:]):
        for i in range(i, len(temp)):
            temp[i] = "X"

        i = 0
        for item in temp:
            grid[i][index] = item
            i += 1
    else:
        for i in range(i, len(temp)):
            if temp[i + 1] == "#":
                temp[i] = "^"
                break
            temp[i] = "X"

    i = 0
    for item in temp:
        grid[i][index] = item
        i += 1
    return grid


def left(grid):
    row, index = find_garden(grid)
    temp = grid[row]
    temp.reverse()

    i = temp.index("^")
    for i in range(i, len(temp)):
        if temp[i + 1] == "#":
            temp[i] = "^"
            break
        temp[i] = "X"

    temp.reverse()
    grid[row] = temp
    return grid


def move_garden(grid):
    end = False

    while end != True:
        grid = up(grid)
        grid = right(grid)
        grid = down(grid)
        if find_garden(grid):
            grid = left(grid)
        else:
            end = True
    
    counter = 0
    for i in grid:
        for j in i:
            if j == "X":
                counter += 1
    return counter, grid



with open("puzzle_input.txt", "r") as file:
    grid = list(map(lambda x: list(x.strip()), file.readlines()))


count, grid = move_garden(grid)
print(f"number of X: {count}")
