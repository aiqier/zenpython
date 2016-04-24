# -*- coding: utf-8 -*-

"""
简单好用的,和时间有关的类
"""

import datetime

def is_early_than_today(date):
    """
    :param date like 2016-05-04
    当前日期是否比今天还早
    :return:
    """
    year, month, day = date.split("-")
    date = datetime.datetime(year=int(year), month=int(month), day=int(day))
    now = datetime.datetime.now()
    now_date = datetime.datetime(year=now.year, month=now.month, day=now.day)
    return date < now_date


def get_tomorrow_label():
    """
    获得明天的时间标签
    :return:
    """
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days = 1))
    return "%s-%02d-%02d" % (tomorrow.year, tomorrow.month, tomorrow.day)