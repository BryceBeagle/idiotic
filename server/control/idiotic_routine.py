from typing import List, Dict, Union

from control.idiotic_trigger import IdioticTrigger
from control.idiotic_event import IdioticEvent
from control.idiotic_conditional import IdioticConditional


class IdioticRoutine:
    """Sequence of events

    Each IotRoutine has only one trigger, but multiple IotRoutines can have the same IotEvent, with
    different triggers

    # TODO: Support for multiple triggers?

    Conditionals can be tied to individual IotEvents within the IotRoutine, or to the entire
    IotRoutine
    """

    def __init__(self, events=None, conditionals=None):

        # Will be overridden by properties below, but defining her for PEP8 compliance
        self._trigger = None
        self._events = []
        self._conditionals = {None: []}

        # Use properties
        self.events = events
        self.conditionals = conditionals

        self._name = None

    def __call__(self, *args, **kwargs):
        """Trigger all events in routine"""

        # All conditionals for routine must be true
        if not all(self.conditionals):
            return

        for event in self.events:
            event()

    def __repr__(self):
        trigger_string = '\t' + repr(self.trigger).replace("\n", "\n    ")
        string  = f"Trigger:\n{trigger_string}\n"

        string += "Conditionals:\n"
        for conditional in self.conditionals:
            cond_string = repr(conditional).replace("\n", "\n    ")
            string += f"    {cond_string}\n"

        string += "Events:\n"
        for event in self.events:
            string += f"    {event}\n"

        return string

    @property
    def trigger(self) -> IdioticTrigger:
        """Get trigger"""
        return self._trigger

    @trigger.setter
    def trigger(self, trigger: IdioticTrigger) -> None:
        """Set trigger"""
        if not isinstance(trigger, IdioticTrigger):
            raise Exception("trigger is not an instance of IotTrigger")
        self._trigger = trigger

    @property
    def events(self) -> List[IdioticEvent]:
        """Get events"""
        return self._events

    @events.setter
    def events(self, events: Union[IdioticEvent, List[IdioticEvent]]) -> None:
        """Set event(s)"""
        if isinstance(events, IdioticEvent):
            self._events = [events]
        elif isinstance(events, list):
            if not all(isinstance(event, IdioticEvent) for event in events):
                raise Exception("event is not an instance of IotEvent")
            self._events = events
        else:
            raise Exception("event is not an instance of IotEvent")

    def add_event(self, event: IdioticEvent) -> None:
        """Add another event"""
        if not isinstance(event, IdioticEvent):  # TODO: Support for list of events?
            raise Exception("event is not an instance of IotEvent")
        self._events.append(event)

    def remove_event(self, event: IdioticEvent) -> None:
        """Remove an event"""
        if not isinstance(event, IdioticEvent):  # TODO: Support for list of events?
            raise TypeError("event is not an instance of IotEvent")
        self._events.remove(event)

    @property
    def conditionals(self) -> Dict[Union[None, IdioticConditional], List[IdioticEvent]]:
        """Get conditionals pattern"""

        return self._conditionals

    @conditionals.setter
    def conditionals(self, conditionals: Union[None, IdioticConditional, List[IdioticConditional]]):

        # No conditionals
        if conditionals is None:
            self._conditionals = [True]

        # Single conditional
        elif isinstance(conditionals, IdioticConditional):
            self._conditionals = [conditionals]

        # List of conditionals
        elif isinstance(conditionals, list):
            if not all(isinstance(conditional, IdioticConditional) for conditional in conditionals):
                raise TypeError("conditionals must all be instances of IotConditional")
            self._conditionals = conditionals

        else:
            raise TypeError("conditionals must all be instances of IotConditional")
