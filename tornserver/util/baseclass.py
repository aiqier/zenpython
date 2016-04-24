# -*- coding: utf-8 -*-


"""
一些被继承和使用的基础工具
"""

import tornado.web
import tornado.gen
import tornado.httpclient

from tornado import ioloop

class BaseHandler(tornado.web.RequestHandler):
    pass


class Singleton(object):
    """
    python单例模式
    """
    INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls.INSTANCE:
            cls.INSTANCE = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.INSTANCE


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
        设置更新频率, 以毫秒为单位
        :param time:
        :return:
        """
        self.time_interval = time_interval

    def start(self):
        self.ioloop = ioloop.PeriodicCallback(self.update, self.time_interval*1000)
        self.ioloop.start()

    def stop(self):
        self.ioloop.stop()


class AsyncRequest(object):
    """
    异步请求处理类
    生成将要发送的数据格式.
    将返回的数据进行解析.
    使用mork类覆盖.请求接口,完成单元测试.

    """
    pass


class BaseException(Exception):
    """
    异常基础类
    """
    pass

class BaseMock(object):
    """
    模拟基础类, 作为python, 有必要实现这两个方法么?
    """
    @staticmethod
    def get(context, url):
        pass

    @staticmethod
    def post(context, url, body):
        pass