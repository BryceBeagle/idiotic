import phue

from iot_device import IotDevice
from iot_device import action, attribute


class HueLight(IotDevice):

    def __init__(self):
        super(HueLight, self).__init__()

        self._room = None
        self._brightness = None

    @action
    def pront(self):
        print("Approaching infinity")

    @attribute
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        self._room = room

    @attribute
    def brightness(self):
        return self._room

    @brightness.setter
    def brightness(self, brightness):
        self._room = brightness

    # @room.setter
    # def room(self, new_room):
    #     self._room = new_room



a = HueLight()
a.brightness = 10
print(a.brightness)
