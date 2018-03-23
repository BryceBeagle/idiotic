from control.idiotic_device import IdioticDevice
from control.idiotic_device import Behavior, Attribute


class IRSensor(IdioticDevice):

    def __init__(self):

        super(IRSensor, self).__init__()

        self.signals = {}

    @Behavior
    def add_signal(self, name, signal):
        self.signals[name] = signal

    @Behavior
    def send_signal(self, name):
        pass
