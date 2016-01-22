# -*- coding: utf-8 -*-

def percent(s):
    """
    使用百分比显示浮点数
    """
    return "%.2f%%" % (s*100)


# -------------------------------------

from collections import OrderedDict
def dedup_list(li):
    """
    list去重(保持顺序)
    """
    return list(OrderedDict.fromkeys(li))

# ------------------------------------
