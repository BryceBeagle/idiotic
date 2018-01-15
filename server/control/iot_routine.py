from typing import List, Dict, Union

from iot_trigger import IotTrigger
from iot_event import IotEvent
from iot_conditional import IotConditional


class IotRoutine:
    """Sequence of events

    Each IotRoutine has only one trigger, but multiple IotRoutines can have the same IotEvent, with
    different triggers

    Conditionals can be tied to individual IotEvents within the IotRoutine, or to the entire
    IotRoutine
    """

    def __init__(self, trigger=None, events=None, conditionals=None):

        self._trigger = self.trigger(trigger)
        self._events = self.events(events)
        self._conditionals = self.conditionals(conditionals)

        self._name = None

    @property
    def trigger(self) -> IotTrigger:
        """Get trigger"""
        return self._trigger

    @trigger.setter
    def trigger(self, trigger: IotTrigger) -> None:
        """Set trigger"""
        self._trigger = trigger

    @property
    def events(self) -> List[IotEvent]:
        """Get events"""
        return self._events

    @events.setter
    def events(self, events: List[IotEvent]) -> None:
        """Set events"""
        self._events = events

    def add_event(self) -> None:
        """Add another event"""
        pass

    def remove_event(self) -> None:
        """Remove an event"""
        pass

    @property
    def conditionals(self) -> Dict[IotConditional, IotEvent]:
        "Get conditionals pattern"
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
            self._conditionals = {None, None}

        # Single conditional for entire IotRoutine
        elif isinstance(conditionals, IotConditional):
            self._conditionals = {[conditionals], None}

        # List of conditionals for entire IotRoutine
        elif isinstance(conditionals, list):
            self._conditionals = {conditionals, None}

        # Dict of conditionals and IotEvents
        elif isinstance(conditionals, dict):
            for key in conditionals:

                # Single IotEvent
                if isinstance(conditionals[key], IotEvent):
                    conditionals[key] = [IotEvent]

                # List of IotEvents
                elif isinstance(conditionals[key], list):
                    if not all(isinstance(item, IotEvent) for item in conditionals[key]):
                        raise ValueError(f"Improper conditionals format")

                else:
                    raise ValueError(f"Improper conditionals format")
                self._conditionals = conditionals

        else:
            raise ValueError(f"Improper conditionals format")

        self._conditionals = conditionals
