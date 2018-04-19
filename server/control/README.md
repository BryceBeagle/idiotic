This directory is for all things controller. A summary of the purposes of each file/directory is provided below:

* `device_drivers/` - Directory where device-drivers should be placed. These files outline the abilities of each device
in the system
* `idiotic_conditional.py` - Contains the `IdioticConditional` class, used by IdioticRoutines and IdioticEvents for
requirements testing before executing
* `idiotic_controller.py` - The meat of the directory. Manages device driver instances and IdioticRoutines
* `idiotic_device.py` - Has base `IdioticDevice` class for device drivers to inherit from, as well as `Attributes` and
`Behavior` decorators
* `idiotic_routine.py` - Contains the `IdioticRoutine` class, which manage the flow of functionality in the system
* `idiotic_trigger.py` - Contains the `IdioticTrigger` class, used by IdioticRoutines to subscribe to device attributes

See the readme in `device_drivers/` for how to create a new device driver to be added to the system
