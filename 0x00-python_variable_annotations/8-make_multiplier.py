#!/usr/bin/env python3
"""function make_multiplier that takes a float multiplier as arg
   ument and returns a function that multiplies a float by multiplier.
   """


from typing import Callable
"""import from typing module"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function that multiplies a float by multiplier"""
    def multiply_by_multiplier(x: float) -> float:
        return x * multiplier
    return multiply_by_multiplier
