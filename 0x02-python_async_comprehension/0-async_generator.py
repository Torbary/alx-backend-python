#!/usr/bin/env python3
"""
0-async_generator
"""


import asyncio
import random


async def async_generator():
    """retrun random.uniform()"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
