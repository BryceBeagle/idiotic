from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/")
def hello():
    print("Hello World")
    return "Hello World"


@app.route("/alarm/", methods=['POST'])
def test():
    print(request.get_json())
    return 501

app.run(port=8008)