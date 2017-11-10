import logging
import json

from   flask import Flask
from   flask import request
from   flask import make_response
from   flask import helpers

app = Flask(__name__)
app.config['DEBUG'] = True

# https://github.com/dialogflow/fulfillment-webhook-weather-python/blob/master/app.py
# https://pastebin.com/wpzqtMWK

logger = logging.getLogger('gunicorn.error')


@app.route("/")
def hello():
    return "Test 2"


@app.route("/modules/door")
def door_handler():

    logger.error("Test")

    req = request.get_json(silent=True, force=True)

    print("Request: \n {}".format(json.dumps(req, indent=4)))

    with open('state', 'w+') as fi:
        fi.write(req['status'] + "\n")

    return "OK"


@app.route('/webhook', methods=['POST'])
def webhook():

    req = request.get_json(silent=True, force=True)

    print("Request: \n {}".format(json.dumps(req, indent=4)))

    res = {"speech"        : "the door is {}".format(get_door_state()),
           "displayText"   : ""                                       ,
           "data"          : {}                                       ,
           "contextOut"    : []                                       ,
           "source"        : "Your mom"                               ,
           "followupEvent" : {}                                       }

    r = make_response(json.dumps(res))
    r.headers['Content-Type'] = 'application/json'

    return r


def get_door_state():
    with open('state') as fi:
        state = fi.readline()

    print("State: {}".format(state))

    return state


if __name__ == "__main__":

    app.run(host="0.0.0.0")
