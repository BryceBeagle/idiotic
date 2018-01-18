from typing import Union, Set, Iterable

# TODO: Fix cyclic import
# from iot_routine import IotRoutine


class IotTrigger:

    def __init__(self, watch_event=None):

        self._routines = set()
        """
        Set of IotRoutines that are subscribed to this trigger.
        Must be updated whenever the IotRoutine updates its trigger [TODO: trigger set]
        """

        if watch_event is not None:
            # Add IotTrigger instance to watch list of watch_event
            # When watch_event is triggered, it will call self.trigger()
            watch_event.subscribe(self)

    def trigger(self) -> None:
        """Trigger all subscribed routines"""
        for routine in self.routines:
            routine()

    @property
    def routines(self):  # -> Set[IotRoutine]:  TODO: Fix cyclic import
        """Get set of routines that are subscribed to this IotTrigger instance"""
        return self._routines

    @routines.setter
    def routines(self, routines):  # Union[IotRoutine,  TODO: Fix cyclic import
                                   #       Iterable[IotRoutine]]):
        """Set routine set"""

        from iot_routine import IotRoutine  # TODO: Fix cyclic import

        # Single IotRoutine
        if isinstance(routines, IotRoutine):
            self._routines = {routines}

        # Iterable (ie set, list) of IotRoutines
        elif isinstance(routines, Iterable):
            if not all(isinstance(routine, IotRoutine) for routine in routines):
                raise TypeError("routines is not an instance or list of IotRoutine")
            self._routines = set(routines)

        # Invalid IotRoutine type
        else:
            raise TypeError("routines is not an instance or list of IotRoutine")
