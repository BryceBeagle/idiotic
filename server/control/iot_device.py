class IotDevice:

    actions    = set()
    attributes = set()

    def __init__(self):

        self._uuid = None
        self._name = None

    # TODO: Restrict access to only actions and attributes for non-class members
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    @classmethod
    def get_actions(cls):
        return cls.actions

    @classmethod
    def _action(cls, func):
        cls.actions.add(func.__name__)

        return func

    @classmethod
    def _attribute(cls, func):
        cls.attributes.add(func.__name__)

        func = property(func)

        return func

    # TODO: Get decorators working within class using magic
    # @attribute
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, id):
        self._uuid = id

    # @attribute
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    actions.add(uuid)
    actions.add(name)


action    = IotDevice._action
attribute = IotDevice._attribute
