# -*- coding: utf-8 -*-

import logging

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
from tornado.options import define, options

from handler.status import StatusHandler
from handler.wlprice_handler import WlanPriceHandler

from util.nearflight import MatchNearFlight

define("port", default=8000, help="服务端口", type=int)
define("configpath", help="配置文件所在路径")

# 我只是害怕单例对象被释放
blood_pool = {}

def loader(blood_pool):
    """
    在这里初始化所有全局对象
    :return:
    """
    mnf = MatchNearFlight()
    blood_pool["mnf"] = mnf.load("statics/nfdb", "json")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/status", StatusHandler),
                  (r"/wlan", WlanPriceHandler)]
    )
    loader(blood_pool)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()