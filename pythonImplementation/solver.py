import heapq
import random
from data_model import PuzzleState
import util

def solve(initial_puzzle):
    
    states_to_check = []
    states_checked = {}
    success = 0
    final_state = util.generate_puzzle_solution(initial_puzzle.size)

    heapq.heappush(states_to_check, initial_puzzle)
    while (len(states_to_check) != 0 and not success):
        # Pop most valuable state.
        current_state = heapq.heappop(states_to_check)
        

        # check if final state
        if (current_state.is_final_state(final_state)):
            success = True
        else:
            # add to closed list.
            states_checked[current_state] = current_state.overall_cost

            # expand to next combinations.
            for new_state in current_state.expand():

                # ignore state already in open/closed list.
                if (new_state in states_to_check or new_state in states_checked):
                    continue

                new_state.previous_state = current_state
                heapq.heappush(states_to_check, new_state)

    if (success):
        print(current_state)