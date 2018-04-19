from typing import Union, List, Callable

from control.idiotic_conditional import IdioticConditional


class IdioticEvent:
    """List of atomic actions to perform with the device, with a conditional

    Actions are usually attribute.setter functions or behaviors
    """

    def __init__(self, actions: Union[Callable, List[Callable]],
                 conditionals: Union[IdioticConditional,
                                     List[IdioticConditional]] = ()):

        self._actions = []
        self._conditionals = []

        self.actions = actions
        self.conditionals = conditionals

    def __call__(self, *args, **kwargs):
        """Verifies that all conditionals pass. If so, executes the actions"""

        # All conditionals must be true for event to execute
        if not all(self.conditionals):
            return

        # Run every action in the action list
        for action in self.actions:
            action()

    @property
    def actions(self) -> List[Callable]:
        """Return action list"""
        return self._actions

    @actions.setter
    def actions(self, actions: Union[Callable, List[Callable]]):
        """Set list of actions for event

        actions must be a Callable or list of Callables. Bare callables are
        wrapped into a single-length list internally
        """
        if isinstance(actions, Callable):
            self._actions = [actions]
        elif isinstance(actions, list):
            self._actions = actions
        else:
            raise TypeError("action list is not properly formatted")

    def add_action(self, action: Callable, index: int = -1):
        """Add an action at an index in the list

        :param action: Action to add to to action list
        :param index: Index in action list. Defaults to -1 (end of list)
        """
        self.actions.insert(index, action)

    def remove_action(self, index: int = -1,
                      action: Union[None, Callable] = None):
        """Remove action for action list, based on index

        Defaults to last action of list. If action is not none, it is popped
        from list.
        """
        if action is not None:
            self.actions.remove(action)
        else:
            self.actions.pop(index)

    @property
    def conditionals(self):
        """Return conditionals required to run actions in action list"""
        return self._conditionals

    @conditionals.setter
    def conditionals(self, conditionals):
        """Set conditionals required to run actions in action list"""
        self._conditionals = conditionals
