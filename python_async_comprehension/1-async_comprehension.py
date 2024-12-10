#!/usr/bin/env python3
"""aysinc generator"""


import asyncio
import random


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers from the async_generator
    using async comprehension.

    Returns:
        list: A list containing 10 random numbers generated asynchronously.
    """
    result = []
    async for num in async_generator():
        result.append(num)
        if len(result) == 10:
            break
    return result
