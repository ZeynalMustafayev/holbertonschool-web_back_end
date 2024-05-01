#!usr/bin/env python3
"""sum list"""


def sum_list(input_list:list[float]) -> float:
    sum = 0
    for i in input_list:
        sum += i
    return sum