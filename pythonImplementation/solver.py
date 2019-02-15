import heapq
import random
from data_model import PuzzleState

def solve(initial_puzzle):
    
    puzzleStates = []
    for i in range(10):
        elem = PuzzleState(random.randint(0, 50),i, 0, 0, [])
        heapq.heappush(puzzleStates, elem)


    print([heapq.heappop(puzzleStates) for i in range(len(puzzleStates))])
