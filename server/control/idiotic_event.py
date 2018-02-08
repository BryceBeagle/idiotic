from typing import Union, List, Callable

from control.idiotic_conditional import IdioticConditional


class IdioticEvent:

    def __init__(self,
                 actions: Union[Callable, List[Callable]],
                 conditionals: Union[None, IdioticConditional, List[IdioticConditional]] = []):

        self._actions = []
        self._conditionals = []

        self.actions = actions
        self.conditionals = conditionals

    def __call__(self, *args, **kwargs):

        # All conditionals must be true for event to execute
        if not all(self.conditionals):
            return

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

    def add_action(self, action: Callable, index: int = -1):
        self.actions.insert(index, action)

    def remove_action(self, index: int = -1, action: Union[None, Callable] = None):
        """Remove action for action list.

        Defaults to last action of list. If action is not none, it is popped from list.
        """
        if action is not None:
            self.actions.remove(action)
        else:
            self.actions.pop(index)

    @property
    def conditionals(self):
        return self._conditionals

    @conditionals.setter
    def conditionals(self, conditionals):
        self._conditionals = conditionals
