from flask import Flask, request, jsonify
import numpy as np
import cv2, shutil,os
from postprocess import postprocess
from postprocess import decoup
from preprocess import image_threshold
import subprocess

app = Flask(__name__)

# Getter to solve the grid
@app.route('/recognize', methods=['POST'])
def recognizeGrid():
    if os.path.exists("Logs"):
        shutil.rmtree("Logs/")
    if os.path.exists("results"):
        shutil.rmtree("results/")
    os.makedirs("Logs")

    # Partie 1 : Recevoir et télécharger l'image
    print("Téléchargement de l'image")
    r = request
    MatrixSize = int(request.args.get('size'))
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("raw_image.jpg", img)

    # PARTIE 2 : Préprocessing
    print("Preprocessing image")
    image_threshold("raw_image.jpg", threshold=100, outfile="cleaned_image.jpg")
    shutil.copyfile("raw_image.jpg", "Logs/raw_image.jpg")

    # Partie 3 : Détection utilisant Yolo
    print("Première détection")
    if not os.path.exists("results"):
        os.makedirs("results")
    with open("detect.log", "w") as f:
        subprocess.run(["python3.9", "YoloV5/detect.py", "--weights", "YoloV5/Hashiwokakero-model/EXP22/weights/best.pt", "--img", "640", "--conf", "0.3", "--source", "cleaned_image.jpg", "--save-txt", "--save-conf", "--project=results/", "--name=detected"], stdout=f, stderr=f)
    shutil.copyfile("detect.log", "Logs/detect1.log")
    
    # Partie 4 : Détection de l'emplacement de la grille
    print("Détection de l'emplacement de la grille")
    matrixResult = decoup(MatrixSize, CONFIDENCE_THRESHOLD=0, matrixPath="results/detected/labels/cleaned_image.txt")
    shutil.copyfile("cleaned_image.jpg", "Logs/cleaned_image.jpg")  # Plus besoin
    shutil.copyfile("results/detected/cleaned_image.jpg", "Logs/detected_image1.jpg")
    shutil.copyfile("results/detected/labels/cleaned_image.txt", "Logs/detected_labels1.txt")
    shutil.copyfile("postprocess_logs.out", "Logs/decoup.log")

    
    # Partie 5 : Treshold sur l'image coupée
    print("Treshold sur l'image coupée")
    image_threshold("cropped_image.jpg", threshold=160, outfile="net_image.jpg")
    shutil.copyfile("cropped_image.jpg", "Logs/cropped_image.jpg")
    shutil.copyfile("net_image.jpg", "Logs/net_image.jpg")

    # Partie 6 : Détection précise
    shutil.rmtree("results/")
    print("Détection précise")
    if not os.path.exists("results"):
        os.makedirs("results")
    with open("detect.log", "w") as f:
        subprocess.run(["python3.9", "YoloV5/detect.py", "--weights", "YoloV5/Hashiwokakero-model/EXP22/weights/best.pt", "--img", "640", "--conf", "0.3", "--source", "net_image.jpg", "--save-txt", "--save-conf", "--project=results/", "--name=detected"], stdout=f, stderr=f)
    shutil.copyfile("detect.log", "Logs/detect2.log")
    shutil.copyfile("results/detected/net_image.jpg", "Logs/net_image.jpg")
    shutil.copyfile("results/detected/labels/net_image.txt", "Logs/net_image.txt")
    
    # Partie 7 : Génération des résultats
    print("Post processing")
    matrixResult = postprocess(MatrixSize, CONFIDENCE_THRESHOLD=0)
    shutil.copyfile("postprocess_logs.out", "Logs/postprocess.log")

    # Partie 4 : Nettoyer le dossier
    print("Cleaning folder")
    if os.path.exists("results"):
        shutil.rmtree("results/")
    if os.path.exists("./*.jpg"):
        os.remove("./*.jpg")
    if os.path.exists("./*.out"):
        os.remove("./*.out")
    if os.path.exists("./*.log"):
        os.remove("./*.log")


    # Partie 5 : Retourner un resultat propre
    jsonResponse = jsonify(matrixResult)
    return jsonResponse

if __name__ == '__main__':
    app.run(host="0.0.0.0")

