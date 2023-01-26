import random
from Water import Water
from VertexOutput import VertexOutput

# [ONLY FOR TESTING]
# Generate an array of arrays where len(array) == len(array[i]) for all i
# The array is composed of two objects with random values 
# Note that some of them can't happen in the game (e.g. a VertexOutput with k = 2 and 5 lines)
def randomArray(size):
    arr = []
    for i in range(size):
        arr.append([])
        for j in range(size):
            if random.random() < 0.7:
                k = random.randint(1, 8)
                Top = random.randint(0,2)
                Right = random.randint(0,2)
                Bottom = random.randint(0,2)
                Left = random.randint(0,2)
                thisRand = VertexOutput(k, Top, Right, Bottom, Left)
                
            else:
                Horizontal = 0
                Vertical = 0
                if random.random() < 0.25:
                    Horizontal = 1
                elif random.random() < 0.5:
                    Horizontal = 2
                elif random.random() < 0.75:
                    Vertical = 1
                else:
                    Vertical = 2
                thisRand = Water(Horizontal, Vertical)
            arr[i].append(thisRand)
    return arr
