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

            # In case already in solution position or not in solution row/column
            if (row == expected_row):
                # iterate on row
                for index in range(puzzle.size):
                    if (index == column or puzzle.currentState[row][index] == 0):
                        continue
                    compare_digit = puzzle.currentState[row][index]
                    (compare_digit_expected_row, compare_digit_expected_column) = solution.positions[compare_digit]
                    if (compare_digit_expected_row != expected_row):
                        continue
                    if ((compare_digit_expected_column >= column and column > index) or 
                        (compare_digit_expected_column <= column and column < index)):
                        puzzle.display()
                        print(f"Linear conflict between {digit} & {compare_digit}")
                        cost += 1

    
            # iterate on column
            if (column == expected_column):
                for index in range(puzzle.size):
                    if (index == row):
                        continue
                    pass


            # for (uint8_t j=row * b._width, l=j + col; j < l; j++) {
            #     if (b._tiles[j] == 0) {
            #         continue
            #     }
            #     if (goalRow[j] == row & & goalCol[i] < goalCol[j]) {
            #         md += 2
            #     }
            # }

    return cost





# def linear_conflict(puzzle, solution):
#     linear_cost = 0
#     manhattan_cost = manhattan_heuristic(puzzle, solution)

#     for y in range(puzzle.size):
#         for x in range(puzzle.size):
#             # check if belong to
#             return

#     return manhattan_cost + linear_cost

# def generate_pairs(puzzle, solution):
#     "return list of tiles that are already in their final row/column"
#     tiles_placed = []

#     for row in range(puzzle.size):
#         for column in range(puzzle.size):
#             tile_value = puzzle.currentState[row][column]
#             if (tile_value == 0):
#                 continue

#             (expected_row, expected_column) = solution.positions[tile_value]

#             # We use XOR here cause we dont want case where tile is perfectly placed.
#             if ((row == expected_row) ^ (column == expected_column)):
#                 tiles_placed.append({"tile": tile, })
