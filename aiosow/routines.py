from typing import Callable

import asyncio, logging

from aiosow.setup import setup
from aiosow.perpetuate import perpetuate, autofill
from aiosow.bindings import return_true

ROUTINES = []


def clear_routines():
    global ROUTINES
    ROUTINES = []


def get_routines():
    global ROUTINES
    return ROUTINES


def routine(
    frequency: int, condition: Callable = return_true, timeout: int = -1
) -> Callable:
    """
    Specifies a function to be executed as a routine.

    **args**:
    - frequency : the frequency at which the routine should run
    - condition : to prevent the triggering
    - perpetuate : wether the result should be saved in memory
    """

    def decorator(fn: Callable) -> Callable:
        ROUTINES.append(
            {
                "frequency": frequency,
                "timeout": timeout if timeout >= 0 else abs(frequency),
                "function": fn,
                "condition": condition,
            }
        )
        return fn

    return decorator


async def consume_routines(memory):
    routines = get_routines()
    while routines:
        # Find the routine with the smallest remaining timeout or a timeout <= 0
        smallest_timeout_routine = min(routines, key=lambda x: x["timeout"])
        smallest_timeout = smallest_timeout_routine["timeout"]
        if smallest_timeout <= 0:
            smallest_timeout = 0

        # Wait until the smallest timeout has elapsed
        await asyncio.sleep(smallest_timeout)

        # Execute any routines that have timed out
        for routine in routines:
            routine["timeout"] -= smallest_timeout
            if routine["timeout"] <= 0:
                condition = routine["condition"]
                function = routine["function"]
                # Check the condition before running the routine
                try:
                    if await autofill(condition, args=[], memory=memory):
                        await perpetuate(function, args=[], memory=memory)
                except:
                    pass
                # Update the timeout value based on the frequency
                if routine["frequency"] > 0:
                    routine["timeout"] = routine["frequency"]
                else:
                    routines.remove(routine)


async def consumer(memory):  # pragma: no cover
    while True:
        await autofill(consume_routines, memory=memory)


async def spawn_consumer(memory):  # pragma: no cover
    return asyncio.create_task(consumer(memory))


__all__ = ["routine"]
