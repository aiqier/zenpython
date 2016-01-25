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
