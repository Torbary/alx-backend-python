#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
"""


import asyncio
from typing import List
from random import randint
from functools import partial


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return a list of floats"""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
