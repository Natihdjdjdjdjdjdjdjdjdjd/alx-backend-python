#!/usr/bin/env python3
"""modules that type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """lets take a mixed list of integers and floats and returns
        their sum as float"""
    add: float = 0.0
    for i in mxd_lst:
        add += i
    return add
