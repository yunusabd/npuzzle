import logging
from data_model import ParsingError
from util import flatten_nested_list

def check_puzzle_unicity(puzzle_list):
    "a set items are unique. we compare basic array to its set version."
    if (len(set(puzzle_list)) != len(puzzle_list)):
        raise ParsingError("Puzzle numbers must be unique.")


def check_numbers_present(puzzle_size, puzzle_list):
    if (puzzle_size <= 0):
        raise ParsingError("Puzzle length must be greater than 0")
    if (puzzle_size*puzzle_size != len(puzzle_list)):
        raise ParsingError(
            "Puzzle does not contain expected amount of numbers.")


def check_correct_numbers(puzzle_size, puzzle_list):
    for number in range(puzzle_size * puzzle_size):
        if (number not in puzzle_list):
            raise ParsingError("Puzzle doesnt contain expected numbers.")


def check_puzzle_integrity(puzzle):
    logging.debug("Checking puzzle validity.")
    flattened_puzzle = flatten_nested_list(puzzle.currentState)

    try:
        check_puzzle_unicity(flattened_puzzle)
        check_numbers_present(puzzle.size, flattened_puzzle)
        check_correct_numbers(puzzle.size, flattened_puzzle)
    except ParsingError as err:
        print(err.message)
        exit(-1)
