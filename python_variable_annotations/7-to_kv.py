#!/usr/bin/env python3
"""to_kv"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv"""
    v **= 2
    return k, v
