import warnings


class IotConditional:

    EQUALS = "=="
    LT = "<"
    LT_EQUALS = "<="
    GT = ">"
    GT_EQUALS = ">="

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

        if self.check is True:
            return self.value1() is True
        if self.check is False:
            return self.value1() is False

        if self.check == self.EQUALS:
            return self.value1() == self.value2()
        if self.check == self.LT:
            return self.value1() < self.value2()
        if self.check == self.LT_EQUALS:
            return self.value1() <= self.value2()
        if self.check == self.GT:
            return self.value1() > self.value2()
        if self.check == self.GT_EQUALS:
            return self.value1() >= self.value2()

