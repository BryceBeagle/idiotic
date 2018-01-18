class IotWatch:

    EQUALS = "=="
    LT = "<"
    LT_EQUALS = "<="
    GT = ">"
    GT_EQUALS = ">="

    # TODO: Support specific state transitions
    # TRANSITION = "trans"

    def __init__(self, value1, watch_type, value2, value3=None):

        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

        self.watch_type = watch_type

    def subscribe(self, instance):

        if self.watch_type is True:
            pass
        if self.watch_type is False:
            pass

        if self.watch_type == self.EQUALS:
            pass
        if self.watch_type == self.LT:
            pass
        if self.watch_type == self.LT_EQUALS:
            pass
        if self.watch_type == self.GT:
            pass
        if self.watch_type == self.GT_EQUALS:
            pass
