from control.idiotic_device import IdioticDevice
from control.idiotic_device import Attribute


class TempSensor(IdioticDevice):

    def __init__(self):

        super().__init__()

        self._temp = None
        self._temp2 = None

    @Attribute
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp

    @Attribute
    def temp2(self):
        return self._temp2

    @temp2.updater
    def temp2(self, temp2):
        self._temp2 = temp2


