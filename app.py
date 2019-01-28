import json

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/webhooks", methods=["GET", "POST"])
def webhooks():
    data = json.loads(request.data)
    f = open("fits_req.py", "w+")
    f.write(str(data))
    f.close()
    return jsonify("working")


if __name__ == '__main__':
    app.run()
