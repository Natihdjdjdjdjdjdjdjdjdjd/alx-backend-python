#!/usr/bin/env python3
"""a module that help to Advanced type annotated function for mapping"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """This function gets the value for a given key in a mapping"""
    if key in dct:
        return dct[key]
    else:
        return default
