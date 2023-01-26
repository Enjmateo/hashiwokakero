from Water import Water
from VertexOutput import VertexOutput

# Print without going to the next line
def pprint(arg):
    print(arg, end = '')

# [ONLY FOR TESTING]
# Print an array of objects 
def bprint(array) :
    for i in range(len(array)):
        for j in range(len(array[0])):
            obj = array[i][j]
            if isinstance(obj, VertexOutput):
                pprint(obj.k)
            elif isinstance(obj, Water):
                if obj.Horizontal == 1:
                    pprint("h")
                elif obj.Horizontal == 2:
                    pprint("H")
                elif obj.Vertical == 1:
                    pprint("v")
                elif obj.Vertical == 2:
                    pprint("V")
            pprint("-")
        print("\n")