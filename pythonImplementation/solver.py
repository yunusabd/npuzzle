import heapq
import random
from data_model import PuzzleState
from heuristic import *
import util

class Astar:
    def __init__(self, initial_puzzle):
        self.initial_puzzle = initial_puzzle

    def queue_push(self, value):
        heapq.heappush(self.open_list, value)

    def queue_pop(self):
        return heapq.heappop(self.open_list)

    def solve(self):
        
        self.open_list = []
        self.closed_list = {}
        self.solution = util.generate_puzzle_solution(self.initial_puzzle.size)
        success = 0

        self.queue_push(self.initial_puzzle)
        while (len(self.open_list) != 0 and not success):
            # Pop most valuable state.
            current_state = self.queue_pop()
            

            # check if final state
            if (current_state.is_final_state(self.solution.state)):
                success = True
            else:
                # add to closed list.
                self.closed_list[current_state] = current_state.overall_cost

                # expand to next combinations.
                for new_state in current_state.expand():

                    # compute new node heuristic cost.
                    new_state.compute_cost(self.solution, manhattan_heuristic)

                    # ignore state already in open/closed list.
                    if (new_state in self.closed_list):
                        continue

                    self.queue_push(new_state)

        if (success):
            current_state.display_path()