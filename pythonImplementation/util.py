# from data_model import PuzzleState

def flatten_nested_list(nested_list):
    return [item for elem in nested_list for item in elem]

def generate_snail_positions(array_size):
    x = 0
    y = 0
    limit = {
        'top':0,
        'bottom': array_size-1,
        'right': array_size-1,
        'left': 0
    }
    
    for _ in range(array_size//2 + 1):

        while x < limit['right']:
            yield (x, y)
            x += 1
        limit['top'] += 1

        while y < limit['bottom']:
            yield (x, y)
            y += 1
        limit['right'] -= 1

        while x > limit['left']:
            yield (x, y)
            x -= 1
        limit['bottom'] -= 1

        while y > limit['top']:
            yield (x, y)
            y -= 1
        limit['left'] += 1
    yield (x, y)


def generate_puzzle_solution(size):
    puzzle = [[0 for _ in range(size)] for _ in range(size)]


    for ((x,y), num) in zip(generate_snail_positions(size), range(1, size * size)):
        puzzle[y][x] = num

    return puzzle

def get_empty_position(puzzle):
    for x in range(len(puzzle)):
        for y in range(len(puzzle)):
            if (puzzle[y][x] == 0):
                return (y, x)

def get_allowed_permutations(puzzle):
    (y, x) = get_empty_position(puzzle)
    if (y > 0):
        yield (y-1, x)
    if (y < len(puzzle)-1):
        yield(y+1, x)
    if (x > 0):
        yield (y, x-1)
    if (x < len(puzzle)-1):
        yield(y, x+1)

def permute_puzzle(puzzle, empty_tile_pos, swap_tile_pos):
    new = puzzle
    new[empty_tile_pos[0]][empty_tile_pos[1]
                           ] = new[swap_tile_pos[0]][swap_tile_pos[1]]
    new[swap_tile_pos[0]][swap_tile_pos[1]] = 0
    return PuzzleState(0,0,0,0,0,new,0)

def generate_permutations(puzzle):
    for (empty_tile_pos, swap_tile_pos) in get_allowed_permutations(puzzle):
        new_puzzle = permute_puzzle(puzzle, empty_tile_pos, swap_tile_pos)
        yield new_puzzle
