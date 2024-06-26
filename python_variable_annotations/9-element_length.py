#!/usr/bin/env python3
"""make multiplier"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length"""
    return [(i, len(i)) for i in lst]
