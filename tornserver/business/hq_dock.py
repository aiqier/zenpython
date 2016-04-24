# -*- coding: utf-8 -*-

"""
对接行情服务
"""

import tornado.gen

from util.baseclass import AsyncRequest
from util.iolooptools import put_get_request_into_ioloop


class Config():
    def __init__(self):
        self.hq_server_url = "http://www.aiqier.com"

config = Config()

class HqRequest(AsyncRequest):
    @tornado.gen.coroutine
    def get(self, context, url):
        return put_get_request_into_ioloop(context, url)

    def __init__(self, context):
        self.context = context

    @staticmethod
    def format_request_url(params):
        url = "http://%s/fcgi-bin/hqquery_serv?hqfrom=%s&hqto=%s&df=%s&dt=%s&type=text" % (config.hq_server_url, params["str_from"], params["str_to"], params["str_date"], params["str_date"])
        return url

    @staticmethod
    def parser_response(response, str_date):
        """
        解析失败是应该打印到日志中的,方便以后排查问题
        :param response:
        :param str_date:
        :return:
        """
        try:
            for line in response.split("\n"):
                items = line.split("\t")
                if items != [] and items[2] == str_date:
                   return (items[0], items[1], items[2], items[3], items[4])
            else:
                return None
        except:
            return None

    @tornado.gen.coroutine
    def fetch(self, params):
        """
        获取行情数据,如果成功,返回FTD,航线,最低价
        失败则返回None
        :param params:
        :return:
        """
        url = self.format_request_url(params)
        ok, response = yield self.get(self.context, url)
        if ok:
            self.parser_response(response, params["str_date"])
        else:
            tornado.gen.Return(None)