import csv

# print a matrix line by line
def printMatrix(matrix):
    print("[")
    for m in matrix:
        print(m)
    print("]")

# Compute the common area betwin 2 surfaces 
def intersection_area(rect1, rect2):
    [x1, y1, w1, h1] = rect1
    [x2, y2, w2, h2] = rect2
    left = max(x1, x2)
    right = min(x1 + w1, x2 + w2)
    top = max(y1, y2)
    bottom = min(y1 + h1, y2 + h2)
    if left > right or top > bottom:
        return 0
    else:
        return (right - left) * (bottom - top)

# From a given path to a file return a matrix
def readMatrixFromFile(file):
    # Open the input file and read the data
    with open(file, 'r') as file:
        data = list(csv.reader(file, delimiter=' '))

    # Convert the data into a matrix
    matrix = []
    for row in data:
        matrix.append([float(x) for x in row])

    file.close()
    return matrix