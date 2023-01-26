def lineTop(obj,x,y,CELL_ROUND, CELL_SIZE) : 
    offset = int(CELL_ROUND/4)
    if obj == "solo" : 
        return (x + CELL_ROUND/2,y - CELL_ROUND/2,x + CELL_ROUND/2, y)
    elif obj == "one" : 
        return ((x-offset) + CELL_ROUND/2,y - CELL_ROUND/2,(x-offset) + CELL_ROUND/2, y)
    elif obj == "two" : 
        return (((x+offset) + CELL_ROUND/2,y - CELL_ROUND/2,(x+offset) + CELL_ROUND/2, y))
    else : print("T'as loupé ta demande de line top")
    
def lineBottom(obj,x,y,CELL_ROUND, CELL_SIZE) : 
    offset = int(CELL_ROUND/4)
    if obj == "solo" : 
        return (x + CELL_ROUND/2,y + CELL_SIZE - CELL_ROUND/2,x + CELL_ROUND/2, y + CELL_SIZE)
    elif obj == "one" : 
        return ((x-offset) + CELL_ROUND/2,y + CELL_SIZE - CELL_ROUND/2,(x-offset) + CELL_ROUND/2, y+CELL_SIZE)
    elif obj == "two" : 
        return (((x+offset) + CELL_ROUND/2,y + CELL_SIZE- CELL_ROUND/2,(x+offset) + CELL_ROUND/2, y+CELL_SIZE))
    else : print("T'as loupé ta demande de line bottom")
    
def lineRight(obj,x,y,CELL_ROUND,CELL_SIZE) : 
    offset = int(CELL_ROUND/4)
    if obj == "solo" : 
        return (x + CELL_SIZE - CELL_ROUND/2,y + CELL_ROUND/2,x + CELL_SIZE, y + CELL_ROUND/2)
    elif obj == "one" : 
        return (x + CELL_SIZE - CELL_ROUND/2,y-offset + CELL_ROUND/2,x + CELL_SIZE, y-offset + CELL_ROUND/2)
    elif obj == "two" : 
        return (x + CELL_SIZE - CELL_ROUND/2,y+offset + CELL_ROUND/2,x + CELL_SIZE, y+offset + CELL_ROUND/2)
    else : print("T'as loupé ta demande de line right")
    
def lineLeft(obj,x,y,CELL_ROUND,CELL_SIZE) : 
    offset = int(CELL_ROUND/4)
    if obj == "solo" : 
        return (x - CELL_ROUND/2,y + CELL_ROUND/2,x, y + CELL_ROUND/2)
    elif obj == "one" : 
        return (x - CELL_ROUND/2,y-offset + CELL_ROUND/2,x , y-offset + CELL_ROUND/2)
    elif obj == "two" : 
        return (x - CELL_ROUND/2,y+offset + CELL_ROUND/2,x , y+offset + CELL_ROUND/2)
    else : print("T'as loupé ta demande de line left")