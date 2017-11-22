from iot_device import IotDevice
from iot_device import action, attribute


class DoorSensor(IotDevice):

    def __init__(self):

        super(DoorSensor, self).__init__()

        self._uuid = None
        self._name = None

        self.state = None

    @attribute
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self_state = state
