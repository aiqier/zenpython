#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(path, "../"))

from business.hello_action import add
from setting.logging_config import init_debug_logger

def setup():
    init_debug_logger("")


def test_add_well_ok():
    """
    正常的数据,返回
    :return:
    """
    a = 4
    b = 5
    expect = 9
    actual = add(a, b)
    assert expect == actual