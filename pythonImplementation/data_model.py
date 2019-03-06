from dataclasses import dataclass
from typing import List, Any, Dict
from util import generate_permutations, flatten_nested_list

@dataclass(order=True)
class PuzzleState:
    overall_cost: int
    moveNumber: int
    heuristicCost: int
    size: int
    currentState: List[List[int]]
    previous_state: Any
    
    def hash(self):
        to_str = [str(x) for x in flatten_nested_list(self.currentState)]
        joined = "".join(to_str)
        return (int(joined))

    def is_final_state(self, solution):
        return self.currentState == solution

    def expand(self):
        "generates possible transitions from a given state"
        for child in generate_permutations(self):
            # child.display()
            child.previous_state = self
            child.moveNumber = self.moveNumber + 1
            child.size = self.size
            yield child

    def compute_cost(self, solution, heuristic):
        "Take a heuristic function as param to compute cost."
        self.heuristicCost = heuristic(self, solution)
        self.overall_cost = self.heuristicCost + self.moveNumber

    def display_solution(self, stats):
        self.display_move_number()
        self.display_path()
        self.display_analytics(stats)

    def display(self):
        "display current state of puzzle on screen"
        width = self.size//2
        for elem in self.currentState:
            print("[", end="")
            for item in elem[:-1]:
                print(f"{item:{width}}, ", end="")
            print(f"{elem[-1]:{width}}]")
        print("")

    def display_path(self):
        if (self.previous_state):
            self.previous_state.display_path()
        self.display()
    
    def display_move_number(self):
        print("\n\t\t SOLUTION :\n")
        print(f"Number of moves to solve the puzzle : {self.moveNumber}\n")
    
    def display_analytics(self, stats):
        print("\t\t STATS :\n")
        print(f"Total node selected in open list : {stats.expanded_node_number}")
        print(f"Maximum amount of nodes in open list at same time: {stats.total_node_number}\n")


@dataclass
class PuzzleSolution:
    "contains the finished state and a map to get locations of each digits."
    state: List[List[int]]
    positions: Dict

@dataclass
class ParsingError(Exception):
    message: str

