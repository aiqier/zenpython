#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(path, "../"))

import mock
import tornado.gen
import tornado.ioloop
import tornado.testing
import tornado.concurrent


from business.hello_action import fetch_weather

from setting.config import init_configer
init_configer("/Users/liuaiqi/config/zenserver.conf")


class TestMock(tornado.testing.AsyncTestCase):

    @mock.patch("tornado.httpclient.AsyncHTTPClient")
    @tornado.testing.gen_test
    def test_mock(self, AsyncHTTPClient):
        AsyncHTTPClient.return_value = mock_http_client = mock.MagicMock()
        fetch_future = tornado.concurrent.Future()
        mock_http_client.fetch.return_value = fetch_future
        fetch_future.set_result(mock.MagicMock(body="rain"))


        expect = "city:PEK/date:2016-04-06/weather:rain"
        actual = yield fetch_weather({"queryid": "xxxx"}, "PEK", "2016-04-06")


        self.assertEqual(actual, expect)