# -*- coding: utf-8 -*-

"""
测试临近航班
"""

import tornado.testing

import logging

import tornado.gen
from tornado import ioloop

import sys
sys.path.append("../")

from handler.wlprice_action import fetch_near_flights
from util.nearflight import MatchNearFlight

mnf = MatchNearFlight()
mnf.load("../statics/nfdb", "json")




class MyTestCase(tornado.testing.AsyncTestCase):
    @tornado.testing.gen_test
    def test_fetch_hq_price_ok(self):
        @tornado.gen.coroutine
        def mock_fetch_hq_price(context, str_from, str_to, str_date):
            raise tornado.gen.Return(("1", "2", "3", "4", "5"))

        context = {}
        context["logger"] = logging
        str_from = "PEK"
        str_to = "SHA"
        str_date = "2016-04-29"
        queryid = "3239ie923jhew9"
        int_type = 1

        actual = yield fetch_near_flights(context, mock_fetch_hq_price, str_from, str_to, str_date, queryid, int_type)
        assert actual["error"] == 2



# @tornado.gen.coroutine
# def test_fetch_hq_price_ok():
#     def mock_fetch_hq_price(context, str_from, str_to, str_date):
#         raise tornado.gen.Return(("1", "2", "3", "4"))
#
#     context = {}
#     context["logger"] = logging
#     str_from = "PEK"
#     str_to = "SHA"
#     str_date = "2016-04-29"
#     queryid = "3239ie923jhew9"
#     int_type = 1
#
#     actual = yield fetch_near_flights(context, mock_fetch_hq_price, str_from, str_to, str_date, queryid, int_type)
#     print actual
#     assert actual["error"] == "2"
#
# if __name__ == "__main__":
#     logging.basicConfig()
#     io_loop = ioloop.IOLoop.current()
#     io_loop.run_sync(test_fetch_hq_price_ok)
