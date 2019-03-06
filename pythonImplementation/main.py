from parsing.parser import parse_stdin
from solver import Astar
from solvable import compute_inversions
import argparse
import logging
import util
import cProfile

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-l",
                        "--loglevel",
                        type=str,
                        default="NONE",
                        choices=["NONE", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="Setup the log level.")

    parser.add_argument("-H",
                        "--heuristic",
                        type=str,
                        default="manhattan",
                        choices=["manhattan", "hamming", "..."],
                        help="Choose an heuristic to solve puzzle.")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    if (args.loglevel != "NONE"):
        logging.basicConfig(level=args.loglevel)

    initial_puzzle = parse_stdin()
    # print(initial_puzzle)


    solver = Astar(initial_puzzle)
    solver.set_heuristic(args.heuristic)
    if (solver.is_solvable()):
        solver.solve()
    else:
        print("This puzzle is not solvable !")


if __name__ == "__main__":
    # if we want some profiling
    # cProfile.run('main()')
    main()
