#!/usr/bin/env python3
"""the module that defines duck typed function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """The types function that return of the elements of the input are not known"""
    if lst:
        return lst[0]
    else:
        return None
