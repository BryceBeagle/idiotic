# TODO: Do this dynamically
# This file is used by the controller for automatic importing of devices when
# initializing using the configuration json files.

from .door_sensor import DoorSensor
from .ir_sensor import IRSensor
from .hue import HueLight
from .temp_sensor import TempSensor
from .thermostat import Thermostat
