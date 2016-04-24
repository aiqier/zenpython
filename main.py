# -*- coding: utf-8 -*-

def percent(s):
    """
    使用百分比显示浮点数
    """
    return "%.2f%%" % (s*100)

# ------------------------------------

from collections import OrderedDict
def dedup_list(li):
    """
    list去重(保持顺序)
    """
    return list(OrderedDict.fromkeys(li))

# ------------------------------------

import string
import random
def rand_str_n(n):
    """
    生成一个n位随机字符串,包含数字和字母
    """
    return ''.join([(string.ascii_letters+string.digits)[x] for x in random.sample(range(0,62),n)])

# ------------------------------------

# 使用这两个函数方便的存储解析结果，大量的减小响应时间
import pickle
def load_dict(file):
    with open(file, 'rb') as f:
        return pickle.load(f)

def save_dict(file, di):
    with open(file, 'wb') as f:
        pickle.dump(di, f)

# ------------------------------------

import datetime
def in_fourteenth_day(day1, day2):
    """
    day1和day2的日期间隔在14天内
    :param day1: 
    :param day2: 
    :return: 
    """
    y1, m1, d1 = day1.split("-")
    y2, m2, d2 = day2.split("-")
    date1 = datetime.datetime(int(y1), int(m1), int(d1))
    date2 = datetime.datetime(int(y2), int(m2), int(d2))
    if date1 + datetime.timedelta(14) < date2:
        return False
    return True
