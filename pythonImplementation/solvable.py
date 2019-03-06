from util import flatten_nested_list

def is_solvable(start, solution):
    "return True if puzzle is solvable"

    start_inversions = compute_inversions(start.currentState)
    solution_inversions = compute_inversions(solution.state)

    if (start.size % 2 == 0):
        start_inversions += get_row_empty(start.currentState)
        solution_inversions += get_row_empty(solution.state)

    return ((start_inversions % 2) == (solution_inversions % 2))

def compute_inversions(puzzle):
    nb_inversions = 0
    flat_puzzle = flatten_nested_list(puzzle)
    for tile in range(len(flat_puzzle)):
        if (flat_puzzle[tile] == 0):
            continue
        for to_compare in flat_puzzle[tile+1:]:
            if (to_compare == 0):
                continue
            if (flat_puzzle[tile] > to_compare):
                nb_inversions += 1
    return nb_inversions
            
def get_row_empty(puzzle):
    for row in range(len(puzzle)):
        for elem in puzzle[row]:
            if elem == 0:
                return row