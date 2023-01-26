import sys, csv, cv2
import numpy as np
from utils import *

def decoup(MATRIX_SIZE=3, PERCENT_TOLERANCE=0.50, CONFIDENCE_THRESHOLD=0.70, matrixPath="results/detected/labels/cleaned_image.txt", image="raw_image.jpg"):

    # Lire les deux matrices
    try:
        yoloMatrix = readMatrixFromFile(matrixPath)
    except:
        print("ERROR : File not found")
        exit(1)

    # COUCHE 1 : On enleve les zones de backgrounds détectés à tort
    # On enlève les zones détectés trop petites avec une tolérance de PERCENT_TOLERANCE
    yoloMatrixCleaned=[]
    if CONFIDENCE_THRESHOLD!=0:
        sum=0; cnt=0
        for l in yoloMatrix:
            if (l[5]>CONFIDENCE_THRESHOLD): # Calcule la moyenne des tailles fiables 
                sum += l[3]+l[4]
                cnt += 2
        meanSquareHeight = sum/cnt
        for l in yoloMatrix:
            if((l[3]+l[4])/2 > PERCENT_TOLERANCE*meanSquareHeight): # Ajoute que les éléments à la bonne taille.
                yoloMatrixCleaned.append(l)
    else :
        yoloMatrixCleaned=yoloMatrix  

    # Afficher dans logs
    f = open("postprocess_logs.out", "w")
    f.write("Couche 1 :")
    for m in yoloMatrixCleaned:
        txt="" 
        txt = txt + str(m[0]) + " "
        f.write(txt)


    # COUCHE 2 : On rogne l'image à la taille pile de la grille  
    def maxColumn(L):    
        return list(map(max, zip(*L)))
    def minColumn(L):    
        return list(map(min, zip(*L)))

    matMax = maxColumn(yoloMatrixCleaned)
    matMin = minColumn(yoloMatrixCleaned)
    img = cv2.imread(image)
    limitX=img.shape[1]
    limitY=img.shape[0]
    x1=int((abs(matMin[1]-matMax[3]/2))*limitX)
    x2=int((abs(matMax[1]+matMax[3]/2))*limitX)
    y1=int((abs(matMin[2]-matMax[4]/2))*limitY)
    y2=int((abs(matMax[2]+matMax[4]/2))*limitY)

    if y2>limitY : y2=limitY
    if x2>limitX : x2=limitX
    crop_image = img[y1:y2, x1:x2]
    cv2.imwrite("cropped_image.jpg", crop_image)


def postprocess(MATRIX_SIZE=3, PERCENT_TOLERANCE=0.50, CONFIDENCE_THRESHOLD=0.70, matrixPath="results/detected/labels/net_image.txt"):

    # Lire la deux matrices
    try:
        netMatrix = readMatrixFromFile(matrixPath)
    except:
        print("ERROR : File not found")
        exit(1)

    # COUCHE 3 : On rempli la matrice résultat
    # Initialiser la matrice vide
    resultMatrix = [[[0,0,0,0,0,0,0,0] for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

    # On fait des carrés de 1/N de coté
    N=MATRIX_SIZE
    grid=[]
    for i in range(N):
        for j in range(N):
            grid.append([i,j , i*1/N, j*1/N, 1/N, 1/N])

    # Maximiser la surface commune entre les carrés de la grille et les carrés de la détection
    for l in netMatrix :
        maxVal=0
        maxInd=-1
        cp=l
        # yolo donne le centre du cercle, on place le point en haut à gauche
        l[1]=cp[1]-cp[3]/2
        l[2]=cp[2]-cp[4]/2
        for g in grid:
            if maxVal <  intersection_area(l[1:5],g[2:]):
                maxVal = intersection_area(l[1:5],g[2:])
                maxInd=(g[0],g[1])
        # Placer l'élement trouvé dans la matrice finale
        resultMatrix[maxInd[1]][maxInd[0]][int(l[0])]=int(l[5]*100)

    f = open("postprocess_logs.out", "w")
    f.write("Couche 2 :")
    for m in resultMatrix:
        f.newlines
        f.newlines
        txt="" 
        txt = txt + str(m) + " \n"
        f.write(txt)
        f.newlines

    obj={"size":MATRIX_SIZE,
    "grid":resultMatrix}

    return obj
