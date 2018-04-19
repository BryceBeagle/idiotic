from control.idiotic_device import IdioticDevice
from control.idiotic_device import Attribute


class DoorSensor(IdioticDevice):
    """Door Sensor module. Uses a Hall Effect + a magnet to sense the door"""

    def __init__(self):
        super().__init__()

        self._door_open = None

    @Attribute
    def door_open(self):
        """Whether or not the door is open or closed"""
        return self._door_open

    @door_open.updater
    def door_open(self, door_open):
        # Turn the 0/1 received in the JSON into a False/True
        self._door_open = bool(door_open)
