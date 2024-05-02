#!/usr/bin/env python3
'''
For printing the correct output of the wait_n coroutine
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """task_wait_n"""
    sort_list = []
    for _ in range(n):
        sort_list.append(await wait_random(max_delay))
    return sorted(sort_list)
