import types

class IotTrigger:

    def __init__(self, routine, attr, check, value):
        """
        :param attr:   Attribute to subscribe to
        :param parent: Parent IotRoutine to be triggered
        """
        self.check = types.MethodType(check, self)
        self.value = value

        self.routine = routine
        self.routine.trigger = self

        self.subscribe(attr)

    def subscribe(self, attr) -> None:
        """Subscribe to attribute for state changes"""
        print(f"Subscribed to {attr}")
        attr.subscribe(self)

    def alert(self, value) -> None:
        """Called when attr's state changes

        Calls self.trigger() if [conditional] is True

        :param value: value of attr after state change
        """
        print(f"Checking {value}")
        if self.check(value):
            print(f"Triggered {value}")
            self.trigger()

    def trigger(self) -> None:
        """Call parent IotRoutine"""
        self.routine()

    def check_eq(self, attr_value):
        """attr_value == value"""
        return attr_value == self.value

    def check_neq(self, attr_value):
        """attr_value != value"""
        return attr_value != self.value

    def check_gt(self, attr_value):
        """attr_value > value"""
        return attr_value > self.value

    def check_gte(self, attr_value):
        """attr_value >= value"""
        return attr_value >= self.value

    def check_lt(self, attr_value):
        """attr_value < value"""
        return attr_value < self.value

    def check_lte(self, attr_value):
        """attr_value <= value"""
        return attr_value <= self.value

    def check_true(self, attr_value):
        """attr_value == bool(True)"""
        return bool(attr_value)

    def check_false(self, attr_value):
        """attr_value == bool(False)"""
        return not bool(attr_value)
