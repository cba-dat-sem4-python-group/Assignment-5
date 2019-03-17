from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    attempted_password = request.get_json()['password']
    return ('OK', 200) if attempted_password == "aa" else ('Forbidden', 403)
