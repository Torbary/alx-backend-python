#!/usr/bin/env python3
"""type-annoted function"""


from typing import List, Union
"""import List from typing"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum"""
    return sum(mxd_lst)
