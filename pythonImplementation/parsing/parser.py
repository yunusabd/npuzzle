import sys
import re
import logging
from data_model import PuzzleState, ParsingError
from util import flatten_nested_list
from parsing.integrity import check_puzzle_integrity

def get_next_line():
    "yield each line  content of input on stdin."
    for line_content in sys.stdin:
        yield line_content

def line_is_comment(line):
    trimmed_line = line.lstrip()
    if trimmed_line.startswith("#"):
        print("Comment")
        return True
    return False

def line_is_puzzle_size(line):
    trimmed_line = line.strip()
    if re.match(r"\d+(\s+)?(#.*)?$", trimmed_line):
        return True
    return False
    
def line_is_puzzle_content(line, puzzle_size):
    trimmed_line = line.strip()
    if re.match(f"(\d+\s+){ {puzzle_size-1} }(\d+\s*)(#.*)?$", trimmed_line):
        return True
    print(f"line should contain {puzzle_size} numbers")
    return False

def get_puzzle_size(line):
    "Return puzzle size as an int."
    return int(line.split()[0])

def get_puzzle_row(puzzle_size, line):
    splitted_line = line.split()
    row_string = splitted_line[0:puzzle_size]
    # convert to list of ints.
    row_int = list(map(lambda x: int(x), row_string))
    return row_int

def parse_input():
    logging.debug("Parsing Input")
    # default value before parsing actual value.
    puzzle = PuzzleState(0,0,0,0,[],0)
    rows = []
    for line in get_next_line():
        if line_is_comment(line):
            continue
        if puzzle.size == 0 and line_is_puzzle_size(line):
            puzzle.size = get_puzzle_size(line)
        elif puzzle.size != 0 and line_is_puzzle_content(line, puzzle.size):
            row = get_puzzle_row(puzzle.size, line)
            rows.append(row)
    puzzle.currentState = rows
    return puzzle



def parse_stdin():
    puzzle = parse_input()
    check_puzzle_integrity(puzzle)
    return puzzle


