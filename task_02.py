#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02"""


import task_01


def fibo(count):
    """Function does some transformation.

    Args:
        count(int): The total number of Fibonacci numbers to return.

    Returns:
        list: Fibnacci sequence stored as list.

    Examples:

    >>> fibo(5)
    [0, 1, 1, 2, 3]
    """
    return list(task_01.xfibo(count))
