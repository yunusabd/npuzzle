import sys
import numpy as np
import json, codecs

def parser():
    # read from stdin
    read = sys.stdin.read()
    try:
        size = int(read.split('\n', 1)[0])
        matrix_str = read[read.index("-----------") + len("-----------"):]
    except ValueError:
        print("Invalid input.")
        return
    lines = matrix_str.split('\n')
    cleaned = [line.strip() for line in lines if line != '']

    # read cleaned data into list
    data = []
    for line in cleaned:
        numbers = list(map(int, line.split()))
        data.append(numbers)

    arr = np.array(data)
    shape = arr.shape

    # test if arr is a square matrix
    if shape[0] != shape[1] or shape[0] != size:
        exit()

    b = arr.tolist()
    j = json.dumps(b, separators=(",", ":"), indent=4)
    return j

def writeFile():
    f = open("data.js", "w+")
    f.write("var data = " + str(parser()) + ";")

if __name__ == '__main__':
    writeFile()