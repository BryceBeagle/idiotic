from control.idiotic_device import IdioticDevice
from control.idiotic_device import Action, Attribute


class IRSensor(IdioticDevice):

    def __init__(self):

        super(IRSensor, self).__init__()

        self.signals = {}

    @Action
    def add_signal(self, name, signal):
        self.signals[name] = signal

    @Action
    def send_signal(self, name):
        pass
