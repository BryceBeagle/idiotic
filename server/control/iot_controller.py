from collections import defaultdict

from hue         import HueBridge, HueLight
from ir_sensor   import IRSensor

from iot_device  import IotDevice


class IotController:

    def __init__(self):
        self.devices = defaultdict(dict)

    def add_device(self, device):
        class_type = device.__class__.__name__

        # Use device's name if it has one, else its id()
        name = str(id(device)) if device.name is None else device.name

        self.devices[class_type][name] = device

    def get(self, cls: type(IotDevice), name: str, attr):

        if attr in cls.attributes:

            device = self.devices[cls.__name__][name]
            return getattr(device, attr)

    def set(self, cls: type(IotDevice), name: str, attr: str, value):

        if attr in cls.attributes:
            device = self.devices[cls.__name__][name]
            setattr(device, attr, value)


def _test_random_brightness():

    import random
    import time

    lights = []
    for light in controller.devices[HueLight]:
        if 'Alex Room' in light.groups:
            lights.append((light, light.brightness))
    for _ in range(10):
        time.sleep(.5)
        for light in lights:
            light[0].brightness = random.randint(0, 255)

    time.sleep(5)

    for light in lights:
        light[0].brightness = light[1]


def _test_attributes():

    import time

    controller.set(HueLight, "Dining Room 2", "brightness", 0)
    assert controller.get(HueLight, "Dining Room 2", "brightness") == 0
    time.sleep(1)
    controller.set(HueLight, "Dining Room 2", "brightness", 254)
    assert controller.get(HueLight, "Dining Room 2", "brightness") == 254


if __name__ == '__main__':

    controller = IotController()

    bridge = HueBridge()

    for light in bridge.lights:
        controller.add_device(HueLight(light.light_id))

    controller.add_device(IRSensor())

    _test_attributes()
