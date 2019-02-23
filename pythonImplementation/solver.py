import heapq
import random
from data_model import PuzzleState
import util

def manhattan(current_state, solution):
    return 1


def solve(initial_puzzle):
    
    open_list = []
    closed_list = {}
    success = 0
    final_state = util.generate_puzzle_solution(initial_puzzle.size)

    heapq.heappush(open_list, initial_puzzle)
    while (len(open_list) != 0 and not success):
        # Pop most valuable state.
        current_state = heapq.heappop(open_list)
        

        # check if final state
        if (current_state.is_final_state(final_state)):
            success = True
        else:
            # add to closed list.
            closed_list[current_state] = current_state.overall_cost

            # expand to next combinations.
            for new_state in current_state.expand():

                # compute new node heuristic cost.
                new_state.compute_cost(manhattan)

                # ignore state already in open/closed list.
                if (new_state in closed_list):
                    continue

                heapq.heappush(open_list, new_state)

    if (success):
        current_state.display_path()