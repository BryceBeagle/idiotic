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

    def __init__(self, trigger=None, events=None, conditionals=None):

        # Will be overridden by properties below, but defining her for PEP8 compliance
        self._trigger = None
        self._events = []
        self._conditionals = {None: []}

        # Use properties
        self.trigger = trigger
        self.events = events
        self.conditionals = conditionals

        self._name = None

    def __call__(self, *args, **kwargs):
        """Trigger all events in routine"""

        # Conditionals that apply to entire IotRoutine (event is []) must all pass
        if not all(conditional() for conditional in self.conditionals if not self.conditionals[conditional]):
            return

        for conditional in self.conditionals:

            # Conditional must be True
            if not conditional():
                return

            # TODO: Use conditionals
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
    def conditionals(self,
                     conditionals: Union[None,                                           # No conditionals
                                         IotConditional,                                 # Single conditional
                                         List[IotConditional],                           # Multiple conditionals
                                         Dict[IotConditional, Union[IotEvent,            # Single paired conditional
                                                                    List[IotEvent]]]]):  # Multiple paired conditionals
        """Set conditionals

        Conditionals can either be tied to IotEvents within the IotRoutine, or to the entire
        IotRoutine

        # TODO: Support for if-else type conditionals

        Takes a number of different formats:

        None: No conditionals whatsoever.
        IotConditional(s): Conditionals for entire IotRoutine.
        Dict: Conditionals for IotEvents within the IotRoutine

        """
        # No conditionals
        if conditionals is None:
            self._conditionals = {None: []}

        # Single conditional for entire IotRoutine
        elif isinstance(conditionals, IotConditional):
            self._conditionals = {conditionals: []}

        # List of conditionals for entire IotRoutine
        elif isinstance(conditionals, list):
            self._conditionals = dict((conditional, []) for conditional in conditionals)

        # Dict of conditionals and IotEvents
        elif isinstance(conditionals, dict):
            for key in conditionals:

                # Single IotEvent
                if isinstance(conditionals[key], IotEvent):
                    conditionals[key] = [IotEvent]

                # List of IotEvents
                elif isinstance(conditionals[key], list):
                    if not all(isinstance(item, IotEvent) for item in conditionals[key]):
                        raise TypeError(f"Improper conditionals format")

                else:
                    raise ValueError(f"Improper conditionals format")

                self._conditionals = conditionals

        else:
            raise TypeError(f"Improper conditionals format")
