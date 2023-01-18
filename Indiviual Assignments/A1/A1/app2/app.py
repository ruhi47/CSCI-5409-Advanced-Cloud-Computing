import hashlib

from flask import Flask, request

app = Flask(__name__)


@app.route('/checksum', methods=["POST"])
def generate_checksum():
    data = request.json
    file = data.get("file")
    md5_hash = hashlib.md5()

    a_file = open("/etc/data/"+file, "rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()

    return {"file": file, "checksum": digest}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

# https://www.adamsmith.haus/python/answers/how-to-generate-an-md5-checksum-of-a-file-in-python
