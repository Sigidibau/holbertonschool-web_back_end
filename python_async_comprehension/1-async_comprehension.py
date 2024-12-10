#!/usr/bin/env python3
"""Async generator"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    Coroutine that collects 10 random numbers from the async_generator
    using async comprehension.

    Returns:
        list: A list containing 10 random numbers generated asynchronously.
    """
    result = [num async for num in async_generator()][:10]
    return result
