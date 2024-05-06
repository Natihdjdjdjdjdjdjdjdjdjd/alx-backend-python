#!/usr/bin/env python3
"""
Create a measure_time function with integers n and max_delay as
arguments that measures the total execution time for wait_n(n, max_delay)
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns total execution time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    last_time = time.time()

    total = last_time - start_time
    return (total/n)
