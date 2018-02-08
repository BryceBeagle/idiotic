import types

class _IdioticAttribute:
    """Attribute object that acts like a more powerful, and more confusing, property

    class.func = 5   --> func.__set__(5) --> sets self._func to val
    a = class.func   --> func.__get__    --> return func object
    a = class.func() --> func.__call__   --> returns value of func
    """

    def __init__(self, fget, fset=None, fdel=None, doc=None, subscribers=set()):

        self.fget = fget
        self.fset = fset
        self.fdel = fdel

        if doc is None:
            doc = fget.__doc__
        self.__doc__ = doc

        self.subscribers = subscribers

    def __get__(self, owner, ownertype=None):

        class _Inner(type(self)):

            def __call__(instance):
                return self.fget(owner)

        self.__class__ = _Inner

        return self

    def __set__(self, owner, value):

        if self.fset is None:
            raise AttributeError("can't set attribute")

        for subscriber in self.subscribers:
            subscriber.alert(value)

        self.fset(owner, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__, self.subscribers)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__, self.subscribers)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__, self.subscribers)

    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.discard(subscriber)


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

    @classmethod
    def _attribute(cls, func):
        cls.attributes.add(func.__name__)

        func = _IdioticAttribute(func)

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
attribute = IdioticDevice._attribute
