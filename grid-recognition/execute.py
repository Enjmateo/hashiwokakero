import subprocess

# Chemin d'exécutions pour la détection des chiffres d'une image

# PARTIE 1 : Préprocessing
print("Preprocessing image")

# Partie 2 : Détection utilisant Yolo
print("Détection")
with open("detect.log", "w") as f:
    subprocess.run(["python3.9", "YoloV5/detect.py", "--weights", "YoloV5/Hashiwokakero-model/weights/best.pt", "--img", "640", "--conf", "0.3", "--source", "image.jpg", "--save-txt", "--save-conf", "--project=results/", "--name=detected"], stdout=f, stderr=f)
#subprocess.run(["python3.9", "YoloV5/detect.py", "--weights", "YoloV5/Hashiwokakero-model/weights/best.pt", "--img", "640", "--conf", "0.3", "--source", "image.jpg", "--save-txt", "--save-conf", "--project=results/", "--name=detected"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Partie 3 : Post processing
    print("Post processing")
    subprocess.run(["python3.9", "postprocess.py", "3", "results/detected/labels/image.txt"], stdout=f, stderr=f)

# Partie 4 : Nettoyer le dossier
