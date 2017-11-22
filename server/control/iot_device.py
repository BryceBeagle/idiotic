import sys


def action(func):
    print(f"Action: {func.__name__}")
    # actions = sys._getframe(1).f_locals.get('globals')['IotDevice'].actions
    # if actions is not None:
    #     actions.append(func)
    return func


def attribute(func):

    print(f"Attribute: {func.__name__}")

    name = func.__name__

    @property
    def decorator():
        func()

    return decorator


class IotDevice:

    actions = []
    properties = []

    def __init__(self):

        self._uuid = None

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, id):
        self._uuid = id

    @classmethod
    def get_actions(cls):
        return cls.actions
