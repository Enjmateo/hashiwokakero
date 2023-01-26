from flask import Flask, request, jsonify, send_file
from generateImage import generate_image
from jsonToArrayofObjects import listToArrayOfObjects
from os import path
from flask import request

app = Flask(__name__)

# Getter to solve the grid
@app.route('/create-image', methods=['POST'])
def createImage():
    json_file = request.get_json()
    filename = generate_image(listToArrayOfObjects(json_file))

    try:
        return send_file(filename, mimetype='image/jpeg')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
