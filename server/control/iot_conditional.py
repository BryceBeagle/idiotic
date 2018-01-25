import warnings


class IotConditional:

    def __init__(self, value1, check, value2=None):
        self.value1 = value1
        self.check = check
        self.value2 = value2

    def __bool__(self):

        # TODO: Allow methods of value1/value2 to be used

        # # Both values defined (Most likely something like == or >)
        # if self.value1 and self.value2:
        #     return self.check(self.value1, self.value2)
        #
        # # Only 1 value defined (eg. check  == __bool__())
        # elif self.value1:
        #     return self.check(self.value1)
        # elif self.value2:
        #     warnings.warn("value2 of IotConditional should not be set without value1")
        #     return self.check(self.value2)
        #
        # # Neither value defined
        # else:
        #     raise Exception("Attempted conditional evaluation without values")

        return self.check(self)

    def equals(self):
        return self.value1() == self.value2()

    def not_equals(self):
        return self.value1() != self.value2()

    def lt(self):
        return self.value1() < self.value2()

    def lt_equals(self):
        return self.value1() <= self.value2()

    def gt(self):
        return self.value1() > self.value2()

    def gt_equals(self):
        return self.value1() >= self.value2()
