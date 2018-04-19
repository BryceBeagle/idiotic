import types


class IdioticTrigger:
    """Used by a routine to subscribe to an attribute's value

    When the subscribed-to attribute's update function is called, uses the check
    function with the current attribute's value to determine whether or not to
    call the routine
    """

    def __init__(self, routine, attr, check, value):
        """
        :param attr:   Attribute to subscribe to
        """
        # Allows for both str and class function to be passed
        # TODO: This feels clunky
        if isinstance(check, str):
            self.check = getattr(self, check)
        else:
            self.check = types.MethodType(check, self)

        self.value = value

        self.routine = routine
        self.routine.trigger = self

        self.attr = attr
        self.subscribe(attr)

        self.name = None

        self.active = False

    def subscribe(self, attr) -> None:
        """Subscribe to attribute for state changes"""
        print(f"Subscribed to {attr}")
        attr.subscribe(self)

    def alert(self, value) -> None:
        """Called when attr's state changes

        Calls self.trigger() if self.check [conditional] is True

        :param value: value of attr after state change
        """
        print(f"Checking {value}")
        check = self.check(value)
        if check != self.active:
            if check:
                print(f"Triggered {value}")
                self.trigger()
                self.active = True
            else:
                self.active = False

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
