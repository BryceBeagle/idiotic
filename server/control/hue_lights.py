import phue

from iot_device import IotDevice
from iot_device import action, attribute


class HueLight(IotDevice):

    def __init__(self):
        super(HueLight, self).__init__()

        self._room = None
        self._brightness = None

    @action
    def pulse_lights(self):
        pass

    @action
    def dim_lights(self):
        pass

    @attribute
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        self._room = room
