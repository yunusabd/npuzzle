import logging

def manhattan_heuristic(puzzle, solution):
    cost = 0
    for row in range(puzzle.size):
        for column in range(puzzle.size):
            digit = puzzle.currentState[row][column]
            if (digit == 0):
                continue
            (expected_row, expected_column) = solution.positions[digit]

            x_distance = abs(row - expected_row)
            y_distance = abs(column - expected_column)

            cost += (x_distance + y_distance)
    return cost

def hamming_heuristic(puzzle, solution):
    "return a cost equal to misplaced tiles."
    cost = 0
    for y in range(puzzle.size):
        for x in range(puzzle.size):
            if (puzzle.currentState[y][x] == 0):
                continue
            digit = puzzle.currentState[y][x]
            if (digit != solution.state[y][x]):
                cost += 1
    return cost


def linear_conflict(puzzle, solution):
    cost = 0
    for row in range(puzzle.size):
        for column in range(puzzle.size):
            digit = puzzle.currentState[row][column]
            if (digit == 0):
                continue

            # Manhattan Part. Compute distance.
            (expected_row, expected_column) = solution.positions[digit]
            cost += abs(column - expected_column)
            cost += abs(row - expected_row)

            # Linear Conflict Part.
            # If current tile on its expected column.
            if (column == expected_column):
                cost += compute_vertical_conflict(puzzle, solution, digit, row, column, expected_column)
            
            # If current tile on its expected row.
            if (row == expected_row):
                cost += compute_horizontal_conflict(puzzle, solution, digit, row, column, expected_row)

    return cost

def compute_horizontal_conflict(puzzle, solution, digit, row, column, expected_row):
    cost = 0
    for index in range(puzzle.size):

        # skip if empty or reference tile.
        if (index == column or puzzle.currentState[row][index] == 0):
            continue

        # get infos about tile.
        compare_digit = puzzle.currentState[row][index]
        (compare_digit_expected_row,
            compare_digit_expected_column) = solution.positions[compare_digit]

        # tmp tile goal position should be on same row.
        if (compare_digit_expected_row != expected_row):
            continue

        # if conflict
        if ((index < column and column <= compare_digit_expected_column) or
                (index > column and column >= compare_digit_expected_column)):
            logging.debug(f"Horizontal conflict between {digit} & {compare_digit}")
            cost += 2
    return cost

def compute_vertical_conflict(puzzle, solution, digit, row, column, expected_column):
    cost = 0
    for index in range(puzzle.size):

        # skip if empty or reference tile.
        if (index == row or puzzle.currentState[index][column] == 0):
            continue

        # get infos about tile.
        compare_digit = puzzle.currentState[index][column]
        (compare_digit_expected_row, compare_digit_expected_column) = solution.positions[compare_digit]

        # tmp tile goal position should be on same column.
        if (compare_digit_expected_column != expected_column):
            continue

        # if conflict
        if ((index < row and row <= compare_digit_expected_row) or
            (index > row and row >= compare_digit_expected_column)):
            logging.debug(f"Vertical conflict between {digit} & {compare_digit}")
            cost += 2
    return cost
