from control.idiotic_device import IdioticDevice
from control.idiotic_device import Behavior, Attribute


class Thermostat(IdioticDevice):

    def __init__(self):

        super().__init__()

        self._active_device = None

    @Attribute
    def active_device(self):
        return self._active_device

    @active_device.updater
    def active_device(self, active_device):
        self._active_device = active_device

    @active_device.setter
    def active_device(self, active_device):
        # TODO: Does not work on embedded device yet
        self.ws.get().send(f'{{"get" : {{"{active_device}"}}}}')

