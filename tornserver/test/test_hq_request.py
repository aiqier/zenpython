# -*- coding: utf-8 -*-

"""
获取行情服务
"""

import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(path, "../"))

import tornado.gen
import tornado.ioloop
from tornado.concurrent import Future
from types import MethodType

from business.hq_dock import HqRequest
from util.baseclass import BaseMock


class HqServerMock(BaseMock):
    @tornado.gen.coroutine
    def get(context, url):
        if url == "http://http://www.aiqier.com/fcgi-bin/hqquery_serv?hqfrom=PEK&hqto=SHA&df=2016-04-10&dt=2016-04-10&type=text":
            return Future()
            #return tornado.gen.Return("PEK\tSHA\t2016-05-10\tMU2007\t1234")

def moctget(self, context, url):
    if url == "http://http://www.aiqier.com/fcgi-bin/hqquery_serv?hqfrom=PEK&hqto=SHA&df=2016-04-10&dt=2016-04-10&type=text":
        yield "PEK\tSHA\t2016-05-10\tMU2007\t1234"

# 初始化请求上下文
request_context = {"handler_id": "test_123456"}

def test_format_request_url_ok():
    hqr = HqRequest(request_context)
    params = {
        "str_from": "PEK",
        "str_to": "SHA",
        "str_date": "2016-04-10",
    }
    expect = "http://http://www.aiqier.com/fcgi-bin/hqquery_serv?hqfrom=PEK&hqto=SHA&df=2016-04-10&dt=2016-04-10&type=text"
    actual = hqr.format_request_url(params)
    assert expect == actual

def test_parser_response_ok():
    hqr = HqRequest(request_context)
    response = "PEK\tSHA\t2016-05-10\tMU2007\t1234"
    expect = ("PEK", "SHA", "2016-05-10", "MU2007", "1234")
    actual = hqr.parser_response(response, "2016-05-10")
    assert expect == actual

def test_parser_response_space_character_return_none():
    hqr = HqRequest(request_context)
    response = ""
    expect = None
    actual = hqr.parser_response(response, "2016-05-10")
    assert expect == actual

@tornado.gen.coroutine
def test_fetch_return_ok():
    hqr = HqRequest(request_context)
    hqr.get = MethodType(moctget, HqRequest)
    #hqmock = HqServerMock()
    #hqr.setattr("get", hqmock.get)
    params = {
        "str_from": "PEK",
        "str_to": "SHA",
        "str_date": "2016-04-10"
    }
    expect = ("PEK", "SHA", "2016-05-10", "MU2007", "1234")
    actual = yield hqr.fetch(request_context, params)
    print expect
    print actual
    assert expect == actual


if __name__ == "__main__":
    res = test_fetch_return_ok()
    tornado.ioloop.IOLoop.instance().start()
    print res
    #res.next()
    #res.next()
    #res.next()
    #print res.send("PEK\tSHA\t2016-05-10\tMU2007\t1234")

