from ortools.sat.python import cp_model
from graph import getConnectedGraphs
from gridGenerator import createGrid
from gridReader import readGrid
from vertex import Vertex
import numpy as np


# We define variables of the PLNE problem. We take the same labels of the document "Benchmark Instances and
# Branch-and-Cut Algorithm for the Hashiwokakero Puzzle"

# Delta(i) represent all vertices that you can connect to i.
def createDelta(vertices):
    delta = [None] * len(vertices)
    i = 0
    for currentVertex in vertices:
        if len(vertices) == 0:
            return []
        if i < len(vertices) - 1 and vertices[i + 1].x == currentVertex.x:
            rightNeighbour = vertices[i + 1]
        else:
            rightNeighbour = None
        if i > 0 and vertices[i - 1].x == currentVertex.x:
            leftNeighbour = vertices[i - 1]
        else:
            leftNeighbour = None
        bottomNeighbour = None
        for v in vertices[i + 1:]:
            if v.y == currentVertex.y:
                bottomNeighbour = v
                break
        topNeighbour = None
        if i > 0:
            for v in vertices[i - 1::-1]:
                if v.y == currentVertex.y:
                    topNeighbour = v
                    break
        delta[i] = ((topNeighbour, rightNeighbour, bottomNeighbour, leftNeighbour))
        i += 1
    return delta


# Return epsilon the list of indexes of pairs of vertices that can be connected
def createEpsilon(delta):
    epsilon = []
    for i in range(len(delta)):
        for neighbours in range(len(delta[i])):
            if delta[i][neighbours] != None and delta[i][neighbours].index > i:
                epsilon.append((i, delta[i][neighbours].index))
    return epsilon


# Return bigDelta, he set of intersecting edge pairs {(i, j), (k, l)}
def createBigDelta(epsilon, vertices):
    bigDelta = []
    for index in range(len(epsilon)):
        (i, j) = epsilon[index]
        smallX = -1
        bigX = -1
        smallY = -1
        bigY = -1
        if vertices[i].x < vertices[j].x:
            smallX = vertices[i].x
            bigX = vertices[j].x
        else:
            smallX = vertices[j].x
            bigX = vertices[i].x
        if vertices[i].y < vertices[j].y:
            smallY = vertices[i].y
            bigY = vertices[j].y
        else:
            smallY = vertices[j].y
            bigY = vertices[i].y
        for index1 in range(len(epsilon)):
            (k, l) = epsilon[index1]
            if vertices[i].x == vertices[j].x:
                if vertices[k].x < vertices[l].x:
                    smallX2 = vertices[k].x
                    bigX2 = vertices[l].x
                else:
                    smallX2 = vertices[l].x
                    bigX2 = vertices[k].x
                if vertices[k].y == vertices[l].y and bigY > vertices[k].y > smallY and smallX2 < vertices[i].x < bigX2:
                    bigDelta.append({(i, j), (k, l)})
            else:
                if vertices[k].y < vertices[l].y:
                    smallY2 = vertices[k].y
                    bigY2 = vertices[l].y
                else:
                    smallY2 = vertices[l].y
                    bigY2 = vertices[k].y
                if vertices[k].x == vertices[l].x and bigX > vertices[k].x > smallX and smallY2 < vertices[i].y < bigY2:
                    bigDelta.append({(i, j), (k, l)})
    return bigDelta


# Constraint (1)
def sumConstraint1(k, vertices, variable, epsilon):
    result = 0
    for i in range(k):
        if (i, k) in epsilon and not isinstance(variable[i][k], float):
            result += variable[i][k]
    for j in range(k, len(vertices)):
        if (k, j) in epsilon and not isinstance(variable[k][j], float):
            result += variable[k][j]
    return result


def constraint1(model, vertices, epsilon, x, d):
    for k in range(len(vertices)):
        model.Add(sumConstraint1(k, vertices, x, epsilon) == d[k])


# Constraint (2)
def constraint2(model, epsilon, x, y):
    for (i, j) in epsilon:
        model.Add(y[i][j] <= x[i][j])
        model.Add(x[i][j] <= 2 * y[i][j])


# Constraint (3)
def constraint3(model, bigDelta, y):
    for (i, j), (k, l) in bigDelta:
        model.Add(y[i][j] + y[k][l] <= 1)


# Constraint (4)
def sumConstraint4(epsilon, S, Rest, y):
    res = 0
    for i in S:
        for j in Rest:
            if (i, j) in epsilon:
                res += y[i][j]
    return res


def constraint4(model, cc, V, epsilon, y):
    S = cc[0]
    Rest = list(set(V).difference(S))
    model.Add(sumConstraint4(epsilon, S, Rest, y) >= 1)

# Constraint (7)
def sumConstraint7(epsilon, y):
    res = 0
    for (i, j) in epsilon:
        res += y[i][j]
    return res

def constraint7(model, epsilon, y, size):
    model.Add(sumConstraint7(epsilon, y) >= size - 1)

def solve(grid, vertices):
    delta = createDelta(vertices)
    epsilon = createEpsilon(delta)
    bigDelta = createBigDelta(epsilon, vertices)
    V = [vertex.index for vertex in vertices]
    model = cp_model.CpModel()

    # number of bridges to be constructed from each island
    d = []
    for line in grid:
        for v in line:
            if isinstance(v, Vertex):
                d.append(v.numberNeighbours)
    # Defines x and y variables
    # Xij is the number of bridges between i and j
    # Yij is whether or not there are bridges between i and j
    x = np.zeros((len(vertices), len(vertices)))
    x = x.tolist()
    y = np.zeros((len(vertices), len(vertices)))
    y = y.tolist()
    z = np.zeros(len(vertices))
    for (i, j) in epsilon:
        x[i][j] = model.NewIntVar(0, 2, "x{0}_{1}".format(i, j))
        y[i][j] = model.NewIntVar(0, 1, "y{0}_{1}".format(i, j))

    constraint1(model, vertices, epsilon, x, d)
    constraint2(model, epsilon, x, y)
    constraint3(model, bigDelta, y)
    constraint7(model, epsilon, y, len(vertices))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        cc = getConnectedGraphs(len(vertices), solver, epsilon, x)
        while len(cc) > 1:
            constraint4(model, cc, V, epsilon, y)
            solver = cp_model.CpSolver()
            status = solver.Solve(model)
            if not (status == cp_model.OPTIMAL or status == cp_model.FEASIBLE):
                raise ("Error Not Feasible !")
            cc = getConnectedGraphs(len(vertices), solver, epsilon, x)
        return createGrid(x, vertices, epsilon, len(grid), solver)
    else:
        raise("Error Not Feasible !")
