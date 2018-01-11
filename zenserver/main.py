# -*- coding: utf-8 -*-

import sys

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
from tornado.options import define, options

from setting.logging_config import init_product_logger, init_debug_logger, init_test_logger
from setting.config import init_configer
from setting.ticker_config import init_ticker

from business.hello_handler import HelloWorld

define("port", default=8000, help=u"服务端口", type=int)
define("config_path", default=None , help=u"配置文件所在路径")
define("num_process", default=1, help="process num", type=int)
define("log_path", default=None, help="log root path")
define("env", default = None, help = "run environment, (d)ebug, (t)est, (p)roduct")

if __name__ == "__main__":

    tornado.options.parse_command_line()

    if options.config_path is None:
        print "need config_path"
        sys.exit(0)
    elif options.log_path is None:
        print "need log_path"
        sys.exit(0)
    elif options.env not in ("d", "t", "p"):
        print "need env in (d)ebug, (t)est, (p)roduct"
        sys.exit(0)


    init_configer(options.config_path)
    # 初始化一切上下文
    if options.env == "debug":
        init_debug_logger(options.log_path)
    elif options.env == "test":
        init_test_logger(options.log_path)
    elif options.env == "product":
        init_product_logger(options.log_path)

    init_ticker()

    app = tornado.web.Application(
        handlers=[(r"/", HelloWorld)]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()