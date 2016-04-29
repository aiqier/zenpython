# -*- coding: utf-8 -*-


"""
获取行情服务
"""

import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(path, "../"))

import mock

import tornado.gen
import tornado.ioloop
import tornado.testing
from tornado.concurrent import Future
from types import MethodType

from util.iolooptools import put_get_request_into_ioloop


class TestMock(tornado.testing.AsyncTestCase):
    @mock.patch("tornado.httpclient.AsyncHTTPClient")
    @tornado.testing.gen_test
    def test_mock(self, AsyncHTTPClient):
        AsyncHTTPClient.return_value = mock_http_client = mock.MagicMock()
        fetch_future = tornado.concurrent.Future()
        mock_http_client.fetch.return_value = fetch_future
        fetch_future.set_result(mock.MagicMock(body="test"))

        response = yield put_get_request_into_ioloop("the url")
        self.assertEqual(response.body, "test")