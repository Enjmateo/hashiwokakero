# Class representing Vertices
# index is its index in the grid + 1
# numberNeighbours is the number of bridges that must be built
# x and y are the coordinates of the vertex
class Vertex:
    def __init__(self, index, numberNeighbours, x, y):
        self.index = index
        self.numberNeighbours = numberNeighbours
        self.x = x
        self.y = y

    def __str__(self):
        return "(i=" + str(self.index) + ", k=" + str(self.numberNeighbours) + ", x=" + str(self.x) + ", y=" + str(self.y) + ")"
