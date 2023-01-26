import cv2
import os
import numpy as np 

def image_threshold(image_path, threshold=120, outfile="cleaned_image.jpg") : 
    # Check if it's an image 
    if not image_path.endswith(".png") and not image_path.endswith(".jpg"):
        raise ValueError("Need a .png or .jpg file")
    # Transform the image 
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)[1]
    # Save the image
    cv2.imwrite(outfile, thresh)