#!/usr/bin/env python
# encoding: utf-8


def dollars_to_mills(dollars):
    """Convert dollars to mills, which Simple uses

    :param dollars: Amount to convert
    :type dollars: int, float
    :returns: Input amount, in mills
    :rtype: int
    """
    return int(dollars * 10000)


def mills_to_dollars(mills):
    """Convert mills back to dollars

    :param int mills: Amount to convert
    :returns: Input amount, in mills
    :rtype: float
    """
    return mills / 10000.0
