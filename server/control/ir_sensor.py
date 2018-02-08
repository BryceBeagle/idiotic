from control.idiotic_device import IdioticDevice
from control.idiotic_device import action, attribute


class IRSensor(IdioticDevice):

    def __init__(self):

        super(IRSensor, self).__init__()

        self.signals = {}

    @action
    def add_signal(self, name, signal):
        self.signals[name] = signal

    @action
    def send_signal(self, name):
        pass
