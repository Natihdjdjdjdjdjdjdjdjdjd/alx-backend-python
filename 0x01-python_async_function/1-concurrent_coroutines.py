#!/usr/bin/env python3
"""Write an async routine called wait_n that takes in 2
int arguments (in this order): n and max_delay. You will spawn
wait_random n times with the specified max_delay.
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return and Span waitrandom n times"""
    all_tasks = []
    delays = []

    for i in range(n):
        my_task = wait_random(max_delay)
        all_tasks.append(my_task)

    for my_task in asyncio.as_completed((all_tasks)):
        delay = await my_task
        delays.append(delay)

    return delays
