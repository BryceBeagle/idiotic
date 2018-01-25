import phue

from iot_device import IotDevice
from iot_device import action, attribute


class HueBridge(phue.Bridge):
    """"""

    __instance = None

    def __new__(cls, *args, **kwargs):

        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return HueBridge.__instance

    def __init__(self):
        super().__init__("192.168.1.202")  # TODO: Dynamic IP


class HueLight(IotDevice):

    bridge = HueBridge()

    def __init__(self, light_id=None, bridge=None):
        super().__init__()

        if bridge is not None:
            self.bridge = bridge

        if light_id is not None:
            self._light = self.bridge[light_id]
            self.name = self._light.name
        else:
            self._light = None

        self._light_id = light_id

    @action
    def pulse_lights(self):
        pass

    @action
    def dim_lights(self):
        pass

    @attribute
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        self._room = room

    @attribute
    def light_id(self):
        return self._light_id

    @attribute
    def on(self):
        return self._light.on

    @on.setter
    def on(self, on):
        self._light.on = on

    @attribute
    def brightness(self):
        return self._light.brightness

    @brightness.setter
    def brightness(self, brightness):
        self._light.brightness = brightness

    @attribute
    def hue(self):
        return self._light.hue

    @hue.setter
    def hue(self, hue):
        self._light.hue = hue

    @attribute
    def saturation(self):
        return self._light.saturation

    @saturation.setter
    def saturation(self, saturation):
        self._light.saturation = saturation

    @attribute
    def groups(self):
        return [group['name'] for group in self.bridge.get_group().values()
                if str(self._light_id) in group['lights']]

    @groups.setter
    def groups(self, groups):

        groups = set(groups)

        for group in self.bridge.groups:
            if group.name in groups:

                # Group already exists
                groups.remove(group.name)

                # Current lights of group
                lights = {light.light_id for light in group.lights}

                # Don't change anything to group if light is already in it
                if self.light_id in lights:
                    continue

                # Add light to group
                lights.add(self.light_id)
                self.bridge.set_group(group.group_id, 'lights', list(lights))

            else:

                # Current lights of group
                lights = {light.light_id for light in group.lights}

                # Don't change anything to group if light is not in group
                if self.light_id not in lights:
                    continue

                # Remove light from group
                lights.remove(self.light_id)

                # Delete group if the light to remove is the only light in the group
                if not lights:
                    self.bridge.delete_group(group.group_id)

                # Remove light from group
                else:
                    self.bridge.set_group(group.group_id, 'lights', list(lights))

        # New groups
        for group in groups:
            self.bridge.create_group(group, [self.light_id])


if __name__ == '__main__':
    a = HueLight(9)
    a.brightness = 5
    print(a.groups)
    a.groups = ['Living Room']
    print(a.groups)
    print(a.attributes)

    pass
