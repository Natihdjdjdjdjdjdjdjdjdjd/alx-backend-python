#!/usr/bin/env python3
"""modules that type-annotated function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """let our tuple of a string and a float return"""
    x = v ** 2
    return (k, x)
