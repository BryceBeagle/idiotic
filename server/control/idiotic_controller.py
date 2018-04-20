from collections import defaultdict
import json

from .idiotic_device import IdioticDevice
from .idiotic_routine import IdioticRoutine
from .idiotic_trigger import IdioticTrigger
from .idiotic_event import IdioticEvent

from .device_drivers.hue import HueBridge


class IdioticController:
    """The main controller for the Idiotic system

    Manages all devices and routines. At startup, loads routine, event, and
    device configurations from `server/model/`.

    Currently has a hardcode to initialize the HueBridge in __init__, but this
    should be removed in the future en lieu of a more modular solution.
    """

    def __init__(self):

        self.device_names = defaultdict(dict)
        self.device_uuids = {}

        HueBridge(self)  # TODO: This shouldn't be hardcoded

        self.events = {}
        self.routines = {}

        # Load json configurations
        self.create_devices_from_json('model/devices.json')
        self.create_events_from_json('model/events.json')
        self.create_routines_from_json('model/routines.json')

    def __getattr__(self, device_type):
        """Used when getting dict of IdioticDevices of device_type

        Uses . operator
        """
        if device_type in self.device_names:
            return self.device_names[device_type]

    def __getitem__(self, uuid):
        """Used when getting IdioticDevice instance by uuid

        Uses [] operator
        """
        if uuid in self.device_uuids:
            return self.device_uuids[uuid]

    def __contains__(self, uuid):
        """Return True if self.device_uuids contains uuid

        Allows usage of 'in' keyword on controller
        """
        return uuid in self.device_uuids

    def create_devices_from_json(self, filename: str):
        """Create IdioticDevice instances using json configuration"""
        with open(filename) as fi:
            devices = json.load(fi)

        for klass_name, klass_data in devices.items():
            for device in klass_data:
                if device['uuid'] is None:
                    raise NotImplementedError(
                        "null uuids in device json config files not supported")
                self.new_device(klass_name, device['uuid'])

    def create_events_from_json(self, filename: str):
        """"Create IdioticEvent instances using json configuration"""

        with open(filename) as fi:
            events = json.load(fi)

        for event_name, event_data in events.items():
            actions = []
            for action in event_data['actions']:

                if action['device']['uuid'] is not None:
                    device = self.device_uuids[action['device']['uuid']]

                else:
                    class_dict = self.device_names[action['device']['class']]
                    device = class_dict[action['device']['name']]

                if 'attribute' in action:
                    attribute = action['attribute']
                    value = action['value']

                    # https://stackoverflow.com/a/10452819/8134178
                    actions.append(lambda device=device,
                                          attribute=attribute,
                                          value=value:
                                   getattr(device, attribute).set(value))

                elif 'behavior' in action:
                    behavior = action['behavior']
                    value = action['value']  # TODO: Support multiple arguments

                    # https://stackoverflow.com/a/10452819/8134178
                    # https://stackoverflow.com/a/10452819/8134178
                    actions.append(lambda device=device,
                                          behavior=behavior,
                                          value=value:
                                   # Directly call behavior function
                                   getattr(device, behavior)(value))

                else:
                    raise AttributeError('Action missing behavior or attribute')

            # TODO: Conditionals

            self.events[event_name] = IdioticEvent(actions)

    def create_routines_from_json(self, filename: str):
        """Create IdioticEvent instances using json configuration

        Each routine needs a trigger, conditional (can be null), and an event
        list

        Each event in the event list must have a corresponding entry in the
        events.json

        json structure of file:
        {
          "Demo Light on temp": {
            "trigger": {
              "device": {
                "uuid": "6A:C6:3A:AC:89:EB",
                "class": null,
                "name": null
              },
              "attribute": "temp",
              "check": "check_gt",
              "value": 30
            },
            "conditional": null,
            "events": [
              "Demo Light on"
            ]
          }
        }

        """

        with open(filename) as fi:
            routines = json.load(fi)

        # Iterate over routines expressed in file
        for routine_name, routine_data in routines.items():

            # Create list of events using events pulled from events.json
            # Each entry must have a corresponding entry in the events.json
            events = [self.events[event] for event in routine_data['events']]

            routine = IdioticRoutine(events, None)  # TODO: Conditionals

            trigger = routine_data['trigger']

            if trigger['device']['uuid']:
                trig_dev = self.device_uuids[trigger['device']['uuid']]
            else:
                klass = trigger['device']['class']
                name = trigger['device']['name']
                trig_dev = self.device_names[klass][name]

            attr = getattr(trig_dev, trigger['attribute'])

            trig = IdioticTrigger(routine, attr, trigger['check'],
                                  trigger['value'])
            trig.name = routine_name

            self.routines[routine_name] = routine

    def new_device(self, klass: str, uuid: str, ws=None):
        """Create a new IdioticDevice
        :param klass: IdioticDevice class type
        :param uuid: UUID of IdioticDevice (likely MAC address)
        :param ws: [Optional] Websocket instance
        :return:
        """
        try:
            # Import class and instantiate an instance of it.
            mod = __import__('device_drivers', globals(), locals(), [klass], 1)
            # Note the instantiation at the end
            dev = getattr(mod, klass)()
        except ImportError:
            print(f"Error importing {klass} from device_drivers")
            return None

        dev.ws.update(ws)
        dev.uuid.update(uuid)

        self.add_device(dev)

    def add_device(self, device: IdioticDevice) -> None:
        """Add an existing IotDevice instance to the device dicts.

        device_uuids is a dict of devices by uuid
        device_names is a dict of devices by class type, then name

        :param device: Instance of IotDevice subclass
        :return: None
        """

        # Dict of UUIDs
        if device.uuid.get() is not None:
            self.device_uuids[device.uuid.get()] = device
        else:
            print(f"Warning: device {device} has no uuid")

        # Dict of device types and names
        self.device_names[device.__class__.__name__][device.name.get()] = device


if __name__ == '__main__':
    from .device_drivers import IRSensor

    controller = IdioticController()

    controller.add_device(IRSensor())

    # Access to IdioticDevice instances
    dr1 = controller.HueLight["Dining Room 1"]
    dr2 = controller.HueLight["Dining Room 2"]

    # Create event (Invert brightness)
    actions = [lambda: dr1.brightness.set(254 - dr1.brightness.get())]
    event = IdioticEvent(actions)

    # Create routine
    routine = IdioticRoutine(event)

    # Subscribe routine using IdioticTrigger
    trigger = IdioticTrigger(routine,
                             dr2.brightness, IdioticTrigger.check_gt, 100)

    dr2.brightness.set(100)
    dr2.brightness.set(254)

    pass  # Pause debugger here as no event loop
