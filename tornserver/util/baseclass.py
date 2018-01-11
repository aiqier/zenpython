# -*- coding: utf-8 -*-


"""
一些被继承和使用的基础工具
"""

import logging

import tornado.web
import tornado.gen
import tornado.httpclient
from tornado import ioloop


logger = logging.getLogger(__name__)

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
    def __init__(self, context):
        """
        请求上下文
        :param context:
        :return:
        """
        self.context = context


    def format_request(self, params):
        raise NotImplementedError


    def parser_response(self, response, params):
        raise NotImplementedError

    @tornado.gen.coroutine
    def put_get_request_into_ioloop(self, url, origin=False):
        if origin:
            logger.info("Request:%s\t%s" % (self.context["handler_id"], url))
        try:
            client = tornado.httpclient.AsyncHTTPClient()
            response = yield client.fetch(url)
            if origin:
                logger.info("Response:%s\t%s" % (self.context["handler_id"], response.body))
        except:
            logger.error("ErrorRequest:%s\t%s" % (self.context["handler_id"], url), exc_info=True)
            raise tornado.gen.Return((False, None))
        else:
            raise tornado.gen.Return((True, response.body))


    @tornado.gen.coroutine
    def put_post_request_into_ioloop(self, url, body, origin=False):
        """
        把一个异步post请求扔到tornado ioloop中
        :param url: 请求url
        :param body: 请求体
        :param handler_id: 处理id
        :param origin: 是否日志请求和响应原串
        :return:
        True, 返回结果
        False, None
        """
        if origin:
            logger.info("Request:%s\t%s\t%s" % (self.context["handler_id"], url, body))
        try:
            client = tornado.httpclient.AsyncHTTPClient()
            response = yield client.fetch(url, method="POST", body=body)
            if origin:
                logger.info("Response:%s\t%s" % (self.context["handler_id"], response.body))
        except:
            logger.error("ErrorRequest:%s\t%s\t%s" % (self.context["handler_id"], url, body), exc_info=True)
            raise tornado.gen.Return((False, None))
        else:
            raise tornado.gen.Return((True, response.body))


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