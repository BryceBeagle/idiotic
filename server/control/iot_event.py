from typing import Union, List, Callable


class IotEvent:

    def __init__(self, actions):

        self._actions = []

        self.actions = actions

    def __call__(self, *args, **kwargs):
        for action in self.actions:
            action()

    @property
    def actions(self) -> List[Callable]:
        return self._actions

    @actions.setter
    def actions(self, actions: Union[Callable, List[Callable]]):
        """Set list of actions for event

        actions must be a Callable or list of Callables
        """
        if isinstance(actions, Callable):
            self._actions = [actions]
        elif isinstance(actions, list):
            if not all(isinstance(action, Callable) for action in actions):
                raise TypeError("action is not a Callable or list of Callable")
            self._actions = actions
        else:
            raise TypeError("action is not a Callable or list of Callable")
