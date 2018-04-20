from control.idiotic_device import IdioticDevice
from control.idiotic_device import Behavior, Attribute


class Thermostat(IdioticDevice):
    """Thermostat device. Able to switch output modes between AC, Fan, and Heat
    """

    def __init__(self):

        super().__init__()

        self._active_device = None

    @Attribute
    def active_device(self):
        """Currently active device"""
        return self._active_device

    @active_device.updater
    def active_device(self, active_device):
        self._active_device = active_device

    @active_device.setter
    def active_device(self, active_device):
        """Change the output mode of the device"""
        # TODO: Does not work on embedded device yet
        self.ws.get().send(f'{{"set" : {{"{active_device}"}}}}')

