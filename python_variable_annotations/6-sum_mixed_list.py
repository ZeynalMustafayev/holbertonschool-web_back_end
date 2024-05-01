#!/usr/bin/env python3
"""sum mixed list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]])->float:
    """sum_mixed_list"""
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
