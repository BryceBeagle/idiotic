from collections import defaultdict

from control.idiotic_device import IdioticDevice
from control.idiotic_routine import IdioticRoutine
from control.idiotic_trigger import IdioticTrigger
from control.idiotic_event import IdioticEvent


class IdioticController:

    def __init__(self):
        self.device_names = defaultdict(dict)
        self.device_uuids = {}

        self.routines = {None: None}
        """Registry of trigger:routine mappings
        
        None key corresponds to routines that do not have any triggers (ie. can only be triggered manually)
        """

    def __getattr__(self, device_type):
        """Used when getting dict of IdioticDevices of device_type"""
        if device_type in self.device_names:
            return self.device_names[device_type]

    def __getitem__(self, uuid):
        """Used when IdioticDevice instance by uuid"""
        if uuid in self.device_uuids:
            return self.device_uuids[uuid]

    def new_ws_device(self, klass: str, uuid: str, ws):
        """ Create a new IdioticDevice that relies on websockets
        :param klass: IdioticDevice class type
        :param uuid: UUID of IdioticDevice (likely MAC address)
        :param ws: Websocket instance
        :return:
        """
        try:
            # Import class and instantiate an instance of it. Note the instantiation at the end
            mod = __import__('idiotic_devices', globals(), locals(), [klass], 1)
            dev = getattr(mod, klass)()
        except ImportError:
            print(f"Error importing {klass} from idiotic_devices")
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
        self.device_uuids[device.uuid.get()] = device

        # Dict of device types and names
        self.device_names[device.__class__.__name__][device.name.get()] = device


if __name__ == '__main__':

    from .idiotic_devices.hue import HueBridge
    from .idiotic_devices import IRSensor

    controller = IdioticController()

    bridge = HueBridge(controller)

    controller.add_device(IRSensor())

    # Access to IdioticDevice instances
    dr1 = controller.HueLight["Dining Room 1"]
    dr2 = controller.HueLight["Dining Room 2"]

    # Create event
    actions = [lambda: dr1.brightness.set(254 - dr1.brightness.get())]  # Invert brightness
    event = IdioticEvent(actions)

    # Create routine
    routine = IdioticRoutine(event)

    # Subscribe routine using IdioticTrigger
    trigger = IdioticTrigger(routine, dr2.brightness, IdioticTrigger.check_gt, 100)  # dr2.brightness > 100

    dr2.brightness.set(100)
    dr2.brightness.set(254)

    pass  # Pause debugger here as no event loop
