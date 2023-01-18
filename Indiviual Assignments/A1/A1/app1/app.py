pip3 freeze > requirements.txtfrom copy import deepcopy
from os import path

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/checksum", methods=["POST"])
def validate_json():
    data = request.json
    result = deepcopy(data)

    file = data.get("file")

    if file == "":
        result['error'] = "Invalid JSON input."
        return result

    if file is None or not path.exists("/etc/data/"+file):
        result['error'] = "File not found."
        return result

    response = requests.post("http://app2:5001/checksum", json=result)
    return deepcopy(response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
