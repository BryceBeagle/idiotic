from collections     import defaultdict

from hue             import HueBridge, HueLight
from ir_sensor       import IRSensor

from iot_device      import IotDevice
from iot_routine     import IotRoutine
from iot_trigger     import IotTrigger
from iot_conditional import IotConditional
from iot_event       import IotEvent
from iot_watch       import IotWatch


class IotController:

    def __init__(self):
        self.devices = defaultdict(dict)

        self.routines = {None: None}
        """Registry of trigger:routine mappings
        
        None key corresponds to routines that do not have any triggers (ie. can only be triggered manually)
        """

    def add_device(self, device: IotDevice):
        """Create a a new IotDevice instance

        :param device: Instance of IotDevice subclass
        :return: None
        """

        class_type = device.__class__.__name__

        # Use device's name if it has one, else its id()
        name = str(id(device)) if device.name is None else device.name

        self.devices[class_type][name] = device

    def get_attr(self, cls: type(IotDevice), name: str, attr: str):
        """Get an attribute from a device

        :param cls:  IotDevice subclass
        :param name: Name of instance of class
        :param attr: Name of desired attribute
        :return:     Value of attribute
        """

        # TODO: Allow access using either id() or name

        if attr in cls.attributes:

            device = self.devices[cls.__name__][name]
            return getattr(device, attr)

    def set_attr(self, cls: type(IotDevice), name: str, attr: str, value):
        """Sets an attribute of an IotDevice instance to a value

        :param cls:   IotDevice subclass
        :param name:  Name of instance of class
        :param attr:  Name of attribute
        :param value: Value to set attribute to
        :return:      None
        """

        if attr in cls.attributes:
            device = self.devices[cls.__name__][name]
            setattr(device, attr, value)

    def set_routine(self, trigger: IotTrigger, routine: IotRoutine):
        pass


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

    controller.set_attr(HueLight, "Dining Room 2", "brightness", 0)
    assert controller.get_attr(HueLight, "Dining Room 2", "brightness") == 0
    time.sleep(1)
    controller.set_attr(HueLight, "Dining Room 2", "brightness", 254)  # 254 is max for whatever reason
    assert controller.get_attr(HueLight, "Dining Room 2", "brightness") == 254


def _test_conditionals():

    value1 = lambda: controller.get_attr(HueLight, "Dining Room 1", "brightness")
    value2 = lambda: controller.get_attr(HueLight, "Dining Room 2", "brightness")

    print(f"Room1: {value1()} | Room2 {value2()}")
    conditional = IotConditional(value1, "==", value2)
    print(bool(conditional))

    controller.set_attr(HueLight, "Dining Room 2", "brightness", 0)

    print(f"Room1: {value1()} | Room2 {value2()}")
    conditional = IotConditional(value1, "==", value2)
    print(bool(conditional))


if __name__ == '__main__':

    controller = IotController()

    bridge = HueBridge()

    for light in bridge.lights:
        controller.add_device(HueLight(light.light_id))

    controller.add_device(IRSensor())

    action_list = [lambda: controller.set_attr(HueLight, "Bryce's Room", "brightness", 0)]

    value1 = lambda: controller.get_attr(HueLight, "Dining Room 1", "brightness")
    value2 = lambda: controller.get_attr(HueLight, "Dining Room 2", "brightness")
    conditional = IotConditional(value1, "==", value2)

    watch = IotWatch(lambda: controller.get_attr(HueLight, "Dining Room 1", "brightness"), ">", 150)
    trigger = IotTrigger(watch)

    routine = IotRoutine(trigger, action_list, conditional)
