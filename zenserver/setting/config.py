#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
服务器配置
"""


import ConfigParser

from util.baseclass import singleton

@singleton
class Configer(object):

    def instance_with_file(self, file):
        """
        从文件中
        :param file:
        :return:
        """

        cf = ConfigParser.ConfigParser()
        cf.read(file)
        self.WEATHER_SERVER_URL = cf.get("weather", "weather_server_url")
        self.TICKER_SIM_TIME = cf.getint("ticker", "sim_time")



def init_configer(file):
    Configer().instance_with_file(file)