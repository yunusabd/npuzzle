def manhattan_heuristic(puzzle, solution):
    cost = 0
    for y in range(puzzle.size):
        for x in range(puzzle.size):
            digit = puzzle.currentState[y][x]
            (expected_x, expected_y) = solution.positions[digit]

            x_distance = abs(x - expected_x)
            y_distance = abs(y - expected_y)

            cost += (x_distance + y_distance)
    return cost