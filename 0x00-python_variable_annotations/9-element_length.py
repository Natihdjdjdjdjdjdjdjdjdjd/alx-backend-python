#!/usr/bin/env python3
"""module that type-annotated function element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """it returns as list of int and tuples of sequence"""
    return [(i, len(i)) for i in lst]
