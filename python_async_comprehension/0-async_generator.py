#!/usr/bin/env python3
"""imports for my asyncio program"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random integer between 0 and 10,
    10 times with a 1-second asynchronous delay between each yield.

    This function uses asyncio for asynchronous sleep and random for generating
    random numbers.

    Yields:
        int: A random integer between 0 and 10.
    """
    for _ in range(10):
        yield random.uniform(0.0, 10.0)
        await asyncio.sleep(1)
