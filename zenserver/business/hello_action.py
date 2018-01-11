#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging

import tornado.gen

from util.iolooptools import put_get_request_into_ioloop
from setting.config import Configer

logger = logging.getLogger(__name__)
config = Configer()

def hello():
    return "hello,world"


def add(a, b):
    logger.debug("add %s %s" % (a, b))
    logger.info("hq server url: %s" % config.HQ_SERVER_URL)

    return a + b


@tornado.gen.coroutine
def fetch_weather(context, city, date):
    url = "%s/city=%s&date=%s" % (config.WEATHER_SERVER_URL, city, date)
    ok, result = yield put_get_request_into_ioloop(context, url)
    if ok:
        raise tornado.gen.Return("city:%s/date:%s/weather:%s"% (city, date, result))
    else:
        raise tornado.gen.Return(None)
