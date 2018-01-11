# -*- coding: utf-8 -*-


"""
被继承和使用的基础工具类,函数
"""

import tornado.web
import tornado.gen
import tornado.httpclient
from tornado import ioloop


class BaseHandler(tornado.web.RequestHandler):
    pass


def singleton(cls, *args, **kw):
    """
    python 单例模式
    :param cls:
    :param args:
    :param kw:
    :return:
    """
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


class BaseTicker(object):
    """
    定时任务,被扔到tornado ioloop中,每到时间点会进行出发
    """

    def update(self):
        """
        此法需要被子类所重写,因为i
        :return:
        """
        raise NotImplementedError

    def set_time(self, time_interval):
        """
        设置更新频率, 以秒为单位
        :param time:
        :return:
        """
        self.time_interval = time_interval

    def start(self):
        self.ioloop = ioloop.PeriodicCallback(self.update, self.time_interval*1000)
        self.ioloop.start()

    def stop(self):
        self.ioloop.stop()


class BaseException(Exception):
    """
    异常基础类
    """
    pass
