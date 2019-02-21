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

    def expand(self):
        "generates possible transitions from a given state"
        
        pass

@dataclass
class ParsingError(Exception):
    message: str

