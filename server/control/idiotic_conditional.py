class IdioticConditional:
    """Object that servers as a conditional

    bool(IdioticConditional()) returns IdioticConditional().check()

    When used, value1 and value2 are _called_, not simply used as values.
    """

    def __init__(self, value1, check, value2=None):
        """Initialize an IdioticConditional

        :param value1: First value
        :param check: Operation to perform
        :param value2: [Optional] Second value, if necessary for check function
        """
        self.value1 = value1
        self.check = check
        self.value2 = value2

    def __bool__(self):
        """Allow usage of class instance as a boolean"""
        return self.check(self)

    def true(self):
        """bool(value1)"""
        return bool(self.value1())

    def false(self):
        """not bool(value1)"""
        return not bool(self.value1())

    def equals(self):
        """value1 == value2"""
        return self.value1() == self.value2()

    def not_equals(self):
        """value1 != value2"""
        return self.value1() != self.value2()

    def lt(self):
        """value1 < value2"""
        return self.value1() < self.value2()

    def lt_equals(self):
        """value1 <= value2"""
        return self.value1() <= self.value2()

    def gt(self):
        """value1 > value2"""
        return self.value1() > self.value2()

    def gt_equals(self):
        """value1 >= value2"""
        return self.value1() >= self.value2()
