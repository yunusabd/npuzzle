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
                        default="WARNING",
                        choices=["NONE", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="Setup the log level. can be one of DEBUG, INFO, WARNING, ERROR, CRITICAL or NONE")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    if (args.loglevel != "NONE"):
        logging.basicConfig(level=args.loglevel)

    initial_puzzle = parse_stdin()
    # print(initial_puzzle)


    solver = Astar(initial_puzzle)
    if (solver.is_solvable()):
        solver.solve()
    else:
        print("This puzzle is not solvable !")


if __name__ == "__main__":
    # if we want some profiling
    # cProfile.run('main()')
    main()
