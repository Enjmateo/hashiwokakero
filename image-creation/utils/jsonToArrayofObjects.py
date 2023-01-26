import json
from Water import Water
from VertexOutput import VertexOutput
from Noeud import Noeud

def jsonToArrayofObjects(file) : 
    # Open the JSON file
    with open(file, "r") as json_file:
        # Parse the JSON file
        json_data = json.load(json_file)
        array = []
        # Go through each item in the JSON file
        for i in range(len(json_data)):
            array.append([])
            for j in range(len(json_data[i])):
                # Turn each item into an object
                obj = json_data[i][j]
                if len(json_data[i][j]) == 2 : 
                    thisRand = Water(obj['horizontal'], obj['vertical'])
                else : 
                    thisRand = VertexOutput(obj['k'], obj['top'], obj['right'], obj['bottom'], obj['left'])
                # Add the object to the array
                array[i].append(thisRand)
    return(array)


def listToArrayOfObjects(this_list) :
    array = []
    for i, row in enumerate(this_list) : 
        array.append([])
        for j, obj in enumerate(this_list[i]) : 
            # Turn each item into an object
            thisRand = Noeud(obj['k'], obj['top'], obj['right'], obj['bottom'], obj['left'], obj['horizontal'], obj['vertical'])
            # Add the object to the array
            array[i].append(thisRand)
    return(array)


#this_list = [[{'bottom': 2, 'k': 4, 'left': 0, 'right': 2, 'top': 0}, {'horizontal': 2, 'vertical': 0}, {'bottom': 1, 'k': 3, 'left': 2, 'right': 0, 'top': 0}, {'horizontal': 0, 'vertical': 0}], [{'horizontal': 0, 'vertical': 2}, {'horizontal': 0, 'vertical': 0}, {'bottom': 0, 'k': 1, 'left': 0, 'right': 0, 'top': 1}, {'horizontal': 0, 'vertical': 0}], [{'horizontal': 0, 'vertical': 2}, {'horizontal': 0, 'vertical': 0}, {'horizontal': 0, 'vertical': 0}, {'horizontal': 0, 'vertical': 0}], [{'bottom': 0, 'k': 2, 'left': 0, 'right': 0, 'top': 2}, {'horizontal': 0, 'vertical': 0}, {'horizontal': 0, 'vertical': 0}, {'horizontal': 0, 'vertical': 0}]]
#this_list = [[{"horizontal":0,"vertical":0,"bottom":0,"top":0,"left":0,"right":1,"k":1},{"horizontal":1,"vertical":0,"bottom":0,"top":0,"left":0,"right":0,"k":0},{"horizontal":0,"vertical":0,"bottom":1,"top":0,"left":1,"right":0,"k":2}],[{"horizontal":0,"vertical":0,"bottom":0,"top":0,"left":0,"right":0,"k":0},{"horizontal":0,"vertical":0,"bottom":0,"top":0,"left":0,"right":0,"k":0},{"horizontal":0,"vertical":1,"bottom":0,"top":0,"left":0,"right":0,"k":0}],[{"horizontal":0,"vertical":0,"bottom":0,"top":0,"left":0,"right":0,"k":0},{"horizontal":0,"vertical":0,"bottom":0,"top":0,"left":0,"right":0,"k":0},{"horizontal":0,"vertical":0,"bottom":0,"top":1,"left":0,"right":0,"k":1}]]
#print(listToArrayOfObjects(this_list))