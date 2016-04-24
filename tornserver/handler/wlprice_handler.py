# -*- coding: utf-8 -*-

"""
无线端报价接口handler
"""

try:
    from ujson import encode as json_encode
except ImportError:
    try:
        from cjson import encode as json_encode
    except ImportError:
        from json import dumps as json_encode

try:
    from ujson import decode as json_decode
except ImportError:
    try:
        from cjson import decode as json_decode
    except ImportError:
        from json import loads as json_decode

import tornado.web
import tornado.gen

from util.baseclass import BaseHandler
from wlprice_action import fetch_near_flights


class WlanPriceHandler(BaseHandler):
    """
    无线端报价接口展示

    大部分函数需要一个context对象,
    context是一个上下文函数, 它包含
    queryid: 此次的请求id
    logger: 用于打印日志
    conf: 配置对象
    """

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.write("WLAN PRICE")

        queryid = self.get_argument("queryid", "noqueryid")
        str_from = self.get_argument("from")
        str_to = self.get_argument("to")
        str_date = self.get_argument('date')
        str_filter = self.get_argument('filter', 'ktep3')
        source_id = self.get_argument('sourceid', 'kxmb')
        action = self.get_argument("action", "noaction")

        response = yield fetch_near_flights(queryid, str_from, str_to, str_date, queryid, 0)
        self.finish(response)
        return


