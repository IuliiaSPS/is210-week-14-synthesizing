#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


def xfibo(count):
    """Fibonacci number generator.

    Args:
        count(int): The number of Fibonacci numbers to return.

    Returns:
        int: Ganarated Fibonacci numbers.

    Examples:

        >>> for i in xfibo(5):
            print i
        0
        1
        1
        2
        3
    """
    my_var1 = 0
    my_var2 = 1
    counter = 0
    while True:
        if counter >= count:
            return
        yield my_var1
        my_var1, my_var2 = my_var2, my_var1 + my_var2
        counter += 1
