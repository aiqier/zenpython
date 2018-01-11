# -*- coding: utf-8 -*-

"""
行情接口单元测试
"""

import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(path, "../"))


import mock
import tornado.gen
import tornado.ioloop
import tornado.testing
import tornado.concurrent

from business.hq_action import HqAsyncRequest

class TestMock(tornado.testing.AsyncTestCase):
    @mock.patch("tornado.httpclient.AsyncHTTPClient")
    @tornado.testing.gen_test
    def test_mock_false(self, AsyncHTTPClient):
        AsyncHTTPClient.return_value = mock_http_client = mock.MagicMock()
        fetch_future = tornado.concurrent.Future()
        mock_http_client.fetch.return_value = fetch_future
        fetch_future.set_result(mock.MagicMock(body="test"))

        hqsr = HqAsyncRequest({"handler_id": "kxmsxxxx"})
        params = {
            "str_from": "PEK",
            "str_to": "SHA",
            "str_date": "2016-05-10"
        }
        response = yield hqsr.fetch(params)
        self.assertEqual(response, None)


    @mock.patch("tornado.httpclient.AsyncHTTPClient")
    @tornado.testing.gen_test
    def test_mock_true(self, AsyncHTTPClient):
        AsyncHTTPClient.return_value = mock_http_client = mock.MagicMock()
        fetch_future = tornado.concurrent.Future()
        mock_http_client.fetch.return_value = fetch_future
        fetch_future.set_result(mock.MagicMock(body="PEK\tSHA\t2016-05-10\tMU2007\t1234"))

        hqsr = HqAsyncRequest({"handler_id": "kxmsxxxx"})
        params = {
            "str_from": "PEK",
            "str_to": "SHA",
            "str_date": "2016-05-10"
        }
        response = yield hqsr.fetch(params)
        self.assertEqual(response, ("PEK", "SHA", "2016-05-10", "MU2007", "1234"))