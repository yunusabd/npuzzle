from dataclasses import dataclass
from typing import List

@dataclass(order=True)
class PuzzleState:
    overall_cost: int
    moveNumber: int
    size: int
    heuristicCost: int
    currentState: List[List[int]]