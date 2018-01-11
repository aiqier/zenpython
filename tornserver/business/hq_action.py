# -*- coding: utf-8 -*-

"""
行情对接服务
"""

import tornado.gen

from util.baseclass import AsyncRequest
from servicecontext.config import Config

config = Config.instance()
config.hq_server_url = "www.baidu.com"

class HqAsyncRequest(AsyncRequest):
    """
    请求行情服务对接
    """

    def format_request(self, params):
        url = "http://%s/fcgi-bin/hqquery_serv?hqfrom=%s&hqto=%s&df=%s&dt=%s&type=text" % (config.hq_server_url, params["str_from"], params["str_to"], params["str_date"], params["str_date"])
        return url


    def parser_response(slef, response, params):
        """
        解析失败是应该打印到日志中的,方便以后排查问题
        :param response:
        :param str_date:
        :return:
        """
        try:
            for line in response.split("\n"):
                items = line.split("\t")
                if items != [] and items[2] == params["str_date"]:
                    return (items[0], items[1], items[2], items[3], items[4])
            else:
                return None
        except:
            return None

    @tornado.gen.coroutine
    def fetch(self, params):
        url = self.format_request(params)
        ok, response = yield self.put_get_request_into_ioloop(self.context, url)
        if ok:
            raise tornado.gen.Return(self.parser_response(response, params))
        else:
            raise tornado.gen.Return(None)