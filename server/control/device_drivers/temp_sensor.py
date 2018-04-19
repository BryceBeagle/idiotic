from control.idiotic_device import IdioticDevice
from control.idiotic_device import Attribute


class TempSensor(IdioticDevice):
    """Device whichs reads the current temperature from an MCP9808 temperature sensor
    and reports its to the system
    """

    def __init__(self):
        super().__init__()

        self._temp: float = None

    @Attribute
    def temp(self) -> float:
        """Temperature reported by MCP9808"""
        return self._temp

    @temp.updater
    def temp(self, temp):
        self._temp = float(temp)
