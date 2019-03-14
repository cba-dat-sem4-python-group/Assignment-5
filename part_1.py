from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    return ("", 200) if request.get_json()['password'] == "aa" else ("", 403)
