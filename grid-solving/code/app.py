from flask import Flask, request, jsonify
from gridReader import convertGrid 
from solver import solve
import json

app = Flask(__name__)

# Getter to solve the grid
@app.route('/solve', methods=['POST'])
def solveGrid():
    data = request.get_json()

    # Get the grid and the size
    grid = data['grid']
    size = data['size']

    # Convert grid to objects
    newGrid, vertices = convertGrid(grid, size)

    # Solve the grid
    sol = solve(newGrid, vertices)

    # Convert the solution to json
    for x in range(len(sol)):
        for y in range(len(sol[x])):
            if sol[x][y] is not None:
                sol[x][y] = sol[x][y].__dict__
    json_response = jsonify(sol)
    return json_response

if __name__ == '__main__':
    app.run(host="0.0.0.0")
