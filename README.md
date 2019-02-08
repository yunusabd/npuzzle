[![Build Status](https://travis-ci.com/yunusabd/npuzzle.svg?branch=master)](https://travis-ci.com/yunusabd/npuzzle)

# npuzzle
42 project for solving a sliding block puzzle using the A* algorithm.

To run (on MacOS):

1. ```virtualenv npuzzle_env```

2. ```source npuzzle_env/bin/activate```

3. ```pip install -r requirements.txt```

4. ```python3 gen.py -u 3 | python3 solver.py && open -a Google\ Chrome index.html```

5. ```After the solver has finished solving the puzzle, you can click in the browser to play back the moves of the solution.```