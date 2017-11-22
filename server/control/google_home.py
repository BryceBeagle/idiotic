from iot_device import IotDevice
from iot_device import action, attribute


class GoogleHome(IotDevice):

    def __init__(self):

        super(GoogleHome, self).__init__()

        self._uuid = None
        self._name = None


    @action
    def query(self):
        pass

    @attribute
    def is_querying(self):
        return self.is_querying

