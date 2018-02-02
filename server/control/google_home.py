from control.iot_device import IotDevice
from control.iot_device import action, attribute


class GoogleHome(IotDevice):

    def __init__(self):

        super(GoogleHome, self).__init__()

        self._is_querying = None

    @action
    def query(self):
        pass

    @attribute
    def is_querying(self):
        return self._is_querying

