from generateImage import generate_image
from jsonToArrayofObjects import listToArrayOfObjects

# launch the main.py from the utils folder or it will not find the json file 
this_list = [[{"horizontal":0,"vertical":0,"bottom":0,"top":0,"left":0,"right":1,"k":1},{"horizontal":1,"vertical":0,"bottom":0,"top":0,"left":0,"right":0,"k":0},{"horizontal":0,"vertical":0,"bottom":1,"top":0,"left":1,"right":0,"k":2}],[{"horizontal":0,"vertical":0,"bottom":0,"top":0,"left":0,"right":0,"k":0},{"horizontal":0,"vertical":0,"bottom":0,"top":0,"left":0,"right":0,"k":0},{"horizontal":0,"vertical":1,"bottom":0,"top":0,"left":0,"right":0,"k":0}],[{"horizontal":0,"vertical":0,"bottom":0,"top":0,"left":0,"right":0,"k":0},{"horizontal":0,"vertical":0,"bottom":0,"top":0,"left":0,"right":0,"k":0},{"horizontal":0,"vertical":0,"bottom":0,"top":1,"left":0,"right":0,"k":1}]]
filename = generate_image(listToArrayOfObjects(this_list))
print(filename)