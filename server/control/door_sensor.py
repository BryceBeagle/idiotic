from iot_device import IotDevice
from iot_device import action, attribute


class DoorSensor(IotDevice):

    def __init__(self):

        super(DoorSensor, self).__init__()

        self.state = None

    @attribute
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self_state = state
