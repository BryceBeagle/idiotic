import json
import logging

from flask import Flask
from flask_sockets import Sockets

from control.idiotic_controller import IdioticController


app = Flask(__name__)
app.config['DEBUG'] = True
socketio = Sockets(app)

logger = logging.getLogger('gunicorn.error')

controller = IdioticController()


@socketio.route('/embedded')
def handle_json(ws):
    """Set or get attribute of IdioticDevice

    json structure:
        {"set" : [
           {
            "id"    : <uuid of IdioticDevice instance>,
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
    while not ws.closed:
        message = ws.receive()

        print(message)

        req_json = json.loads(message)

        # Module just started up
        if 'hello' in req_json:

            # Use existing device instance if already exists
            # TODO: Change device type if device "hello"s as a different type
            if req_json['uuid'] in controller:
                controller[req_json['uuid']].ws.update(ws)

            # Otherwise, create one
            else:
                controller.new_device(req_json['class'], req_json['uuid'], ws)

        # Otherwise, it needs a set or a get
        elif 'update' not in req_json and 'get' not in req_json:
            print(f"Invalid message: {message}")
            continue

        if 'update' in req_json:
            for attr, value in req_json['update'].items():
                try:
                    getattr(controller[req_json['uuid']], attr).update(value)
                except (AttributeError, TypeError):
                    logging.error(f"Attribute {attr} does not exist or has no "
                                  f"update function")


@app.route("/")
def hello():
    return "Hello World"


if __name__ == "__main__":

    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    from werkzeug.debug import DebuggedApplication
    from werkzeug.serving import run_with_reloader

    server = pywsgi.WSGIServer(('0.0.0.0', 5000), DebuggedApplication(app, True),
                               handler_class=WebSocketHandler)
    run_with_reloader(server.serve_forever())
