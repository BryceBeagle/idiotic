from control.idiotic_device import IdioticDevice
from control.idiotic_device import Behavior, Attribute


class TempSensor(IdioticDevice):

    def __init__(self):

        super().__init__()

        self._temp = None
        self._temp2 = None

    @Attribute
    def temp(self):
        return self._temp

    @temp.updater
    def temp(self, temp):
        self._temp = temp
