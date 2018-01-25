class _Attribute(property):
    """Subclass of property object that allows properties to be subscribed to

    Whenever the setter for the property is called, all subscribers are notified
    """

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        super().__init__(fget, fset, fdel, doc)

        self.subscribers = set()

    def __set__(self, key, value):

        for subscriber in self.subscribers:
            subscriber.alert(value)

        return super().__set__(key, value)

    def subscribe(self, trigger):
        self.subscribers.add(trigger)

    def unsubscribe(self, trigger):
        self.subscribers.discard(trigger)


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

        func = _Attribute(func)

        return func

    # TODO: Get decorators working within class using magic
    # @attribute
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, id_):
        self._uuid = id_

    # @attribute
    @property
    def name(self):
        """Device name used for external access"""
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    actions.add(uuid)
    actions.add(name)


action    = IotDevice._action
attribute = IotDevice._attribute
