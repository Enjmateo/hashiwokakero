from water import Water
from vertexOutput import VertexOutput
import json
from solver import solve
from gridReader import readGrid


def obj_dict(obj):
    return obj.__dict__


grid = [[VertexOutput(4, 0, 2, 2, 0), Water(2, 0), VertexOutput(3, 0, 0, 1, 2)],
        [Water(0, 2), Water(0, 0), VertexOutput(1, 1, 0, 0, 0)],
        [VertexOutput(2, 2, 0, 0, 0), Water(0, 0), Water(0, 0)]]

y = json.dumps(grid, default=obj_dict)

grid1, vertices, nbVertices = readGrid()
ybis = json.dumps(solve(grid1, vertices), default=obj_dict)
print(ybis)
