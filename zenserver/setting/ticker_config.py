#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.baseclass import BaseTicker
from util.baseclass import singleton

from setting.config import Configer

config = Configer()

@singleton
class SimpleTicker(BaseTicker):

    def update(self):
        print "tick,tick.."


def init_ticker():
    si = SimpleTicker()
    si.set_time(config.TICKER_SIM_TIME)
    si.start()
