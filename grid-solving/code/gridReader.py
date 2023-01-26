import sys
from vertex import Vertex

# Return a Matrix representing the grid, a list of all the vertices and the Number of vertices
def readGrid():
    file = open("../../Hashi_Puzzles/Hashi_Puzzles/" + sys.argv[1], 'r')
    firstLine = file.readline()
    split = firstLine.split()
    nbVertices = int(split[2])
    i = split[0]
    if not i.isdigit():
        raise Exception("Wrong file format, first word of first line not a number")

    i = int(i)
    j = 0
    grid = []
    verticesList = []
    for x in range(i):
        line = file.readline().split()
        gridLine = []
        y = 0
        for k in line:
            if int(k) != 0:
                vertex = Vertex(j, int(k), x, y)
                gridLine.append(vertex)
                verticesList.append(vertex)
                j += 1
            else:
                gridLine.append(0)
            y += 1
        grid.append(gridLine)
    return grid, verticesList, nbVertices

def convertGrid(grid, size):
    j = 0
    newGrid = []
    vertices = []
    for x in range(size):
        gridLine = []
        for y in range(size):
            if grid[x][y] != 0:
                vertex = Vertex(j, grid[x][y], x, y)
                gridLine.append(vertex)
                vertices.append(vertex)
                j += 1
            else:
                gridLine.append(0)
        newGrid.append(gridLine)
    return newGrid, vertices
