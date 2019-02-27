def manhattan_heuristic(puzzle, solution):
    cost = 0
    for y in range(puzzle.size):
        for x in range(puzzle.size):
            digit = puzzle.currentState[y][x]
            if (digit == 0):
                continue
            (expected_x, expected_y) = solution.positions[digit]

            x_distance = abs(x - expected_x)
            y_distance = abs(y - expected_y)

            cost += (x_distance + y_distance)
    return cost

def hamming_heuristic(puzzle, solution):
    "return a cost equal to misplaced tiles."
    cost = 0
    for y in range(puzzle.size):
        for x in range(puzzle.size):
            digit = puzzle.currentState[y][x]
            if (digit != solution.state[y][x]):
                cost += 1
    return cost