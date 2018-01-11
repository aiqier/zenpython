# -*- coding: utf-8 -*-

"""
简单方便使用的工具类
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


def get_diff_time(stime):
    delta_time = datetime.datetime.strptime(stime, "%H:%M:%S") - datetime.datetime.now()
    diff_time = delta_time.seconds * 1000 + delta_time.microseconds / 1000 + 1
    return diff_time