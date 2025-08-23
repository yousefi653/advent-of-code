import re


def count_occurrences(line):
    pattern = re.compile(r"XMAS")
    return len(re.findall(pattern, line))


def right_left(grid):
    total = 0
    for row in grid:
        total += count_occurrences(row)
        reversed_row = row[::-1]
        total += count_occurrences(reversed_row)
    return total


def up_down(grid):
    total = 0
    for col_index in range(len(grid[0])):
        col = "".join(row[col_index] for row in grid)
        total += count_occurrences(col)

        reversed_col = col[::-1]
        total += count_occurrences(reversed_col)
    return total


def diagonal_lr(grid):
    total = 0
    for start_col in range(len(grid[0]) - 1, 0, -1):
        diag = ""
        col = start_col
        grid_width = len(grid[0])

        for row in grid:
            if col == grid_width:
                continue
            diag += row[col]
            col += 1
        total += count_occurrences(diag)
        total += count_occurrences(diag[::-1])

    for start_row in range(len(grid)):
        diag = ""
        col = 0
        for row_index in range(start_row, len(grid)):
            diag += grid[row_index][col]
            col += 1
        total += count_occurrences(diag)
        total += count_occurrences(diag[::-1])

    return total


def diagonal_rl(grid):
    total = 0
    for start_row in range(3, len(grid)):
        diag = ""
        col = start_row
        for row in grid:
            if col == -1:
                continue
            diag += row[col]
            col -= 1
        total += count_occurrences(diag)
        total += count_occurrences(diag[::-1])

    for start_col in range(-4, -len(grid), -1):
        diag = ""
        col = start_col
        for row_index in range(len(grid) - 1, -1, -1):
            if col == 0:
                continue
            diag += grid[row_index][col]
            col += 1
        total += count_occurrences(diag)
        total += count_occurrences(diag[::-1])

    return total


with open("puzzle_input.txt", "r") as file:
    grid = list(map(lambda x: x.strip(), file.readlines()))

total_count = 0
total_count += right_left(grid)
total_count += up_down(grid)
total_count += diagonal_lr(grid)
total_count += diagonal_rl(grid)

print(total_count)
