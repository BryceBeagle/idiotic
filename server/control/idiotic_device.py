import types


class Attribute:
    """Decorator for functions within an IdioticDevice instance

    When the set() method is called, each subscribed IdioticTrigger's alert() method is called.
    IdioticTriggers can subscribe by calling the .subscribe() method and unsubscribe by calling the .unsubscribe()
    method.

    Uses some python magic to return a descriptor. The __get__ dundie is required to create an instance of the
    inner class post initialization. To be honest, I'm not quite sure how it works.

    TODO: Populate IdioticDevice.attributes list
    """

    def __init__(self, fget):
        self.fget = fget
        self.fset = None

    def __get__(self, owner, obj_type=None):
        return self._Inner(owner, self.fget, self.fset)

    class _Inner:

        def __init__(self, owner, fget, fset=None, subscribers=set()):
            """Initialize a """
            self.owner = owner

            self.fget = fget
            self.fset = fset

            self.subscribers = subscribers

        def get(self):
            return self.fget(self.owner)

        def set(self, value, notify=True):
            """Set value of attribute and notify subscribers

            A silent set can be performed by setting notify=False"""

            if notify:
                for subscriber in self.subscribers:
                    subscriber.alert(value)

            return self.fset(self.owner, value)

        def getter(self, fget):
            print(self)
            return type(self)(fget, self.fset, self.subscribers)

        def setter(self, fset):
            print(self)
            return type(self)(self.fget, fset, self.subscribers)

        def subscribe(self, subscriber):
            self.subscribers.add(subscriber)

        def unsubscribe(self, subscriber):
            self.subscribers.discard(subscriber)

    def setter(self, fset):
        self.fset = fset
        return self


class IdioticDevice:

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


action    = IdioticDevice._action
