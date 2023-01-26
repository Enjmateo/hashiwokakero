from water import Water
from vertexOutput import VertexOutput

def createGrid(x, vertices, epsilon, size, solver):
    # Init
    grid = [[Water(0, 0) for i in range(size)] for j in range(size)]
    for v in vertices:
        grid[v.x][v.y] = VertexOutput(v.numberNeighbours, 0, 0, 0, 0)

    for (i, j) in epsilon:
        x_i = vertices[i].x
        y_i = vertices[i].y
        x_j = vertices[j].x
        y_j = vertices[j].y
        sol_x = solver.Value(x[i][j])
        if sol_x > 0:
            if x_j < x_i:
                grid[x_i][y_i].top = sol_x
                grid[x_j][y_j].bottom = sol_x
                for index in range(x_j + 1, x_i):
                    grid[index][y_i].vertical = sol_x
            elif x_j > x_i:
                grid[x_i][y_i].bottom = sol_x
                grid[x_j][y_j].top = sol_x
                for index in range(x_i + 1, x_j):
                    grid[index][y_i].vertical = sol_x
            elif y_j < y_i:
                grid[x_i][y_i].left = sol_x
                grid[x_j][y_j].right = sol_x
                for index in range(y_j + 1, y_i):
                    grid[x_i][index].horizontal = sol_x
            elif y_j > y_i:
                grid[x_i][y_i].right = sol_x
                grid[x_j][y_j].left = sol_x
                for index in range(y_i + 1, y_j):
                    grid[x_i][index].horizontal = sol_x
    return grid
