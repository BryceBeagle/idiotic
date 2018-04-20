The purpose of this project was to create a modular Internet of Things (IoT) system to create an interface between DIY
devices and consumer grade products. The end product is focused on the automation of household tasks and behaviors for
these devices, with functionality resembling a combination of IFTTT (If This Then That; used for integration between
different web services) and Tasker (used for automating system actions on a cellphone). Users have the ability to
integrate devices and services from off-the-shelf products and services, as well as third party or homebrewed solutions.

This project provides a design architecture as well as an implementation thereof. The architecture describes a system
that addresses all of the design requirements, while the implementation makes it happen. The implementation provides the
software required to run the system, as well as a set of physical modules that are able to work with it. The modules
include parts lists, PCB schematics, board designs, and embedded software ‒ everything required to create and deploy one
from scratch.

Users are able to configure their system to create collections of tasks, called routines, that are triggered by internal
or external state changes, such as the time transitioning to a predesignated time of the day, or a door being opened.
These routines contain events, or sequences of actions to perform, where each action is an atomic operation for a device
to execute. A routine can contain one or more events, and each event can contain one or more actions to perform. For
example, if a user wants their Philips Hue internet-connected light bulbs to turn on automatically when they open a
specific door, they can create a routine that is run when a predesignated door sensor is activated. Devices send status
updates to a server which listens to the changing values and notifies routines that are subscribed to pieces of data.

The system has a server that handles connections and routes incoming data to device driver instances using a data
control library, henceforth referred to as the controller. The controller manages routines and events in the system as
well as the data structure that holds all of the device instances. Devices, both physical (e.g., a Temperature Sensor)
and cloud-based (e.g., a Google Home), are configured for use by the controller with driver files that express the
capabilities of the hardware or software that they represent. For example, a driver for the Philips Hue smart light
bulbs would express the ability to set and retrieve attributes such as brightness, hue, saturation and on/off state, as
well as behaviors such as dimming and pulsing.

Routines, events, and devices are stored in a configuration, allowing the system to start up preconfigured and ready for
use. Events referenced in routines must have corresponding configuration entries describing them, and devices mentioned
in events must also have drivers that the controller can access and utilize. Storing configurations in non-volatile,
text-based formats allows them to be version controlled, shared, and edited with relative ease.

The software provided with this project, called Idiotic, is an extendable implementation of the system described above.
It is written in Python 3, with the server implemented with the Flask web framework library. Routines, events, and
devices are loaded from JSON configuration files. There are also a small number of PCB devices, designed using Eagle,
that function with the system as a demonstration of functionality.

Developers that wish to integrate their own devices into Idiotic can make use of the server’s client platform agnostic
websocket-based API to integrate their device within the system, using the simple, documented protocol. Creating a
single driver file in a designated directory is all that is required to allow the controller to handle data from, and
make commands to, a new device type. All integrated devices are treated as a first-class citizens within the system.

Furthermore, if the new device is built on an ESP8266 microcontroller platform, there is a provided library that allows
for expedited embedded development and integration within the system. A developer simply needs to extend a template file
to map which functions are correlated with which pieces of data and behaviors. If the new device is unable to utilize
this library, it simply needs to connect to the server over a Websocket and follow a simple communication protocol.

Modules currently in the system:
* Door Open/Close Sensor (already developed but revising is necessary)
* IR blaster/receiver **(hardware only)** - Send IR signals to TV (with ability to record and reproduce remote signals)
* HVAC Thermostat
* Temperature sensor
* Hue Light support
		
Core features of the software  include:
* Ability to utilize and integrate all created PCB modules
* Ability to interface modules together to create useful routines and actions
* Ability to add DIY modules with an easy to use interface
