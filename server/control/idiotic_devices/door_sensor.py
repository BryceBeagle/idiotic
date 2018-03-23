from control.idiotic_device import IdioticDevice
from control.idiotic_device import Behavior, Attribute


class DoorSensor(IdioticDevice):

    def __init__(self):

        super(DoorSensor, self).__init__()

        self._state = None

    @Attribute
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
