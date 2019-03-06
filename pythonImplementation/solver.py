import heapq
import random
from data_model import PuzzleState
from heuristic import *
from solvable import is_solvable
import util

class Astar:
    def __init__(self, initial_puzzle):
        self.initial_puzzle = initial_puzzle
        self.open_list = []
        self.closed_list = {}
        self.solution = util.generate_puzzle_solution(self.initial_puzzle.size)
        # keep some stats :
        self.expanded_node_number = 0
        self.current_node_number = 1
        self.total_node_number = 1

    def solve(self):
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
                self.closed_list[current_state.hash()] = current_state.overall_cost

                # expand to next combinations.
                for new_state in current_state.expand():

                    # ignore state already in open/closed list.
                    if (new_state.hash() in self.closed_list):
                        continue

                    # compute cost & push in open list
                    new_state.compute_cost(self.solution, hamming_heuristic)
                    self.queue_push(new_state)

        if (success):
            current_state.display_path()
            current_state.display_move_number()
            current_state.display_analytics(self)

    def is_solvable(self):
        return is_solvable(self.initial_puzzle, self.solution)
           
    def queue_push(self, value):
        self.analytics_push()
        heapq.heappush(self.open_list, value)

    def queue_pop(self):
        self.analytics_pop()
        return heapq.heappop(self.open_list)

    def analytics_push(self):
        "Called whenever an object is pushed onto open list."
        self.current_node_number += 1
        if (self.current_node_number > self.total_node_number):
            self.total_node_number = self.current_node_number


    def analytics_pop(self):
        "Called whenever an object is popped from open list."
        self.expanded_node_number += 1
        self.current_node_number -= 1
