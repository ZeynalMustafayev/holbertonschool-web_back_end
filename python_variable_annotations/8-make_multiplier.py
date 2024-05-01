#!/usr/bin/env python3
"""make multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier"""
    def mul_func(x: float) -> float:
        """mul_func"""
        return x * multiplier
    return mul_func
