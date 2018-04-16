from control.idiotic_device import IdioticDevice
from control.idiotic_device import Attribute


class DoorSensor(IdioticDevice):

    def __init__(self):
        super().__init__()

        self._door_open = None

    @Attribute
    def door_open(self):
        return self._door_open

    @door_open.updater
    def door_open(self, door_open):
        self._door_open = door_open
