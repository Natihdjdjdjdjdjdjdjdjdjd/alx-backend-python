#!/usr/bin/env python3
"""let type-annotated function for sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """let take a list of floats and returns their sum as float"""
    add: float = 0.0
    for x in input_list:
        add += x
    return add
