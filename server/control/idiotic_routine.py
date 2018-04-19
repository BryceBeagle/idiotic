from typing import List, Union

from control.idiotic_trigger import IdioticTrigger
from control.idiotic_event import IdioticEvent
from control.idiotic_conditional import IdioticConditional


class IdioticRoutine:
    """Sequence of events to run when triggered with a satisfied conditional

    Each IdioticRoutine has only one trigger, but multiple IdioticRoutines can
    have the same IdioticEvent, with different triggers, allowing the events to
    be used with different routines, for different situations.

    Each routine can have a list of conditionals that must be satisfied for the
    routine to run, once triggered. Each event can also have associated
    conditionals for finer control.
    """

    def __init__(self, events=None, conditionals=None):
        """Initialize an IdioticRoutine

        The trigger for the routine is initialized _after_ using the routine as
        an argument. This may be changed in the future.

        Conditionals are optional. If none are supplied, the events are always
        executed when the routine is triggered

        :param events: List of events to execute
        :param conditionals: Requirements for routine to run once triggered
        """
        self._trigger = None
        self._events = []
        self._conditionals = []

        # Use properties
        self.events = events
        self.conditionals = conditionals

        self._name = None

    def __call__(self, *args, **kwargs):
        """Trigger all events in routine after verifying conditionals pass"""

        # All conditionals for routine must be true
        if not all(self.conditionals):
            return

        # Run all events in event list
        for event in self.events:
            event()

    @property
    def trigger(self) -> IdioticTrigger:
        """Get trigger"""
        return self._trigger

    @trigger.setter
    def trigger(self, trigger: IdioticTrigger):
        """Set trigger"""
        self._trigger = trigger

    @property
    def events(self) -> List[IdioticEvent]:
        """Get events"""
        return self._events

    @events.setter
    def events(self, events: Union[IdioticEvent, List[IdioticEvent]]):
        if isinstance(events, IdioticEvent):
            self._events = [events]
        elif isinstance(events, list):
            self._events = events
        else:
            raise Exception("event list is not properly formatted")

    def add_event(self, event: IdioticEvent):
        """Add another event"""
        self._events.append(event)

    def remove_event(self, event: IdioticEvent):
        """Remove an event"""
        self._events.remove(event)

    @property
    def conditionals(self) -> List[IdioticConditional]:
        """Conditionals for the routine"""
        return self._conditionals

    @conditionals.setter
    def conditionals(self, conditionals: Union[None, IdioticConditional,
                                               List[IdioticConditional]]):
        # No conditionals
        if conditionals is None:
            self._conditionals = []

        # Single conditional
        elif isinstance(conditionals, IdioticConditional):
            self._conditionals = [conditionals]

        # List of conditionals
        elif isinstance(conditionals, list):
            self._conditionals = conditionals

        else:
            raise TypeError("conditionals must all be instances of "
                            "IotConditional")
