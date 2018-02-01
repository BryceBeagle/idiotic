from typing import List, Dict, Union

from iot_trigger import IotTrigger
from iot_event import IotEvent
from iot_conditional import IotConditional


class IotRoutine:
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

    @property
    def trigger(self) -> IotTrigger:
        """Get trigger"""
        return self._trigger

    @trigger.setter
    def trigger(self, trigger: IotTrigger) -> None:
        """Set trigger"""
        if not isinstance(trigger, IotTrigger):
            raise Exception("trigger is not an instance of IotTrigger")
        self._trigger = trigger

    @property
    def events(self) -> List[IotEvent]:
        """Get events"""
        return self._events

    @events.setter
    def events(self, events: Union[IotEvent, List[IotEvent]]) -> None:
        """Set event(s)"""
        if isinstance(events, IotEvent):
            self._events = [events]
        elif isinstance(events, list):
            if not all(isinstance(event, IotEvent) for event in events):
                raise Exception("event is not an instance of IotEvent")
            self._events = events
        else:
            raise Exception("event is not an instance of IotEvent")

    def add_event(self, event: IotEvent) -> None:
        """Add another event"""
        if not isinstance(event, IotEvent):  # TODO: Support for list of events?
            raise Exception("event is not an instance of IotEvent")
        self._events.append(event)

    def remove_event(self, event: IotEvent) -> None:
        """Remove an event"""
        if not isinstance(event, IotEvent):  # TODO: Support for list of events?
            raise TypeError("event is not an instance of IotEvent")
        self._events.remove(event)

    @property
    def conditionals(self) -> Dict[Union[None, IotConditional], List[IotEvent]]:
        """Get conditionals pattern"""

        return self._conditionals

    @conditionals.setter
    def conditionals(self, conditionals: Union[None, IotConditional, List[IotConditional]]):

        # No conditionals
        if conditionals is None:
            self._conditionals = [True]

        # Single conditional
        elif isinstance(conditionals, IotConditional):
            self._conditionals = [conditionals]

        # List of conditionals
        elif isinstance(conditionals, list):
            if not all(isinstance(conditional, IotConditional) for conditional in conditionals):
                raise TypeError("conditionals must all be instances of IotConditional")
            self._conditionals = conditionals

        else:
            raise TypeError("conditionals must all be instances of IotConditional")
