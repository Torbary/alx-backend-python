#!/usr/bin/env python3
"""annoted function"""


from typing import Tuple, Union
"""import module"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple"""
    return k, v ** 2
