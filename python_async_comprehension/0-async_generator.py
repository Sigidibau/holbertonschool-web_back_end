#!/usr/bin/env python3
"""imports for my asyncio"""


import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields a random integer between 0 and 10,
    10 times with a 1-second asynchronous delay between each yield.

    This function uses asyncio for asynchronous sleep and random for generating
    random numbers.

    Yields:
        int: A random integer between 0 and 10.
    """
    for _ in range(10):
        yield random.randit(0, 10)
        await asyncio.sleep(1)
