import json

from flask import Flask
from flask import request
from flask import make_response


app = Flask(__name__)

# https://github.com/dialogflow/fulfillment-webhook-weather-python/blob/master/app.py
# https://pastebin.com/wpzqtMWK

@app.route("/modules/door", methods=['POST'])
def door_handler():

    req = request.get_json(silent=True, force=True)

    print("Request: \n {}".format(json.dumps(req, indent=4)))

    with open('state', 'w+') as fi:
        fi.write(req['status'])

    return "OK"


@app.route('/webhook')
def webhook():

    req = request.get_json(silent=True, force=True)

    print("Request: \n {}".format(json.dumps(req, indent=4)))

    res = {"speech" : "the door is {}".format(get_door_state())}

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'

    return r


def get_door_state():
    with open('state') as fi:
        state = fi.readline()

    print("State: {}".format(state))

    return {'state': state}


if __name__ == "__main__":

    port = 5000
    context = ('server.crt', 'server.key')
    app.run(debug=True, port=port, host='0.0.0.0')#, ssl_context=context)
