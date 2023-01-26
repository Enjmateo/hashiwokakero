import sys, csv, cv2
import numpy as np
from utils import *

#Default global variables
PERCENT_TOLERANCE = 0.20 # For the imperfections removing
MATRIX_SIZE = 3
CONFIDENCE_THRESHOLD = 0.70

# Lire les deux matrices
try:
    MATRIX_SIZE = int(sys.argv[1])
    print(sys.argv[2])
    yoloMatrix = readMatrixFromFile(sys.argv[2])
except:
    print("Usage : python detect.py [Matrix size] [grid]")
    print("ERROR : File not found")
    exit(1)

# COUCHE 1 : On enleve les zones de backgrounds détectés à tort
# On enlève les zones détectés trop petites avec une tolérance de PERCENT_TOLERANCE
yoloMatrixCleaned=[]
for l in yoloMatrix:
    if not (l[3]<PERCENT_TOLERANCE*1/MATRIX_SIZE or
            l[4]<PERCENT_TOLERANCE*1/MATRIX_SIZE):
        yoloMatrixCleaned.append(l)


# COUCHE 2 : On rempli la matrice résultat
# Initialiser la matrice vide
resultMatrix = [[[0,0,0,0,0,0,0,0] for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

# On fait des carrés de 1/N de coté
N=MATRIX_SIZE
grid=[]
for i in range(N):
    for j in range(N):
        grid.append([i,j , i*1/N, j*1/N, 1/N, 1/N])

# Maximiser la surface commune entre les carrés de la grille et les carrés de la détection
for l in yoloMatrixCleaned :
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


printMatrix(resultMatrix)