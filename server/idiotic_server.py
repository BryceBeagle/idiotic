import json
import logging

from flask import Flask
from flask_sockets import Sockets

from control.idiotic_controller import IdioticController

# Create a new Flask app with sockets
app = Flask(__name__)
app.config['DEBUG'] = True
socketio = Sockets(app)

controller = IdioticController()


@socketio.route('/embedded')
def handle_json(ws):
    """Called whenever a websocket connects to the system at /embedded

    The purpose of this function is to parse the json-bodied message.

    There are three types of JSON messages: update, get (unimplemented), and
    hello.

    An IdioticDevice sends a hello message attempting to establish connection to
    the server, usually during its initialization sequence. If the message is a
    hello message, the json structure must contain a class type in the "class"
    key to be associated with the uuid.

    Every JSON message must have the uuid of the sender device.

    hello structure:
    {
      "hello": null,
      "uuid": "13:8C:14:87:B7:AD",
      "class": "DoorSensor"
    }

    update structure:
    {
      "uuid": "13:8C:14:87:B7:AD",
      "update": {
        "door_state": 1,
        "some_value": "some string"
      }
    }

    get structure:
    [unimplemented]

    """
    while not ws.closed:
        message = ws.receive()

        # Print the message for debugging
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

        if 'get' in req_json:
            raise NotImplementedError


@app.route("/")
def hello():
    """For debugging. Allows a user to verify they have access to the server"""
    return "Hello World"


if __name__ == "__main__":

    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    from werkzeug.debug import DebuggedApplication
    from werkzeug.serving import run_with_reloader

    server = pywsgi.WSGIServer(('0.0.0.0', 5000), DebuggedApplication(app, True),
                               handler_class=WebSocketHandler)
    run_with_reloader(server.serve_forever())
