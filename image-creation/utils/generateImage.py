from PIL import Image, ImageDraw, ImageFont
from Water import Water
from VertexOutput import VertexOutput
from Noeud import Noeud
from lineForCircle import * 
import numpy as np
import cv2

def generate_image(objects):
    # Color of the graph
    color_line = (1, 1, 1)
    color_vertix = (1, 1, 1)
    color_text = (1, 1, 1)
    
    # The width and height of each individual cell in the image
    CELL_SIZE = 200
    CELL_ROUND = 2/3 * CELL_SIZE 
    offset = CELL_SIZE//10

    # Text constants 
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = CELL_SIZE//100
    font_bold = CELL_SIZE//100 + 2

    # Determine the dimensions of the image based on the number of rows and columns of objects
    num_rows = len(objects)
    num_cols = len(objects[0])
    print(num_rows, num_cols)

    # Create a blank image with a black background
    img = np.zeros((num_rows * CELL_SIZE, num_cols * CELL_SIZE, 3), np.uint8)

    # Go through all the objects and draw them on the image
    for row_index, row in enumerate(objects):
        for col_index, obj in enumerate(row):
            x = col_index * CELL_SIZE
            y = row_index * CELL_SIZE
            cX = int(x + CELL_SIZE/2)
            cY = int(y + CELL_SIZE/2)
            #cv2.rectangle(img, (x, y), (x + CELL_SIZE, y + CELL_SIZE), (255, 0, 0), 10)
            if obj.k != 0 :
                # Circle
                cv2.circle(img, (cX, cY), int(CELL_ROUND*0.5), color_vertix, 5)
                # Text 
                text = str(obj.k)
                textsize = cv2.getTextSize(text, font, font_size, font_bold)[0]
                textX = x + (CELL_SIZE - textsize[0]) // 2
                textY = y + (CELL_SIZE + textsize[1]) // 2
                cv2.putText(img, text, (textX, textY), font, font_size, color_text, font_bold)
                # Lines
                if (obj.Top) : 
                    y1 = y
                    y2 = int(y+15/100*CELL_SIZE)
                    x0 = int(x+CELL_SIZE//2)
                    if (obj.Top == 1): 
                        cv2.line(img, (x0,y1),(x0, y2), color_line, 5)
                    if (obj.Top == 2): 
                        cv2.line(img, (x0-offset,y1),(x0-offset, y2), color_line, 5)
                        cv2.line(img, (x0+offset,y1),(x0+offset, y2), color_line, 5)
                if (obj.Bottom) : 
                    y1 = int(y+CELL_SIZE-(15/100*CELL_SIZE))
                    y2 = int(y+CELL_SIZE)
                    x0 = int(x+CELL_SIZE//2)
                    if (obj.Bottom == 1): 
                        cv2.line(img, (x0,y1),(x0, y2), color_line, 5)
                    if (obj.Bottom == 2): 
                        cv2.line(img, (x0-offset,y1),(x0-offset, y2), color_line, 5)
                        cv2.line(img, (x0+offset,y1),(x0+offset, y2), color_line, 5)
                if (obj.Left) :
                    x1 = x
                    x2 = int(x+15/100*CELL_SIZE)
                    y0 = int(y+CELL_SIZE//2)
                    if (obj.Left == 1): 
                        cv2.line(img, (x1,y0),(x2, y0), color_line, 5)
                    if (obj.Left == 2): 
                        cv2.line(img, (x1,y0-offset),(x2, y0-offset), color_line, 5)
                        cv2.line(img, (x1,y0+offset),(x2, y0+offset), color_line, 5)
                if (obj.Right) :
                    x1 = int(x+CELL_SIZE-(15/100*CELL_SIZE))
                    x2 = int(x+CELL_SIZE)
                    y0 = int(y+CELL_SIZE//2)
                    if (obj.Right == 1): 
                        cv2.line(img, (x1,y0),(x2, y0), color_line, 5)
                    if (obj.Right == 2): 
                        cv2.line(img, (x1,y0-offset),(x2, y0-offset), color_line, 5)
                        cv2.line(img, (x1,y0+offset),(x2, y0+offset), color_line, 5)

            else:
                # Draw lines in the specified directions
                if (obj.Vertical) : 
                    y1 = y
                    y2 = int(y+CELL_SIZE)
                    x0 = int(x+CELL_SIZE//2)
                    if (obj.Vertical == 1): 
                        cv2.line(img, (x0,y1),(x0,y2),color_line, 5)
                    elif (obj.Vertical == 2):
                        cv2.line(img, (x0-offset,y1),(x0-offset,y2), color_line, 5)
                        cv2.line(img, (x0+offset,y1),(x0+offset,y2), color_line, 5)
                if (obj.Horizontal) :
                    x1 = x
                    x2 = int(x+CELL_SIZE)
                    y0 = int(y+CELL_SIZE//2)
                    if (obj.Horizontal == 1):
                        cv2.line(img, (x1,y0),(x2,y0), color_line, 5)
                    elif (obj.Horizontal == 2):
                        cv2.line(img, (x1,y0-offset),(x2, y0-offset), color_line, 5)
                        cv2.line(img, (x1,y0+offset),(x2, y0+offset), color_line, 5)

    # Turn black to white 
    for i, row in enumerate(img):
        for j, pixel in enumerate(row):
            if (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0):
                img[i][j] = [255,255,255]

    # Save and return the image 
    name = "./../images/oui.jpg"
    cv2.imwrite(name, img)
    return (name)


