from dataclasses import dataclass
from typing import List, Any, Dict
from util import generate_permutations, flatten_nested_list, colors


@dataclass
class PuzzleSolution:
    "contains the finished state and a map to get locations of each digits."
    state: List[List[int]]
    positions: Dict

@dataclass
class ParsingError(Exception):
    message: str

# Dataclass decorator implements for me magic methods (__init__ , __eq__ , ....)
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

    def compute_cost(self, solution, heuristic, search_type):
        "Take a heuristic function as param to compute cost."
        # Greedy only uses heuristic
        if (search_type == "greedy"):
            self.heuristicCost = heuristic(self, solution)
            self.overall_cost = self.heuristicCost
        # uniform cost is Breadth First Search algo.
        elif (search_type == "uniform"):
            self.overall_cost = self.moveNumber
        else:
            self.heuristicCost = heuristic(self, solution)
            self.overall_cost = self.heuristicCost + self.moveNumber

    def display_solution(self, stats):
        self.display_move_number()
        self.display_path()
        self.display_analytics(stats)

    def display_move_number(self):
        print("\n\t\t SOLUTION :\n")
        print(f"Number of moves to solve the puzzle : {self.moveNumber}\n")

    def display_path(self):
        "recursively print path to solve puzzle"
        if (self.previous_state):
            self.previous_state.display_path()
        self.display()
    
    def display_analytics(self, stats):
        print("\t\t STATS :\n")
        print(f"Total node selected in open list : {stats.expanded_node_number}")
        print(f"Maximum amount of nodes in open list at same time: {stats.total_node_number}\n")

    def display(self):
        "display current state of puzzle on screen"
        width = self.size//2
        for elem in self.currentState:
            print("[", end="")
            for item in elem[:-1]:
                if (item == 0):
                    print(colors.OKGREEN, end="")
                    print(f"{item:{width}}", end="")
                    print(f"{colors.ENDC}, ", end="")
                else:
                    print(f"{item:{width}}, ", end="")
            print(f"{elem[-1]:{width}}]")
        print("")



    
