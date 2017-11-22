from iot_device import IotDevice
from iot_device import action, attribute


class IRSensor(IotDevice):

    def __init__(self):

        super(IRSensor, self).__init__()

        self.signals = {}


    @action
    def add_signal(self, name, signal):
        self.signals[name] = signal

    @action
    def send_signal(self, name):
        pass
