# -*- coding: utf-8 -*-

"""
字符串常用工具
"""

def is_empty(s):
    """
    字符串为空
    :param s:
    :return:
    """
    if s is None:
        return True

    if not s.strip():
        return True
    return False

def is_not_empty(s):
    """
    字符串非空
    :param s:
    :return:
    """
    return not is_empty(s)