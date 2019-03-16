from control.idiotic_device import IdioticDevice
from control.idiotic_device import Attribute


class Gardenometer(IdioticDevice):
    """A device that reports various metrics related to plant health."""

    def __init__(self):
        super().__init__()

        self._temp: float = None
        self._lux: float = None

    @Attribute
    def temp(self) -> float:
        """
        :return: The temperature in centigrade
        """
        return self._temp

    @Attribute
    def lux(self) -> float:
        """
        :return: The brightness in lux
        """
        return self._lux

    @temp.updater
    def temp(self, temp):
        self._temp = float(temp)

    @lux.updater
    def lux(self, lux):
        self._lux = float(lux)
