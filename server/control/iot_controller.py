from collections     import defaultdict
from typing          import Union

from control.hue             import HueBridge, HueLight
from control.ir_sensor       import IRSensor

from control.iot_device      import IotDevice
from control.iot_routine     import IotRoutine
from control.iot_trigger     import IotTrigger
from control.iot_conditional import IotConditional
from control.iot_event       import IotEvent


class IotController:

    def __init__(self):
        self.device_names = defaultdict(dict)
        self.device_uuids = {}

        self.routines = {None: None}
        """Registry of trigger:routine mappings
        
        None key corresponds to routines that do not have any triggers (ie. can only be triggered manually)
        """

    def add_device(self, device: IotDevice) -> None:
        """Add an IotDevice instance to the device dicts.

        device_uuids is a dict of devices by uuid
        device_names is a dict of devices by class type, then name

        :param device: Instance of IotDevice subclass
        :return: None
        """

        # Dict of UUIDs
        self.device_uuids[device.uuid] = device

        # Dict of device types and names
        self.device_names[device.__class__.__name__][device.name] = device

    def get_attr(self,
                 attr: str,
                 cls: type(IotDevice) = None,
                 name: str = None,
                 uuid: int = None):
        """Get an attribute from a device

        :param attr: Name of desired attribute
        :param cls:  [Optional] IotDevice subclass or subclass.__name__
        :param name: [Optional] Name of device
        :param uuid: [Optional] ID of device
        :return:     Value of attribute

        uuid or cls must be specified, but not both. If cls is specified, name must be specified as well
        """
        if attr in cls.attributes:

            if uuid:
                if cls: raise ValueError("Only one of uuid and cls must be specified")

                device = self.device_uuids[uuid]

            elif cls:
                if not name: raise ValueError("If cls is specified, name must be as well")

                if isinstance(cls, IotDevice):
                    cls = cls.__name__

                device = self.device_names[cls][name]

            else: raise ValueError("uuid or cls must be specified")

            return getattr(device, attr)

    def set_attr(self,
                 attr: str,
                 value,
                 cls: type(IotDevice) = None,
                 name: str = None,
                 uuid: int = None):
        """Sets an attribute of an IotDevice instance to a value

        :param attr:  Name of attribute
        :param value: Value to set attribute to
        :param cls:   [Optional] IotDevice subclass
        :param name:  [Optional] Name of device
        :param uuid:  [Optional] ID of device
        :return:      None

        uuid or cls must be specified, but not both. If cls is specified, name must be specified as well
        """
        if attr in cls.attributes:

            if uuid:
                if cls: raise ValueError("Only one of uuid and cls must be specified")

                device = self.device_uuids[uuid]

            elif cls:
                if not name: raise ValueError("If cls is specified, name must be as well")

                device = self.device_names[cls.__name__][name]

            else: raise ValueError("uuid or cls must be specified")

            setattr(device, attr, value)

        else:
            raise AttributeError(f"Attribute '{attr}' not accessible")

    def set_routine(self, trigger: IotTrigger, routine: IotRoutine):
        pass


def _test_random_brightness():

    import random
    import time

    lights = []
    for light in controller.device_names[HueLight]:
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

    controller.set_attr("on"        , True, cls=HueLight, name="Dining Room 1")
    controller.set_attr("on"        , True, cls=HueLight, name="Dining Room 2")
    controller.set_attr("brightness", 254 , cls=HueLight, name="Dining Room 1")
    controller.set_attr("brightness", 254 , cls=HueLight, name="Dining Room 2")

    value1 = controller.get_attr("brightness", cls=HueLight, name="Dining Room 1")
    value2 = controller.get_attr("brightness", cls=HueLight, name="Dining Room 2")

    conditional = IotConditional(value1, IotConditional.equals, value2)

    print(f"Room1: {value1()} | Room2 {value2()}")
    print(bool(conditional))

    controller.set_attr("brightness", 0, cls=HueLight, name="Dining Room 2")

    print(f"Room1: {value1()} | Room2 {value2()}")
    print(bool(conditional))


if __name__ == '__main__':

    controller = IotController()

    bridge = HueBridge(controller)

    controller.add_device(IRSensor())

    _test_conditionals()

    action_list = [lambda: controller.set_attr("brightness", 0, cls=HueLight, name="Dining Room 2")]
    events = [IotEvent(action_list)]

    value1 = controller.get_attr("brightness", cls=HueLight, name="Dining Room 1")
    value2 = controller.get_attr("brightness", cls=HueLight, name="Dining Room 2")
    conditional = IotConditional(value1, IotConditional.lt_equals, value2)

    routine = IotRoutine(events, conditional)

    trigger = IotTrigger(routine, value1, IotTrigger.check_gt, 80)
    controller.set_attr("brightness", 70, cls=HueLight, name="Dining Room 2")
    controller.set_attr("brightness", 100, cls=HueLight, name="Dining Room 2")
    value2()

    # Room1: 254 | Room2 254
    # True
    # Room1: 0 | Room2 0
    # True
    # Subscribed to < iot_device._Attribute.__get__. < locals >._Inner object at 0x7fd90a6af3c8 >
    # Checking 70
    # Checking 100
    # Triggered 100
    # Checking 0







