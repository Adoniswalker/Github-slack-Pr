import json

import requests
from flask import Flask, jsonify, request

from authentications.authentication import authenticate

app = Flask(__name__)


@app.route('/')
def get_app_details():
    url = "https://api.github.com/app"
    r = requests.get(url, headers=authenticate())
    return jsonify(r.json())


@app.route("/webhooks", methods=["GET", "POST"])
def webhooks():
    data = json.loads(request.data)
    f = open("fits_req.py", "w+")
    f.write(str(data))
    f.close()
    return jsonify("working")

@app.route("/githubtoken")
def github_auth_token():
    return 

if __name__ == '__main__':
    app.run()
