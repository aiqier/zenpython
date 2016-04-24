# -*- coding: utf-8 -*-

"""
作为一个服务能正常启动的上下文.
"""


import ConfigParser
from util.baseclass import Singleton


class Config(Singleton):
    """
    需要被设置的项
    hq_server_url: 行情服务地址
    """
    def set_with_dict(self, di):
        self.hq_server_url = di["hq_server_url"]

    def set_with_file(self, file):
        cf = ConfigParser.ConfigParser()
        cf.read(file)
        self.hq_server_url = cf.get("hq", "hq_server_url")
