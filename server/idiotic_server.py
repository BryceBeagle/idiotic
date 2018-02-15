import logging
import json

from   flask import Flask
from   flask import request
from   flask import make_response

from control.idiotic_controller import IdioticController
from control.idiotic_devices.hue import HueBridge

app = Flask(__name__)
app.config['DEBUG'] = True

# https://github.com/dialogflow/fulfillment-webhook-weather-python/blob/master/app.py
# https://pastebin.com/wpzqtMWK

logger = logging.getLogger('gunicorn.error')
controller = IdioticController()
bridge = HueBridge(controller)


@app.route("/")
def hello():
    return "Test 2"


# @app.route("/modules/door")
# def door_handler():
#
#     logger.error("Test")
#
#     req = request.get_json(silent=True, force=True)
#
#     print("Request: \n {}".format(json.dumps(req, indent=4)))
#
#     with open('state', 'w+') as fi:
#         fi.write(req['status'] + "\n")
#
#     return "OK"

@app.route("/modules/", methods=['POST'])
def module_handler():
    """Set or get attribute of IotDevice

    json structure:
        {"set" : [
           {
            "id"    : <uuid of IotDevice instance>,
            "attr"  : <attribute name>,
            "value" : <value>,
           },
           {
            "class" : <type(IotDevice())>,
            "name"  : <IotDevice().name>,
            "attr"  : <attribute name>,
            "value" : <value>
           }
        ],
        "get : [
           {
            "id"    : <uuid of IotDevice instance>,
            "attr"  : <attribute name>
           },
           {
            "class" : <type(IotDevice())>,
            "name"  : <IotDevice().name>,
            "attr"  : <attribute name>
           }
        ]}

    json contains a list of set and/or get commands. Either id, or class+name, must be specified in json

    :param module_class:
    :return:
    """

    req_json = request.get_json()

    if 'set' in req_json:
        for get_cmd in req_json['set']:
            attr  = get_cmd["attr" ]
            value = get_cmd["value"]
            klass = get_cmd["class"] if "class" in get_cmd else None
            name  = get_cmd["name" ] if "name"  in get_cmd else None
            id    = get_cmd["id"   ] if "id"    in get_cmd else None

            # Make sure either id, or klass+name was specified
            # TODO: Use error response
            assert id or (klass and name)

            controller.set_attr(attr, value, klass, name, id)

            r = make_response("Value set")
            return r

    if 'get' in req_json:

        resp = []

        for get_cmd in req_json['set']:
            attr  = get_cmd["attr" ]
            klass = get_cmd["class"] if "class" in get_cmd else None
            name  = get_cmd["name" ] if "name"  in get_cmd else None
            id    = get_cmd["id"   ] if "id"    in get_cmd else None

            # Make sure either id, or klass+name was specified
            # TODO: Use error response
            assert id or (klass and name)

            value = controller.get_attr(attr, klass, name, id)()

            # TODO: Respond with _both_ id and class+name
            resp.append({"id"    : id,
                         "class" : klass,
                         "name"  : name,
                         "attr"  : attr,
                         "value" : value})


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
