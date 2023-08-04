#!/usr/bin/env python3
"""type-annoted function that return sum of float"""


from typing import List
"""import from typing"""


def sum_list(input_list: List[float]) -> float:
    """return thier sum as float"""
    return sum(input_list)
