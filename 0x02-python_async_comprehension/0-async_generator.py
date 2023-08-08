#!/usr/bin/env python3
"""
0-async_generator
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """retrun random.uniform()"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
