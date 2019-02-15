from parser import parse_stdin
from solver import solve
import argparse
import logging

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-l",
                        "--loglevel",
                        type=str,
                        default="WARNING",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="Setup the log level. can be one of DEBUG, INFO, WARNING, ERROR, CRITICAL")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    logging.basicConfig(level=args.loglevel)

    initial_puzzle = parse_stdin()
    
    solve(initial_puzzle)


if __name__ == "__main__":
    main()
