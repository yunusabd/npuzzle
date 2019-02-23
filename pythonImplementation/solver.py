import heapq
import random
from data_model import PuzzleState
import util

def manhattan(puzzle, solution):
    cost = 0
    for y in range(puzzle.size):
        for x in range(puzzle.size):
            digit = puzzle.currentState[y][x]
            (expected_x, expected_y) = solution.positions[digit]

            x_distance = abs(x - expected_x)
            y_distance = abs(y - expected_y)

            cost += (x_distance + y_distance)

    return cost


def solve(initial_puzzle):
    
    open_list = []
    closed_list = {}
    success = 0
    solution = util.generate_puzzle_solution(initial_puzzle.size)
    print(solution.positions)

    heapq.heappush(open_list, initial_puzzle)
    while (len(open_list) != 0 and not success):
        # Pop most valuable state.
        current_state = heapq.heappop(open_list)
        

        # check if final state
        if (current_state.is_final_state(solution.state)):
            success = True
        else:
            # add to closed list.
            closed_list[current_state] = current_state.overall_cost

            # expand to next combinations.
            for new_state in current_state.expand():

                # compute new node heuristic cost.
                new_state.compute_cost(solution, manhattan)

                # ignore state already in open/closed list.
                if (new_state in closed_list):
                    continue

                heapq.heappush(open_list, new_state)

    if (success):
        current_state.display_path()