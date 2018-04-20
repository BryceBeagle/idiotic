from typing import Set


class Attribute:
    """Decorator for functions within an IdioticDevice instance

    When the .update method is called, each subscribed IdioticTrigger's alert
    method is called. IdioticTriggers can subscribe by calling the .subscribe
    method and unsubscribe by calling the .unsubscribe method.

    Uses some python magic to return a descriptor. The __get__ dundie is
    required to set the owner post initialition, removing the Singleton aspect
    that decorators usually have.
    """

    def __init__(self, fget, fupdate=None, fset=None, owner=None):

        self.fget = fget
        self.fupdate = fupdate
        self.fset = fset

        self.subscribers = set()

        self.owner = owner

    def __get__(self, owner, obj_type=None):
        """Special magical function the user should _never_ worry about.

        Removes the singleton aspect of decorators in a very hacky way. Usually
        decorators are singletons, bound to the Class. We want Attributes bound
        to a class instance.

        By default, Attributes are not bound to a class instance. Luckily,
        whenever they are gotten (i.e., their __get__ method is called),
        the owner class of the attribute (i.e., the device driver instance),
        is passed. We keep that owner and use it to bind the methods to the
        class instance. We also monkeypatch the device driver's Attribute
        attribute to be a _new_ Attribute instance, this time with an owner.

        If the Attribute does have an owner, we simply return the existing one
        that the owning device class has in its dict.

        This is a disgusting function, but is necessary.
        """
        # If not already bound to a class instance
        if not self.owner:
            # Instantiate a new Attribute with an owner
            attr_temp = type(self)(self.fget, self.fupdate, self.fset,
                                   owner=owner)
            # Monkeypatch it into the owner's dict
            setattr(owner, self.fget.__name__, attr_temp)

        # Return the monkeypatched Attribute
        return getattr(owner, self.fget.__name__)

    def get(self):
        """Getter function of Attribute"""
        return self.fget(self.owner)

    def update(self, value, notify=True):
        """Update value of attribute and notify subscribers

        A silent update can be performed by setting notify=False"""

        # TODO: Alert user if fupdate is None

        ret = self.fupdate(self.owner, value)

        if notify:
            for subscriber in self.subscribers:
                subscriber.alert(value)

        return ret

    def set(self, value):
        """Set value using fset"""
        return self.fset(self.owner, value)

    def getter(self, fget):
        """Set the getter function of Attribute"""
        return type(self)(fget, self.fupdate, self.fset)

    def updater(self, fupdate):
        """Set the updater function of the Attribute"""
        return type(self)(self.fget, fupdate, self.fset)

    def setter(self, fset):
        """Set the setter function of the Attribute"""
        return type(self)(self.fget, self.fupdate, fset)

    def subscribe(self, subscriber):
        """Subscribe to Attribute. Subscribers are called when .update is run"""
        self.subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        """Unsubscribe from Attribute"""
        self.subscribers.discard(subscriber)


class Behavior:
    """Add function to function's class' list of Actions"""

    # test = get_class_that_defined_method(func)

    def __init__(self, func, owner=None):
        self.func = func
        self.owner = owner

    def __call__(self, *args, **kwargs):
        return self.func(self.owner, *args, **kwargs)

    def __get__(self, owner, obj_type=None):
        if not self.owner:
            attr_temp = type(self)(self.func, owner=owner)
            setattr(owner, self.func.__name__, attr_temp)

        return getattr(owner, self.func.__name__)


class IdioticDevice:
    """Base class for device drivers.

    Subclasses gain the following attributes:
        uuid
        name
        ws
    """

    def __init__(self):

        self._uuid = None
        self._name = None
        self._ws = None

    @Attribute
    def uuid(self):
        """Device UUID"""
        return self._uuid

    @uuid.updater
    def uuid(self, uuid):
        self._uuid = uuid

    @Attribute
    def name(self):
        """Device name used for external access"""
        return self._name

    @name.updater
    def name(self, name):
        self._name = name

    @Attribute
    def ws(self):
        """Device websocket, if it uses one"""
        return self._ws

    @ws.updater
    def ws(self, ws):
        self._ws = ws

    @classmethod
    def get_attributes(cls) -> Set[str]:
        """Get list of attributes that the device has.

        Upon usage, every attribute (in the normal Python sense of the word) of
        the class is checked to see if it is an instance of the Attribute class.
        """
        attributes = set()
        for name, obj in cls.__dict__.items():
            if isinstance(obj, Attribute):
                attributes.add(name)
        return attributes

    @classmethod
    def get_behaviors(cls) -> Set[str]:
        """Get list of behaviors that the device supports.

        Upon usage, every attribute (in the normal Python sense of the word) of
        the class is checked to see if it is an instance of the Behavior class.
        """
        behaviors = set()
        for name, obj in cls.__dict__.items():
            if isinstance(obj, Behavior):
                behaviors.add(name)
        return behaviors
