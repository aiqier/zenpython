# -*- coding: utf-8 -*-

"""
常用的正则表达式
"""
import re

NUMBER_PATTERN = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')

def is_number(s):
    """
    判断一个字符串是否都是数字
    :param s:
    :return:
    """
    return s.match(NUMBER_PATTERN)

def is_valid_price(s):
    """
    判断一个价格字符串是否合法
    :param s:
    :return:
    """
    try:
        p = float(s)
        if p <= 0:
            return False
        return True
    except:
        return False

