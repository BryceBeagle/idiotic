import logging
import json

from flask import Flask, abort, make_response, request, render_template
from flask_socketio import SocketIO, emit

from control.idiotic_controller import IdioticController
from control.idiotic_devices import (
    DoorSensor, IRSensor, HueLight)  # TODO: Do this automatically

app = Flask(__name__)
app.config['DEBUG'] = True
socketio = SocketIO(app, engineio_logger=True)

logger = logging.getLogger('gunicorn.error')

controller = IdioticController()


@socketio.on('json')
def handle_json(message):
    print(f'received_json: {message}')

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})


# @socketio.on('connect')


#
# @app.route("/modules/", methods=['POST'])
# def module_handler():
#     """Set or get attribute of IotDevice
#
#     json structure:
#         {"set" : [
#            {
#             "id"    : <uuid of IotDevice instance>,
#             "attr"  : <attribute name>,
#             "value" : <value>,
#            },
#            {
#             "class" : <type(IotDevice())>,
#             "name"  : <IotDevice().name>,
#             "attr"  : <attribute name>,
#             "value" : <value>
#            }
#         ],
#         "get : [
#            {
#             "id"    : <uuid of IotDevice instance>,
#             "attr"  : <attribute name>
#            },
#            {
#             "class" : <type(IotDevice())>,
#             "name"  : <IotDevice().name>,
#             "attr"  : <attribute name>
#            }
#         ]}
#
#     json contains a list of set and/or get commands. Either id, or class+name, must be specified in json
#
#     :param module_class:
#     :return:
#     """
#
#     req_json = request.get_json()
#
#     # Ensure set and/or get in Json body
#     if 'set' not in req_json and 'get' not in req_json:
#         abort(501, "Request must have a get and/or a set key in Json body")
#
#     if 'set' in req_json:
#         for get_cmd in req_json['set']:
#             attr  = get_cmd["attr" ]
#             value = get_cmd["value"]
#             klass = get_cmd["class"] if "class" in get_cmd else None
#             name  = get_cmd["name" ] if "name"  in get_cmd else None
#             id    = get_cmd["id"   ] if "id"    in get_cmd else None
#
#             # Make sure either id, or klass+name was specified
#             # TODO: Use error response
#             assert id or (klass and name)
#
#             controller.set_attr(attr, value, klass, name, id)
#
#             r = make_response("Value set")
#             return r
#
#     if 'get' in req_json:
#
#         resp = []
#
#         for get_cmd in req_json['set']:
#             attr  = get_cmd["attr" ]
#             klass = get_cmd["class"] if "class" in get_cmd else None
#             name  = get_cmd["name" ] if "name"  in get_cmd else None
#             id    = get_cmd["id"   ] if "id"    in get_cmd else None
#
#             # Make sure either id, or klass+name was specified
#             # TODO: Use error response
#             assert id or (klass and name)
#
#             if id:
#                 # Get value using uuid. Makes use of controller's __getitem__ magic method
#                 value = controller[id].get()
#             else:
#                 # Get value using uuid. Makes use of controller's __getattr__ magic method
#                 value = getattr(controller, klass)[name].get()
#
#             # TODO: Respond with _both_ id and class+name
#             resp.append({"id"    : id,
#                          "class" : klass,
#                          "name"  : name,
#                          "attr"  : attr,
#                          "value" : value})
#

@app.route("/")
def hello():
    return render_template('index.html', async_mode=socketio.async_mode)


if __name__ == "__main__":

    socketio.run(app, host="0.0.0.0")
