class IotDevice:

    actions = []
    attributes = []

    def __init__(self):

        self._uuid = None
        self._name = None

    @classmethod
    def get_actions(cls):
        return cls.actions

    @classmethod
    def _action(cls, func):
        cls.actions.append(func)

        return func

    @classmethod
    def _attribute(cls, func):
        cls.attributes.append(func)

        func = property(func)

        return func

    # TODO: Get decorators working within class using magic
    # @_attribute()
    # def uuid(self):
    #     return self._uuid
    #
    # @uuid.setter
    # def uuid(self, id):
    #     self._uuid = id
    #
    # @_attribute()
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, name):
    #     self._name = name



action    = IotDevice._action
attribute = IotDevice._attribute
