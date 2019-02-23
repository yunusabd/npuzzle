from dataclasses import dataclass
from typing import List, Any
from util import generate_permutations

@dataclass(order=True)
class PuzzleState:
    overall_cost: int
    moveNumber: int
    heuristicCost: int
    size: int
    currentState: List[List[int]]
    previous_state: Any

    def __hash__(self):
        return hash(str(self.currentState))

    def is_final_state(self, solution):
        return self.currentState == solution

    def expand(self, heuristic):
        "generates possible transitions from a given state"
        for child in generate_permutations(self):
            # child.display()
            child.previous_state = self
            child.moveNumber = self.moveNumber + 1
            child.size = self.size
            yield child

    def compute_cost(self, solution, heuristic):
        # compute cost of node.
        self.heuristicCost = heuristic(self.currentState, solution)
        self.overall_cost = self.heuristicCost + self.moveNumber


    def display(self):
        "display current state of puzzle on screen"
        for elem in self.currentState:
            print(elem)
        print("")

    def display_path(self):
        if (self.previous_state):
            self.previous_state.display_path()
        self.display()

@dataclass
class ParsingError(Exception):
    message: str

